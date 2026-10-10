#!/usr/bin/env python3
"""Basic online license-list checker for the public SAAD-PRO repository.

Convenience gating only, not strong DRM: the list and client are public,
local checks can be patched, and GitHub may cache raw-file responses.
"""

from __future__ import annotations

import hmac
import json
from datetime import date, datetime, timezone
from urllib.error import URLError
from urllib.request import Request, urlopen

LICENSES_URL = (
    "https://raw.githubusercontent.com/yem96778037/SAAD-PRO/main/licenses.json"
)
MAX_RESPONSE_BYTES = 1_000_000


def _load_license_list() -> list[object]:
    request = Request(
        LICENSES_URL,
        headers={
            "User-Agent": "SAAD-PRO-License-Checker/1.0",
            "Accept": "application/json",
        },
    )
    with urlopen(request, timeout=10) as response:
        raw = response.read(MAX_RESPONSE_BYTES + 1)
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ValueError("License list is too large")

    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("licenses"), list):
        raise ValueError("Expected a JSON object containing a licenses list")
    return payload["licenses"]


def check_license(code: str) -> tuple[bool, str]:
    """Return (is_valid, explanation); expiry is inclusive through that UTC date."""
    code = code.strip()
    if not code:
        return False, "أدخل كود الترخيص."

    try:
        licenses = _load_license_list()
    except (URLError, TimeoutError, OSError):
        return False, "تعذّر الاتصال بقائمة التراخيص؛ حاول مرة أخرى لاحقًا."
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
        return False, "قائمة التراخيص غير صالحة أو لم تُنشر بعد."

    match: dict[str, object] | None = None
    for entry in licenses:
        if not isinstance(entry, dict):
            continue
        candidate = entry.get("code")
        if isinstance(candidate, str) and hmac.compare_digest(candidate, code):
            if match is not None:
                return False, "يوجد كود مكرر في قائمة التراخيص؛ راجع الملف."
            match = entry

    if match is None:
        return False, "الكود غير موجود."
    if match.get("enabled", True) is not True:
        return False, "هذا الترخيص معطّل."

    expires_text = match.get("expires")
    if not isinstance(expires_text, str):
        return False, "تاريخ انتهاء هذا الترخيص غير صالح."
    try:
        expires = date.fromisoformat(expires_text)
    except ValueError:
        return False, "اكتب تاريخ الانتهاء بصيغة YYYY-MM-DD."

    today_utc = datetime.now(timezone.utc).date()
    if today_utc > expires:
        return False, "انتهت صلاحية هذا الترخيص."
    return True, "الكود صالح."


def main() -> int:
    try:
        code = input("أدخل كود الترخيص: ")
    except (EOFError, KeyboardInterrupt):
        print("تم الإلغاء.")
        return 1

    valid, message = check_license(code)
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
