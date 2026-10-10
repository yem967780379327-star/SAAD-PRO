
join = "https://t.me/+GqgtmTVZN1I3OTA0"

ادخل هنا = "https://t.me/+GqgtmTVZN1I3OTA0"

import itertools as it
import math, struct, shutil, os, re, sys, time, zlib, hashlib, tempfile
import copy as _cp
import subprocess
import importlib
from io import BytesIO
from dataclasses import dataclass
from functools import lru_cache
from pathlib import PurePath, Path
from typing import List, Dict, Tuple, Optional, Any
from datetime import datetime
from collections import Counter, defaultdict

ARABIC_OK = False
try:
    import arabic_reshaper
    subprocess.run(['fribidi', '--version'], capture_output=True, check=True)
    ARABIC_OK = True
except Exception:
    ARABIC_OK = False


def ar(text):
    if not ARABIC_OK:
        return text
    try:
        shaped = arabic_reshaper.reshape(text)
        r = subprocess.run(['fribidi', '--rtl'], input=shaped,
                           capture_output=True, text=True, timeout=5)
        return r.stdout.strip() or text
    except Exception:
        return text


LANG = "en"

STRINGS = {
    "en": {
        "title": "SAAD INJ",
        "subtitle": "SMART EDITION v1.0",
        "lang_prompt": "Choose language",
        "lang_en": "English",
        "lang_ar": "العربية",
        "menu_title": "MAIN MENU - SMART OPTION 1 ONLY",
        "m4": "SMART REPACK TO PATH (NEW FILES)",
        "m0": "EXIT",
        "your_choice": "ENTER YOUR CHOICE",
        "invalid": "Invalid choice! Only 1 or 2.",
        "exit_msg": "Thank you for using SAAD INJ",
        "goodbye": "Goodbye!",
        "owner": "Owner",
        "telegram": "Telegram",
        "contact": "Contact",
        "header": "HEADER",
        "menu_border": "SAAD INJ - SMART EDITION",
        "select_pak": "Select PAK file (SMART REPACK TO PATH)",
        "target_path": "Target path inside PAK",
        "default_path": "Enter = default",
        "path_prompt": "Path",
        "processing": "PROCESSING",
        "success": "SUCCESS",
        "error": "ERROR",
        "output": "OUTPUT",
        "found_files": "Found files in LUA folder",
        "no_files": "No files found in LUA folder!",
        "analyzing": "Analyzing PAK intelligently",
        "analysis_done": "Analysis done in",
        "files": "files",
        "proceed": "Proceed with repack? y/n",
        "cancelled": "Repack cancelled by user.",
        "backup": "Backup created",
        "backup_failed": "Backup failed",
        "files_to_repack": "Files to repack",
        "no_files_repack": "No files to repack!",
        "processed": "Processed",
        "added_new": "Added new",
        "verifying": "Verifying round-trip",
        "verified": "Verified - files byte-for-byte identical",
        "successfully": "Successfully processed",
        "file_s": "file(s)",
        "game_ready": "PAK is GAME READY!",
        "no_processed": "No files processed!",
        "repack_failed": "Repack failed",
        "press_enter": "Press Enter to continue...",
        "no_pak": "No pak files in",
        "select_file": "Select file number",
        "invalid_sel": "Invalid selection",
        "valid_number": "Enter a valid number",
        "pak_not_found": "INPUT folder not found",
        "smart_repack": "Smart repacking",
        "target": "Target",
        "path_required": "No path",
        "invalid_path": "Invalid path",
        "interrupted": "Interrupted.",
        "error_label": "ERROR",
        "std_open_fail": "Standard open failed, retrying OD mode",
        "cannot_open": "Cannot open PAK",
        "skipping": "Skipping",
        "no_template": "No template",
        "same_name": "Same name exists",
        "same_ext_dir": "Same extension in same dir",
        "same_ext": "Same extension",
        "most_common": "Most common combo",
        "fallback": "fallback",
        "replace_existing": "Replace existing file",
        "dry_run": "DRY-RUN",
        "repack_plan": "REPACK PLAN",
        "analyzer": "SMART ANALYZER",
        "analysis_report": "PAK ANALYSIS REPORT",
        "file_label": "File",
        "size_label": "Size",
        "version_label": "Version",
        "index_enc": "Index enc.",
        "rsa_hash": "RSA hash",
        "mount": "Mount point",
        "total_files": "Total files",
        "total_dirs": "Total dirs",
        "compression_methods": "Compression Methods",
        "encryption_methods": "Encryption Methods",
        "most_combo": "Most-common combo",
        "smart_reason": "Smart reasoning",
        "valid": "VALID",
        "mismatch": "MISMATCH",
        "yes": "YES",
        "no": "NO",
        "large_pak": "Large PAK - loading into memory",
        "method": "Method",
        "count": "Count",
        "action": "Action",
        "template": "Template",
        "empty": "(empty)",
        "done": "done",
    },
    "ar": {
        "title": "سعد",
        "subtitle": "سعد المخلافي ",
        "lang_prompt": "اختر اللغة",
        "lang_en": "English",
        "lang_ar": "العربية",
        "menu_title": "القائمة الرئيسية - الخيار الذكي 1 فقط",
        "m4": "إعادة الحزم الذكية إلى المسار (ملفات جديدة)",
        "m0": "خروج",
        "your_choice": "ادخل اختيارك",
        "invalid": "اختيار غير صحيح! فقط 1 أو 2.",
        "exit_msg": "شكراً لاستخدامك سعد",
        "goodbye": "مع السلامة!",
        "owner": "المالك",
        "telegram": "تليجرام",
        "contact": "للتواصل",
        "header": "الترويسة",
        "menu_border": "نسخة تجريبية - فقط",
        "select_pak": "اختر ملف PAK (إعادة الحزم الذكية)",
        "target_path": "المسار الهدف داخل PAK",
        "default_path": "Enter = الافتراضي",
        "path_prompt": "المسار",
        "processing": "جاري المعالجة",
        "success": "نجاح",
        "error": "خطأ",
        "output": "المخرج",
        "found_files": "تم إيجاد ملفات في مجلد lua",
        "no_files": "لا توجد ملفات في مجلد lua!",
        "analyzing": "جاري تحليل PAK بذكاء",
        "analysis_done": "تم التحليل في",
        "files": "ملف",
        "proceed": "هل تريد المتابعة؟ y/n",
        "cancelled": "تم إلغاء إعادة الحزم.",
        "backup": "تم إنشاء نسخة احتياطية",
        "backup_failed": "فشل النسخ الاحتياطي",
        "files_to_repack": "الملفات لإعادة الحزم",
        "no_files_repack": "لا توجد ملفات لإعادة الحزم!",
        "processed": "تمت المعالجة",
        "added_new": "تمت الإضافة",
        "verifying": "جاري التحقق",
        "verified": "تم التحقق - الملفات متطابقة بايت ببايت",
        "successfully": "تمت معالجة",
        "file_s": "ملف",
        "game_ready": "PAK جاهز للعبة!",
        "no_processed": "لم تتم معالجة أي ملف!",
        "repack_failed": "فشلت إعادة الحزم",
        "press_enter": "اضغط Enter للمتابعة...",
        "no_pak": "لا توجد ملفات pak في",
        "select_file": "اختر رقم الملف",
        "invalid_sel": "اختيار غير صحيح",
        "valid_number": "ادخل رقماً صحيحاً",
        "pak_not_found": "مجلد input غير موجود",
        "smart_repack": "جاري إعادة الحزم الذكية",
        "target": "الهدف",
        "path_required": "لا يوجد مسار",
        "invalid_path": "مسار غير صحيح",
        "interrupted": "تم المقاطعة.",
        "error_label": "خطأ",
        "std_open_fail": "فشل الفتح العادي، إعادة المحاولة في وضع OD",
        "cannot_open": "لا يمكن فتح PAK",
        "skipping": "تخطي",
        "no_template": "لا يوجد قالب",
        "same_name": "نفس الاسم موجود",
        "same_ext_dir": "نفس الامتداد في نفس المجلد",
        "same_ext": "نفس الامتداد",
        "most_common": "أكثر combo استخداماً",
        "fallback": "احتياطي",
        "replace_existing": "استبدال الملف الموجود",
        "dry_run": "تجربة جافة",
        "repack_plan": "خطة إعادة الحزم",
        "analyzer": "المحلل الذكي",
        "analysis_report": "تقرير تحليل PAK",
        "file_label": "الملف",
        "size_label": "الحجم",
        "version_label": "الإصدار",
        "index_enc": "تشفير الفهرس",
        "rsa_hash": "تجزئة RSA",
        "mount": "نقطة التركيب",
        "total_files": "إجمالي الملفات",
        "total_dirs": "إجمالي المجلدات",
        "compression_methods": "طرق الضغط",
        "encryption_methods": "طرق التشفير",
        "most_combo": "أكثر combo استخداماً",
        "smart_reason": "الاستنتاج الذكي",
        "valid": "صحيح",
        "mismatch": "غير متطابق",
        "yes": "نعم",
        "no": "لا",
        "large_pak": "PAK كبير - جاري التحميل للذاكرة",
        "method": "الطريقة",
        "count": "العدد",
        "action": "الإجراء",
        "template": "القالب",
        "empty": "(فارغ)",
        "done": "تم",
    },
}

ZAIN = str.maketrans({
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ',
    'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ',
    'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ',
    'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
    'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ꜰ', 'G': 'ɢ',
    'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
    'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
    'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ',
})


def fancy(text):
    try:
        return text.translate(ZAIN)
    except Exception:
        return text


def S(key, **kw):
    raw = STRINGS[LANG].get(key, key)
    if kw:
        raw = raw.format(**kw)
    if LANG == "ar":
        return ar(raw)
    return fancy(raw)


def Sraw(key, **kw):
    raw = STRINGS[LANG].get(key, key)
    if kw:
        raw = raw.format(**kw)
    if LANG == "ar":
        return ar(raw)
    return raw


REQUIRED_LIBS = [
    ("rich", "rich"),
    ("gmalg", "gmalg"),
    ("Crypto", "pycryptodome"),
    ("zstandard", "zstandard"),
    ("arabic_reshaper", "arabic-reshaper"),
]


def _try_import(mod_name):
    try:
        importlib.import_module(mod_name)
        return True
    except Exception:
        return False


def _pip_install(pkg):
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet",
             "--disable-pip-version-check", pkg],
            check=True, capture_output=True,
        )
        return True
    except Exception:
        return False


def ensure_requirements():
    missing = []
    for mod, pkg in REQUIRED_LIBS:
        if not _try_import(mod):
            missing.append((mod, pkg))
    for mod, pkg in missing:
        try:
            print(f"  [*] {mod}: installing...")
        except Exception:
            pass
        if not _pip_install(pkg):
            try:
                print(f"  [!] {mod}: install failed -> {pkg}")
            except Exception:
                pass


ensure_requirements()

from rich.console import Console
from rich.panel import Panel
from rich.progress import (Progress, SpinnerColumn, TextColumn, BarColumn,
                            TaskProgressColumn, TimeElapsedColumn,
                            TimeRemainingColumn)
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.console import Group
from rich.box import HEAVY_EDGE, ROUNDED, DOUBLE_EDGE, MINIMAL_DOUBLE_HEAD

import gmalg
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_CBC
from Crypto.Hash import SHA1
from Crypto.Util.Padding import unpad
from zstandard import (ZstdDecompressor, ZstdCompressionDict,
                       DICT_TYPE_AUTO, ZstdCompressor)

console = Console()


def _batched(iterable, n):
    data = iterable if isinstance(iterable, (bytes, bytearray)) else list(iterable)
    for i in range(0, len(data), n):
        yield data[i:i + n]


C_GOLD = "#EBCB8B"
C_CYAN = "#88C0D0"
C_BLUE = "#81A1C1"
C_GREEN = "#A3BE8C"
C_RED = "#BF616A"
C_PURPLE = "#B48EAD"
C_ORANGE = "#D08770"
C_DIM = "#4C566A"
C_TEAL = "#8FBCBB"
C_FROST = "#5E81AC"

ADD_TO_PATH_TARGET = "Content/Lua/GameLua/Mod/BRMod/Gameplay/Core"

BASE_DIR = Path("/storage/emulated/0/SAAD--INJ")
INPUT_DIR = BASE_DIR / "input"
LUA_DIR = BASE_DIR / "lua"
DONE_DIR = BASE_DIR / "done"

ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
ZUC_IV = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

RSA_MOD_1 = bytes.fromhex('CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
RSA_MOD_2 = bytes.fromhex('7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

SIMPLE1_DECRYPT_KEY = 121
SIMPLE2_DECRYPT_KEY = bytes.fromhex('E55B4ED1')
SIMPLE2_BLOCK_SIZE = 16

SM4_SECRET_4 = 'eb691efea914241317a8'
SM4_SECRET_2 = 'Q0hVTKey$as*1ZFlQCiA'
SM4_SECRET_NEW = [
    'xG2qW5lP7lV2iN5fN5pG', 'xT1cJ6dL5wC0kK1rB4dK', 'qC4jS5bZ6fL5xE6nD4zA',
    'gD4jQ2aL3bS3lC3xT0iW', 'xU1yQ8wE9zY3gZ3bT5aE', 'uQ3cO2dX7xY4xU7gH7iS',
    'gW1fR0jK6wQ4oN0oK1kZ', 'aJ4pV7iZ7pU4wP2aC2cZ', 'cX6jT3cM2oT3vK0kJ1qN',
    'iT2vS0cS6yT6cZ1sE1lO', 'hM1pH9iY8wM9hT4lN5uJ', 'kG6bC8jK0fL0dE4sH4mL',
    'dB6lB3vE0eZ8wM8rI0aC', 'tP7sP7nI9rA2vQ4cV5yQ', 'aT0cL1yN4pT3sZ7eM2vY',
    'uV6fU8fC9zN3mP5dH8mN', 'rT6aQ6oZ1yM0gO5tO1aN', 'jU5bH7lQ0fM9hK2kI0oF',
    'iQ0eM0mJ7uT0kV6kL5zY',
]

EM_SIMPLE1 = 1
EM_SIMPLE2 = 16
EM_SM4_2 = 2
EM_SM4_4 = 4
EM_SM4_NEW_BASE = 31
EM_SM4_NEW_MASK = ~EM_SM4_NEW_BASE
EM_UNKNOWN_17 = 17

CM_NONE = 0
CM_ZLIB = 1
CM_ZSTD = 6
CM_ZSTD_DICT = 8
CM_MASK = 15


class SM4:
    _S_BOX = bytes([
        52,102,37,116,137,120,228,169,90,65,188,122,214,22,33,35,77,97,218,148,155,223,19,60,105,58,49,10,95,215,153,149,
        241,174,114,61,7,96,36,182,152,238,196,162,45,136,221,141,4,234,187,17,202,62,93,161,246,63,176,151,128,71,43,166,
        230,247,217,177,89,192,124,190,84,40,183,126,79,248,67,110,160,80,14,245,144,184,251,163,123,98,25,70,3,42,185,143,
        159,119,180,91,131,135,8,235,226,30,66,240,15,232,113,106,117,173,85,31,181,171,51,250,127,21,189,133,216,6,104,179,
        82,48,72,11,0,237,239,178,87,142,231,108,213,229,46,83,130,5,249,129,244,86,191,140,75,227,219,74,145,76,44,211,
        64,41,78,32,20,54,121,9,111,209,55,224,57,12,138,146,56,18,53,109,225,253,147,154,23,212,201,156,107,132,38,157,
        175,118,193,158,208,150,197,203,233,115,73,210,205,100,195,199,1,125,243,172,252,222,164,68,50,27,194,186,28,2,198,39,
        69,139,242,24,167,16,81,29,200,207,99,255,47,13,88,206,101,165,220,26,59,134,254,34,92,168,94,103,170,236,112,204])
    _FK = [1184304796, 1270900830, 1493524870, 3164752158]
    _CK = [964907,973793155,2654690407,2916866751,2071233739,1226140771,3348805095,2045549823,388349611,800627875,
           612403927,3721562911,1195432523,3150178931,612053223,2445162591,67183755,1174197155,1393249511,3331183455,
           3822152747,1332317203,1804781383,1990130463,1282653851,3376591251,2910902311,925872959,332098219,735840931,
           396665415,3588844719]

    @staticmethod
    def ROL32(x, n):
        return (x << n) & 0xFFFFFFFF | (x >> (32 - n))

    @staticmethod
    def _BS(X):
        return (SM4._S_BOX[X>>24&255]<<24 | SM4._S_BOX[X>>16&255]<<16 |
                SM4._S_BOX[X>>8&255]<<8 | SM4._S_BOX[X&255])

    @staticmethod
    def _T0(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X,2) ^ SM4.ROL32(X,10) ^ SM4.ROL32(X,18) ^ SM4.ROL32(X,24)

    @staticmethod
    def _T1(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X,13) ^ SM4.ROL32(X,23)

    @staticmethod
    def _key_expand(key, rkey):
        K0 = int.from_bytes(key[0:4],'big') ^ SM4._FK[0]
        K1 = int.from_bytes(key[4:8],'big') ^ SM4._FK[1]
        K2 = int.from_bytes(key[8:12],'big') ^ SM4._FK[2]
        K3 = int.from_bytes(key[12:16],'big') ^ SM4._FK[3]
        for i in range(0,32,4):
            K0 ^= SM4._T1(K1^K2^K3^SM4._CK[i]); rkey[i]=K0
            K1 ^= SM4._T1(K2^K3^K0^SM4._CK[i+1]); rkey[i+1]=K1
            K2 ^= SM4._T1(K3^K0^K1^SM4._CK[i+2]); rkey[i+2]=K2
            K3 ^= SM4._T1(K0^K1^K2^SM4._CK[i+3]); rkey[i+3]=K3

    @classmethod
    def key_length(cls):
        return 16

    @classmethod
    def block_length(cls):
        return 16

    def __init__(self, key):
        if len(key)!=16:
            raise ValueError('Key must be 16 bytes')
        self._rkey=[0]*32
        SM4._key_expand(key,self._rkey)
        self._bb=bytearray()

    def encrypt(self, block):
        RK=self._rkey
        X0=int.from_bytes(block[0:4],'big'); X1=int.from_bytes(block[4:8],'big')
        X2=int.from_bytes(block[8:12],'big'); X3=int.from_bytes(block[12:16],'big')
        for i in range(0,32,4):
            X0^=SM4._T0(X1^X2^X3^RK[i]); X1^=SM4._T0(X2^X3^X0^RK[i+1])
            X2^=SM4._T0(X3^X0^X1^RK[i+2]); X3^=SM4._T0(X0^X1^X2^RK[i+3])
        b=self._bb; b.clear()
        b.extend(X3.to_bytes(4,'big')); b.extend(X2.to_bytes(4,'big'))
        b.extend(X1.to_bytes(4,'big')); b.extend(X0.to_bytes(4,'big'))
        return bytes(b)

    def decrypt(self, block):
        RK=self._rkey
        X0=int.from_bytes(block[0:4],'big'); X1=int.from_bytes(block[4:8],'big')
        X2=int.from_bytes(block[8:12],'big'); X3=int.from_bytes(block[12:16],'big')
        for i in range(0,32,4):
            X0^=SM4._T0(X1^X2^X3^RK[31-i]); X1^=SM4._T0(X2^X3^X0^RK[30-i])
            X2^=SM4._T0(X3^X0^X1^RK[29-i]); X3^=SM4._T0(X0^X1^X2^RK[28-i])
        b=self._bb; b.clear()
        b.extend(X3.to_bytes(4,'big')); b.extend(X2.to_bytes(4,'big'))
        b.extend(X1.to_bytes(4,'big')); b.extend(X0.to_bytes(4,'big'))
        return bytes(b)


class Misc:
    @staticmethod
    def pad_to_n(data,n):
        p=n-len(data)%n
        return data if p==n else data+b'\x00'*p

    @staticmethod
    def align_up(x,n):
        return (x+n-1)//n*n


class Reader:
    def __init__(self, buffer, cursor=0):
        self._b=buffer
        self._c=cursor

    def u1(self,mc=True):
        return self.unpack('B',move_cursor=mc)[0]

    def u4(self,mc=True):
        return self.unpack('<I',move_cursor=mc)[0]

    def u8(self,mc=True):
        return self.unpack('<Q',move_cursor=mc)[0]

    def i4(self, move_cursor=True):
        return self.unpack('<i', move_cursor=move_cursor)[0]

    def s(self,n,mc=True):
        return self.unpack(f'{n}s',move_cursor=mc)[0]

    def unpack(self,f,offset=0,move_cursor=True):
        x=struct.unpack_from(f,self._b,self._c+offset)
        if move_cursor:
            self._c+=struct.calcsize(f)
        return x

    def string(self,mc=True):
        L=self.i4(move_cursor=mc)
        if L==0:
            return ''
        off=0 if mc else 4
        raw=self.unpack(f'{L}s',offset=off,move_cursor=mc)[0].rstrip(b'\x00')
        try:
            s=raw.decode('utf-8')
        except UnicodeDecodeError:
            try:
                s=raw.decode('utf-16-le')
            except UnicodeDecodeError:
                s=raw.decode('utf-8',errors='replace')
        return s.replace('\x00','')


class PakInfo:
    def __init__(self, buffer, ks):
        r=Reader(buffer[-PakInfo._mem_size(-1):])
        self.index_encrypted=((r.u1()^ks[3])&255)==1
        self.magic=r.u4()^ks[2]
        self.version=r.u4()
        if self.version>=6:
            key=struct.pack('<5I',*ks[4:][:5])
            self.index_hash=bytes(a^b for a,b in zip(r.s(20),key))
        else:
            self.index_hash=bytes()
        self.index_size=r.u8()^(ks[10]<<32|ks[11])
        self.index_offset=r.u8()^(ks[0]<<32|ks[1])
        if self.version<=3:
            self.index_encrypted=False

    @staticmethod
    def _mem_size(_):
        return 45


class TencentPakInfo(PakInfo):
    def __init__(self, buffer, ks):
        super().__init__(buffer, ks)
        r=Reader(buffer[-TencentPakInfo._mem_size(self.version):])
        if self.version>=7:
            key=struct.pack('<8I',*ks[7:][:8])
            self.unk1=bytes(a^b for a,b in zip(r.s(32),key))
        else:
            self.unk1=bytes()
        self.packed_key=r.s(256) if self.version>=8 else bytes()
        self.packed_iv=r.s(256) if self.version>=8 else bytes()
        self.packed_index_hash=r.s(256) if self.version>=8 else bytes()
        self.stem_hash=r.u4()^ks[8] if self.version>=9 else 0
        self.unk2=r.u4()^ks[9] if self.version>=9 else 0
        self.content_org_hash=r.s(20) if self.version>=12 else bytes()

    @staticmethod
    def _mem_size(v):
        return PakInfo._mem_size(v)+(32 if v>=7 else 0)+(768 if v>=8 else 0)+(8 if v>=9 else 0)+(20 if v>=12 else 0)

    @staticmethod
    def _mem_size_max():
        return PakInfo._mem_size(-1)+32+768+8+20


class PakCompressedBlock:
    def __init__(self, r):
        self.start=r.u8()
        self.end=r.u8()


@dataclass
class TencentPakEntry:
    def __init__(self, r, v):
        self.content_hash=r.s(20)
        if v<=1:
            _=r.u8()
        self.offset=r.u8()
        self.uncompressed_size=r.u8()
        self.compression_method=r.u4()&CM_MASK
        self.size=r.u8()
        self.unk1=r.u1() if v>=5 else 0
        self.unk2=r.s(20) if v>=5 else bytes()
        if self.compression_method!=0 and v>=3:
            self.compressed_blocks=[PakCompressedBlock(r) for _ in range(r.u4())]
        else:
            self.compressed_blocks=[]
        self.compression_block_size=r.u4() if v>=4 else 0
        self.encrypted=(r.u1()==1) if v>=4 else False
        self.encryption_method=r.u4() if v>=12 else 0
        self.index_new_sep=r.u4() if v>=12 else 0


class PakCrypto:
    class _LCG:
        def __init__(self, seed):
            self.s=seed

        def next(self):
            M32=4294967295
            MSB=2147483648
            def wrap(x):
                x&=M32
                return x if not x&MSB else (x+MSB&M32)-MSB
            x1=wrap(1103515245*self.s)
            self.s=wrap(x1+12345)
            x2=wrap(x1+77880) if self.s<0 else self.s
            return (x2>>16&M32)%32767

    @staticmethod
    def zuc_keystream():
        zuc=gmalg.ZUC(ZUC_KEY,ZUC_IV)
        return [struct.unpack('>I',zuc.generate())[0] for _ in range(16)]

    @staticmethod
    def _xorxor(buf,x):
        return bytes(buf[i]^x[i%len(x)] for i in range(len(buf)))

    @staticmethod
    def _hashhash(buf,n):
        r=bytes()
        for _ in range(math.ceil(n/SHA1.digest_size)):
            r+=SHA1.new(buf).digest()
        return r[:n] if len(r)>=n else r+b'\x00'*(n-len(r))

    @staticmethod
    def _meowmeow(buf):
        if len(buf)<43:
            return bytes()
        x1=buf[1:][:SHA1.digest_size]
        x2=buf[SHA1.digest_size+1:]
        x1=PakCrypto._xorxor(x1,PakCrypto._hashhash(x2,len(x1)))
        x2=PakCrypto._xorxor(x2,PakCrypto._hashhash(x1,len(x2)))
        p1,m=x2[:SHA1.digest_size],x2[SHA1.digest_size:]
        if p1!=SHA1.new(b'\x00'*SHA1.digest_size).digest():
            return bytes()
        skip=1+next((i for i in range(len(m)) if m[i]!=0),0)
        return m[skip:]

    @staticmethod
    def rsa_extract(sig,mod):
        c=int.from_bytes(sig,'little')
        n=int.from_bytes(mod,'little')
        m=pow(c,65537,n).to_bytes(256,'little').rstrip(b'\x00')
        return PakCrypto._meowmeow(Misc.pad_to_n(m,4))

    @staticmethod
    def _decrypt_simple1(ct):
        return bytes(x^SIMPLE1_DECRYPT_KEY for x in ct)

    @staticmethod
    def _decrypt_simple2(ct):
        assert len(ct)%SIMPLE2_BLOCK_SIZE==0
        initial,=struct.unpack('<I',SIMPLE2_DECRYPT_KEY)
        rk=initial
        out=[]
        for x, in struct.iter_unpack('<I',ct):
            rk^=x
            out.append(rk)
        return struct.pack(f'<{len(out)}I',*out)

    @staticmethod
    @lru_cache(maxsize=128)
    def _derive_sm4_key(fp,em):
        stem=fp.stem.lower()
        if em==EM_SM4_2:
            secret=SM4_SECRET_2
        elif em==EM_SM4_4:
            secret=SM4_SECRET_4
        else:
            idx=(em-EM_SM4_NEW_BASE)%len(SM4_SECRET_NEW)
            secret=f'{SM4_SECRET_NEW[idx]}{em}'
        return SHA1.new(str(stem+secret).encode()).digest()[:16]

    @staticmethod
    @lru_cache(maxsize=128)
    def _sm4_context_for_key(key):
        return SM4(key)

    @staticmethod
    def _decrypt_sm4(ct,fp,em):
        key=PakCrypto._derive_sm4_key(fp,em)
        sm4=PakCrypto._sm4_context_for_key(key)
        return bytes(it.chain.from_iterable(sm4.decrypt(x) for x in _batched(ct,16)))

    @staticmethod
    def decrypt_index(ct, pi):
        if pi.version>7:
            key=iv=None
            try:
                key=PakCrypto.rsa_extract(pi.packed_key,RSA_MOD_1)
                iv=PakCrypto.rsa_extract(pi.packed_iv,RSA_MOD_1)
            except Exception:
                pass
            if key and iv and len(key)>=32 and len(iv)>=16:
                try:
                    return unpad(AES.new(key[:32],MODE_CBC,iv[:16]).decrypt(ct),AES.block_size)
                except ValueError:
                    pass
                try:
                    return AES.new(key[:32],MODE_CBC,iv[:16]).decrypt(ct)
                except Exception:
                    pass
            ks=PakCrypto.zuc_keystream()
            xk=struct.pack('<5I',*ks[4:][:5])
            if len(ct)<len(xk):
                ct2=ct+b'\x00'*(len(xk)-len(ct))
            else:
                xk=(xk*(len(ct)//len(xk)+1))[:len(ct)]
                ct2=ct
            return bytes(a^b for a,b in zip(ct2,xk))
        return bytes(PakCrypto._decrypt_simple1(ct))

    @staticmethod
    def _is_simple1_method(m):
        return m==EM_SIMPLE1

    @staticmethod
    def _is_simple2_method(m):
        return m in (EM_SIMPLE2,17)

    @staticmethod
    def _is_sm4_method(m):
        return m in (EM_SM4_2,EM_SM4_4) or (m&EM_SM4_NEW_MASK)!=0

    @staticmethod
    def align_encrypted_content_size(n,em):
        if PakCrypto._is_simple2_method(em):
            return Misc.align_up(n,SIMPLE2_BLOCK_SIZE)
        if PakCrypto._is_sm4_method(em):
            return Misc.align_up(n,16)
        return n

    @staticmethod
    def decrypt_block(ct,fp,em):
        if PakCrypto._is_simple1_method(em):
            return PakCrypto._decrypt_simple1(ct)
        if PakCrypto._is_simple2_method(em):
            return PakCrypto._decrypt_simple2(ct)
        if PakCrypto._is_sm4_method(em):
            return PakCrypto._decrypt_sm4(ct,fp,em)
        raise ValueError(f'Unknown encryption: {em}')

    @staticmethod
    @lru_cache(maxsize=64)
    def generate_block_indices(n,em):
        if not PakCrypto._is_sm4_method(em):
            return list(range(n))
        perm=[]
        lcg=PakCrypto._LCG(n)
        while len(perm)!=n:
            x=lcg.next()%n
            if x not in perm:
                perm.append(x)
        inv=[0]*len(perm)
        for i,x in enumerate(perm):
            inv[x]=i
        return inv


class PakCompression:
    @staticmethod
    @lru_cache(maxsize=8)
    def _zstd_decompressor(d):
        return ZstdDecompressor(d)

    @staticmethod
    def zstd_dictionary(dd):
        return ZstdCompressionDict(dd,DICT_TYPE_AUTO)

    @staticmethod
    def decompress_block(block,d,cm):
        if cm==CM_ZLIB:
            try:
                return zlib.decompress(block)
            except zlib.error:
                return block
        if cm in (CM_ZSTD,CM_ZSTD_DICT):
            if cm!=CM_ZSTD_DICT:
                d=None
            return PakCompression._zstd_decompressor(d).decompress(block)
        raise ValueError(f'Unknown compression: {cm}')


class _TailView:
    def __init__(self,data,total):
        self._d=data
        self._t=total
        self._b=total-len(data)

    def _r(self,i,df):
        return df if i is None else (i if i>=0 else max(0,self._t+i))

    def __getitem__(self,k):
        if isinstance(k,slice):
            s=self._r(k.start,0)
            e=self._r(k.stop,self._t)
            lo=max(0,s-self._b)
            hi=max(0,e-self._b)
            return memoryview(self._d)[lo:hi]
        if k<0:
            k=self._t+k
        return self._d[k-self._b]

    def __len__(self):
        return self._t


_LARGE_FILE_THRESHOLD=512*1024*1024


class TencentPakFile:
    def __init__(self, file_path, is_od=False):
        self._file_path=Path(file_path)
        self._is_od=is_od
        self._file_size=self._file_path.stat().st_size
        self._mount_point=PurePath()
        self._is_zstd_with_dict='zsdic' in str(self._file_path)
        self._zstd_dict=None
        self._files=[]
        self._index={}
        self._large_file=self._file_size>_LARGE_FILE_THRESHOLD
        ks=PakCrypto.zuc_keystream()
        if self._large_file:
            tr=min(self._file_size,TencentPakInfo._mem_size_max()+256)
            with open(self._file_path,'rb') as f:
                f.seek(max(0,self._file_size-tr))
                self._tail_data=f.read()
            buffer=_TailView(self._tail_data,self._file_size)
            self._file_content=None
        else:
            with open(file_path,'rb') as f:
                self._file_content=memoryview(f.read())
            buffer=self._file_content
            self._tail_data=None
        self._pak_info=TencentPakInfo(buffer,ks)
        self._verify_stem_hash()
        self._tencent_load_index()

    def _read_file_range(self,off,sz):
        with open(self._file_path,'rb') as f:
            f.seek(off)
            return f.read(sz)

    def _verify_stem_hash(self):
        if not self._is_od and self._pak_info.version>=9:
            exp=zlib.crc32(self._file_path.stem.encode('utf-32le'))
            if self._pak_info.stem_hash!=exp:
                console.print(f"[bold {C_GOLD}]Stem hash mismatch[/bold {C_GOLD}]")

    def _tencent_load_index(self):
        if self._large_file:
            idx=self._read_file_range(self._pak_info.index_offset,self._pak_info.index_size)
        else:
            idx=bytes(self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size])
        if self._pak_info.index_encrypted:
            idx=PakCrypto.decrypt_index(idx,self._pak_info)
        self._verify_index_hash(idx)
        self._load_index(idx)

    def _verify_index_hash(self, idx):
        exp=self._pak_info.index_hash
        if not self._is_od and self._pak_info.version>=8:
            rh=PakCrypto.rsa_extract(self._pak_info.packed_index_hash,RSA_MOD_2)
            if exp!=rh:
                console.print(f"[bold {C_GOLD}]RSA index hash mismatch[/bold {C_GOLD}]")
        act=SHA1.new(idx).digest()
        if exp!=act:
            console.print(f"[bold {C_GOLD}]Index hash mismatch[/bold {C_GOLD}]")

    @staticmethod
    def _construct_mount_point(mp):
        r=PurePath()
        for part in PurePath(mp).parts:
            if part!='..':
                r/=part
        return r

    def _peek_content(self,off,sz,em):
        sz=PakCrypto.align_encrypted_content_size(sz,em)
        if self._large_file:
            return self._read_file_range(off,sz)
        return self._file_content[off:][:sz]

    def _peek_block_content(self,b,em):
        sz=PakCrypto.align_encrypted_content_size(b.end-b.start,em)
        if self._large_file:
            return self._read_file_range(b.start,sz)
        return self._file_content[b.start:][:sz]

    def _construct_zstd_dict(self,de):
        assert not self._zstd_dict and not de.encrypted and de.compression_method==CM_NONE
        r=Reader(self._peek_content(de.offset,de.size,0))
        dsz=r.u8()
        _=r.u4()
        assert dsz==r.u4()
        self._zstd_dict=PakCompression.zstd_dictionary(r.s(dsz))

    def _load_index(self, idx):
        if self._pak_info.version<=10:
            raise ValueError(f'Unsupported PAK version: {self._pak_info.version}')
        r=Reader(idx)
        self._mount_point=self._construct_mount_point(r.string())
        self._files=[TencentPakEntry(r,self._pak_info.version) for _ in range(r.u4())]
        for _ in range(r.u8()):
            dp=PurePath(r.string())
            e={}
            for _ in range(r.u8()):
                fn=r.string()
                fi=r.i4()
                i=~fi
                if 0<=i<len(self._files):
                    e[fn]=self._files[i]
            if self._is_zstd_with_dict and dp.name=='zstddic':
                if len(e)==1:
                    self._construct_zstd_dict(e[[*e.keys()][0]])
            elif e:
                self._index.update({dp:e})

    def _write_to_disk(self, fp, e, pak_rel):
        if e.encrypted and e.encryption_method==17:
            return
        em=e.encryption_method
        cm=e.compression_method
        try:
            with open(fp,'wb') as f:
                if cm==CM_NONE:
                    data=self._peek_content(e.offset,e.size,em)
                    if e.encrypted:
                        data=PakCrypto.decrypt_block(data,pak_rel,em)
                    f.write(data[:e.uncompressed_size])
                    return
                rem=e.uncompressed_size
                for x in PakCrypto.generate_block_indices(len(e.compressed_blocks),em):
                    data=self._peek_block_content(e.compressed_blocks[x],em)
                    if e.encrypted:
                        data=PakCrypto.decrypt_block(data,pak_rel,em)
                    data=PakCompression.decompress_block(data,self._zstd_dict,cm)
                    if rem<=0:
                        break
                    data=data[:rem]
                    f.write(data)
                    rem-=len(data)
        except Exception as ex:
            console.print(f"[bold {C_GOLD}]{S('skipping')} {fp.name}: {ex}[/bold {C_GOLD}]")
            if fp.exists():
                fp.unlink()

    def extract_entry_to_bytes(self, e, pak_rel):
        if e.encrypted and e.encryption_method==17:
            return None
        em=e.encryption_method
        cm=e.compression_method
        try:
            if cm==CM_NONE:
                data=self._peek_content(e.offset,e.size,em)
                if e.encrypted:
                    data=PakCrypto.decrypt_block(data,pak_rel,em)
                return data[:e.uncompressed_size]
            out=bytearray()
            rem=e.uncompressed_size
            for x in PakCrypto.generate_block_indices(len(e.compressed_blocks),em):
                data=self._peek_block_content(e.compressed_blocks[x],em)
                if e.encrypted:
                    data=PakCrypto.decrypt_block(data,pak_rel,em)
                data=PakCompression.decompress_block(data,self._zstd_dict,cm)
                if rem<=0:
                    break
                data=data[:rem]
                out+=data
                rem-=len(data)
            return bytes(out)
        except Exception:
            return None


def human_size(size):
    for u in ['B','KB','MB','GB','TB']:
        if size<1024.0:
            return f'{size:.2f} {u}'
        size/=1024.0
    return f'{size:.2f} PB'


def _encrypt_plaintext(pt, pak_rel, em):
    if PakCrypto._is_simple1_method(em):
        return bytes(b^SIMPLE1_DECRYPT_KEY for b in pt)
    if PakCrypto._is_simple2_method(em):
        pad=-len(pt)%SIMPLE2_BLOCK_SIZE
        pt+=b'\x00'*pad
        key,=struct.unpack('<I',SIMPLE2_DECRYPT_KEY)
        rk=key
        out=[]
        for x, in struct.iter_unpack('<I',pt):
            c=rk^x
            out.append(c)
            rk^=c
        return struct.pack(f'<{len(out)}I',*out)
    if PakCrypto._is_sm4_method(em):
        key=PakCrypto._derive_sm4_key(pak_rel,em)
        sm4=PakCrypto._sm4_context_for_key(key)
        pad=-len(pt)%16
        if pad>0:
            pt+=b'\x00'*pad
        out=bytearray()
        for i in range(0,len(pt),16):
            b=pt[i:i+16]
            if len(b)<16:
                b=b.ljust(16,b'\x00')
            out.extend(sm4.encrypt(b))
        return bytes(out)
    return pt


def _best_compress(chunk, cm, zd=None):
    if cm==CM_ZLIB:
        return zlib.compress(chunk,9)
    if cm in (CM_ZSTD,CM_ZSTD_DICT):
        d=zd if cm==CM_ZSTD_DICT else None
        for lvl in [22,19,16,13,10,7,4,1]:
            try:
                return ZstdCompressor(level=lvl,dict_data=d,threads=1).compress(chunk)
            except Exception:
                continue
    return chunk


def _pw_string(s):
    if not s:
        return struct.pack('<i',0)
    b=s.encode('utf-8')+b'\x00'
    return struct.pack('<i',len(b))+b


def _pw_entry(e, v):
    w=bytearray(e.content_hash)
    w+=struct.pack('<Q',e.offset)
    w+=struct.pack('<Q',e.uncompressed_size)
    w+=struct.pack('<I',e.compression_method)
    w+=struct.pack('<Q',e.size)
    if v>=5:
        w+=bytes([e.unk1])
        w+=e.unk2
    if e.compression_method!=CM_NONE and v>=3:
        w+=struct.pack('<I',len(e.compressed_blocks))
        for b in e.compressed_blocks:
            w+=struct.pack('<QQ',b.start,b.end)
    if v>=4:
        w+=struct.pack('<I',e.compression_block_size)
        w+=bytes([1 if e.encrypted else 0])
    if v>=12:
        w+=struct.pack('<II',e.encryption_method,e.index_new_sep)
    return bytes(w)


def _get_all_dirs_and_mp(pak):
    if pak._large_file:
        raw=pak._read_file_range(pak._pak_info.index_offset,pak._pak_info.index_size)
    else:
        raw=bytes(pak._file_content[pak._pak_info.index_offset:][:pak._pak_info.index_size])
    if pak._pak_info.index_encrypted:
        raw=PakCrypto.decrypt_index(raw,pak._pak_info)
    r=Reader(raw)
    mp=r.string()
    n=r.u4()
    for _ in range(n):
        TencentPakEntry(r,pak._pak_info.version)
    dirs={}
    for _ in range(r.u8()):
        dp=r.string()
        cnt=r.u8()
        dirs[dp]={r.string():pak._files[~r.i4()] for _ in range(cnt)}
    return mp,dirs


def _verify_repacked_files(out_path, edited, is_od=False):
    vp=TencentPakFile(out_path,is_od=is_od)
    indexed={}
    for dp, files in vp._index.items():
        for name, e in files.items():
            fp=str(PurePath(dp)/name).replace('\\','/')
            indexed[fp.lower()]=(fp,e)
    for fp,(src,_) in edited.items():
        m=indexed.get(fp.lower())
        if not m:
            raise ValueError(f"Verification: missing {fp}")
        _, e=m
        if e.encrypted and e.encryption_method==EM_UNKNOWN_17:
            continue
        exp=src.read_bytes()
        act=vp.extract_entry_to_bytes(e,PurePath(fp))
        if act is None:
            raise ValueError(f"Verification: extract failed {fp}")
        if act!=exp:
            raise ValueError(f"Verification: mismatch {fp} exp={len(exp)} got={len(act)}")


def _auto_backup(pak_path):
    src=Path(pak_path)
    bd=src.parent/"backup"
    bd.mkdir(parents=True,exist_ok=True)
    ts=datetime.now().strftime("%Y%m%d_%H%M%S")
    dst=bd/f"{src.stem}_{ts}{src.suffix}"
    shutil.copy2(src,dst)
    return dst


class SmartPakAnalysis:
    def __init__(self):
        self.file_name=""
        self.file_size=0
        self.version=0
        self.index_encrypted=False
        self.rsa_hash_ok=False
        self.sha1_hash_ok=False
        self.mount_point=""
        self.total_files=0
        self.total_dirs=0
        self.compression_stats=Counter()
        self.encryption_stats=Counter()
        self.combo_stats=Counter()
        self.most_common_combo=None
        self.by_name=defaultdict(list)
        self.by_ext=defaultdict(list)
        self.by_dir=defaultdict(list)
        self.ext_templates={}
        self.analysis_time_ms=0

    def cm_name(self,cm):
        return {CM_NONE:"NONE",CM_ZLIB:"ZLIB",CM_ZSTD:"ZSTD",CM_ZSTD_DICT:"ZSTD_DICT"}.get(cm,f"CM_{cm}")

    def em_name(self,em):
        if em==0:
            return "NONE"
        if em==EM_SIMPLE1:
            return "SIMPLE1"
        if em==EM_SIMPLE2:
            return "SIMPLE2"
        if em==EM_UNKNOWN_17:
            return "UNKNOWN_17"
        if em==EM_SM4_2:
            return "SM4_2"
        if em==EM_SM4_4:
            return "SM4_4"
        if em&EM_SM4_NEW_MASK:
            return f"SM4_{em}"
        return f"EM_{em}"


class SmartPakAnalyzer:
    def __init__(self, pak):
        self.pak=pak
        self.rep=SmartPakAnalysis()

    def analyze(self):
        t0=time.time()
        pak=self.pak
        rep=self.rep
        rep.file_name=pak._file_path.name
        rep.file_size=pak._file_size
        rep.version=pak._pak_info.version
        rep.index_encrypted=pak._pak_info.index_encrypted
        rep.mount_point=str(pak._mount_point)
        if not pak._is_od and pak._pak_info.version>=8:
            try:
                rh=PakCrypto.rsa_extract(pak._pak_info.packed_index_hash,RSA_MOD_2)
                rep.rsa_hash_ok=(rh==pak._pak_info.index_hash)
            except Exception:
                rep.rsa_hash_ok=False
        else:
            rep.rsa_hash_ok=True
        rep.sha1_hash_ok=True
        for dp, files in pak._index.items():
            ds=str(dp).replace("\\","/").strip("/")
            rep.total_dirs+=1
            for name, e in files.items():
                fp=str(PurePath(dp)/name).replace("\\","/")
                rep.total_files+=1
                cm=e.compression_method
                em=e.encryption_method if e.encrypted else 0
                rep.compression_stats[cm]+=1
                rep.encryption_stats[em]+=1
                rep.combo_stats[(cm,em)]+=1
                rep.by_name[name.lower()].append((fp,e))
                ext=Path(name).suffix.lower()
                if ext:
                    rep.by_ext[ext].append((fp,e))
                    if ext not in rep.ext_templates:
                        rep.ext_templates[ext]=e
                if ds:
                    rep.by_dir[ds].append((fp,e))
        if rep.combo_stats:
            rep.most_common_combo=rep.combo_stats.most_common(1)[0][0]
        rep.analysis_time_ms=(time.time()-t0)*1000
        return rep


class SmartTemplatePicker:
    def __init__(self, an, pidx):
        self.rep=an
        self.pak_index=pidx

    def pick(self, fname, target_dir, size_hint=0, existing=None):
        if existing is not None:
            return existing
        rep=self.rep
        nl=fname.lower()
        ext=Path(fname).suffix.lower()
        dn=target_dir.replace("\\","/").strip("/").lower()
        if nl in rep.by_name:
            c=rep.by_name[nl]
            sd=[x for x in c if Path(x[0]).parent.as_posix().lower().endswith(dn)]
            return sd[0][1] if sd else c[0][1]
        if ext and dn:
            for fp,e in rep.by_dir.get(dn,[]):
                if Path(fp).suffix.lower()==ext:
                    return e
        if ext and ext in rep.by_ext:
            c=rep.by_ext[ext]
            if size_hint>0:
                c=sorted(c,key=lambda x:abs(x[1].uncompressed_size-size_hint))
            return c[0][1]
        if rep.most_common_combo:
            cm,em=rep.most_common_combo
            for _, files in self.pak_index.items():
                for _, e in files.items():
                    ec=e.compression_method
                    ee=e.encryption_method if e.encrypted else 0
                    if (ec,ee)==(cm,em):
                        return e
        for _, files in self.pak_index.items():
            for _, e in files.items():
                return e
        return None

    def reason(self, t, fname, target_dir):
        if t is None:
            return S('no_template')
        nl=fname.lower()
        ext=Path(fname).suffix.lower()
        dn=target_dir.replace("\\","/").strip("/").lower()
        rep=self.rep
        if nl in rep.by_name:
            return S('same_name')
        if ext and dn:
            for fp,e in rep.by_dir.get(dn,[]):
                if e is t and Path(fp).suffix.lower()==ext:
                    return S('same_ext_dir')
        if ext and ext in rep.by_ext:
            for _,e in rep.by_ext[ext]:
                if e is t:
                    return f"{S('same_ext')} {ext}"
        if rep.most_common_combo:
            cm,em=rep.most_common_combo
            if (t.compression_method, t.encryption_method if t.encrypted else 0)==(cm,em):
                return S('most_common')
        return S('fallback')


class SmartDryRunReport:
    def __init__(self, an, picker, ef, tp):
        self.rep=an
        self.picker=picker
        self.edit_files=ef
        self.target_path=tp
        self.plan=[]

    def build_plan(self, all_dirs):
        tn=self.target_path.replace("\\","/").strip("/").lower()
        ex={}
        for dp, files in all_dirs.items():
            if dp.replace("\\","/").strip("/").lower()==tn:
                for n,e in files.items():
                    ex[n.lower()]=(n,e)
                break
        for p in self.edit_files:
            nl=p.name.lower()
            sh=p.stat().st_size
            existing=None
            action="add"
            extra=""
            if nl in ex:
                _,existing=ex[nl]
                action="replace"
                extra=S('replace_existing')
            t=self.picker.pick(p.name,self.target_path,sh,existing)
            r=self.picker.reason(t,p.name,self.target_path)
            if extra:
                r=extra+" - "+r
            self.plan.append((p,action,t,r,existing))
        return self.plan

    def print_report(self):
        rep=self.rep
        console.print()
        console.print(Panel(f"[bold {C_GOLD}]{S('analysis_report')}[/bold {C_GOLD}]",
                            border_style=C_FROST, box=DOUBLE_EDGE,
                            title=f" {S('analyzer')} ", title_align="center"))
        t=Table(box=ROUNDED, border_style=C_TEAL, show_header=False)
        t.add_column("K", style=f"bold {C_CYAN}")
        t.add_column("V", style=f"bold #ECEFF4")
        t.add_row(f"{S('file_label')}", rep.file_name)
        t.add_row(f"{S('size_label')}", human_size(rep.file_size))
        t.add_row(f"{S('version_label')}", str(rep.version))
        t.add_row(f"{S('index_enc')}", S('yes')+" (AES-256-CBC)" if rep.index_encrypted else S('no'))
        t.add_row(f"{S('rsa_hash')}", f"{S('valid')}" if rep.rsa_hash_ok else f"{S('mismatch')}")
        t.add_row(f"{S('mount')}", rep.mount_point or S('empty'))
        t.add_row(f"{S('total_files')}", f"{rep.total_files:,}")
        t.add_row(f"{S('total_dirs')}", f"{rep.total_dirs:,}")
        console.print(t)
        console.print()
        ct=Table(title=f"[bold {C_PURPLE}]{S('compression_methods')}[/bold {C_PURPLE}]",
                 box=MINIMAL_DOUBLE_HEAD, border_style=C_PURPLE)
        ct.add_column(S('method'),style=f"bold {C_CYAN}")
        ct.add_column(S('count'),justify="right",style=f"bold {C_GREEN}")
        ct.add_column("%",justify="right",style=f"bold {C_GOLD}")
        for cm,c in rep.compression_stats.most_common():
            p=c/rep.total_files*100 if rep.total_files else 0
            ct.add_row(rep.cm_name(cm),f"{c:,}",f"{p:.1f}%")
        console.print(ct)
        console.print()
        et=Table(title=f"[bold {C_ORANGE}]{S('encryption_methods')}[/bold {C_ORANGE}]",
                 box=MINIMAL_DOUBLE_HEAD, border_style=C_ORANGE)
        et.add_column(S('method'),style=f"bold {C_CYAN}")
        et.add_column(S('count'),justify="right",style=f"bold {C_GREEN}")
        et.add_column("%",justify="right",style=f"bold {C_GOLD}")
        for em,c in rep.encryption_stats.most_common():
            p=c/rep.total_files*100 if rep.total_files else 0
            et.add_row(rep.em_name(em),f"{c:,}",f"{p:.1f}%")
        console.print(et)
        if rep.most_common_combo:
            cm,em=rep.most_common_combo
            console.print()
            console.print(f"[bold {C_GREEN}]{S('most_combo')}:[/bold {C_GREEN}] "
                          f"[bold {C_CYAN}]{rep.cm_name(cm)}[/bold {C_CYAN}] + "
                          f"[bold {C_ORANGE}]{rep.em_name(em)}[/bold {C_ORANGE}]")
        console.print()

    def print_plan(self):
        console.print()
        console.print(Panel(f"[bold {C_GOLD}]{S('repack_plan')} - {S('target')}: {self.target_path}[/bold {C_GOLD}]",
                            border_style=C_GOLD, box=ROUNDED, title=f" {S('dry_run')} ", title_align="center"))
        pt=Table(box=ROUNDED, border_style=C_TEAL)
        pt.add_column("#",justify="center",style=f"bold {C_GOLD}",width=3)
        pt.add_column(S('file_label'),style=f"bold {C_GREEN}")
        pt.add_column(S('action'),justify="center")
        pt.add_column(S('size_label'),justify="right",style=f"bold {C_CYAN}")
        pt.add_column(S('template'),style=f"dim #ECEFF4")
        for i,(p,act,t,r,ex) in enumerate(self.plan,1):
            a=f"[bold {C_ORANGE}]REPLACE[/bold {C_ORANGE}]" if act=="replace" else f"[bold {C_GREEN}]ADD[/bold {C_GREEN}]"
            ti=""
            if t:
                ti=f"{self.rep.cm_name(t.compression_method)} / {self.rep.em_name(t.encryption_method if t.encrypted else 0)}"
            pt.add_row(str(i),p.name,a,human_size(p.stat().st_size),ti)
        console.print(pt)
        console.print()
        console.print(f"[bold {C_PURPLE}]{S('smart_reason')}:[/bold {C_PURPLE}]")
        for i,(p,act,t,r,ex) in enumerate(self.plan,1):
            console.print(f"  [{i}] [bold {C_CYAN}]{p.name}[/bold {C_CYAN}] -> {r}")
        console.print()


def repack_pak_file_full(pak_file, edited_root, output_path,
                  target_path=None, force_add=False,
                  do_dry_run=True, do_backup=True):
    import copy as _cp
    edit_files=[p for p in Path(edited_root).rglob('*') if p.is_file()]
    if not edit_files:
        console.print(f'[bold {C_RED}]{S("no_files")}[/bold {C_RED}]')
        return 0
    console.print(f'[bold {C_CYAN}]{S("found_files")}: {len(edit_files)}[/bold {C_CYAN}]')

    if pak_file._large_file:
        console.print(f'[bold {C_GOLD}]{S("large_pak")}[/bold {C_GOLD}]')
        with open(pak_file._file_path,'rb') as f:
            pak_file._file_content=memoryview(f.read())
        pak_file._large_file=False

    version=pak_file._pak_info.version
    ks=PakCrypto.zuc_keystream()
    orig_fc=pak_file._file_content
    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)

    if target_path and force_add:
        target_path=target_path.replace('\\','/').strip('/')
        matched=None
        for ed in all_dirs.keys():
            if ed.replace('\\','/').strip('/').lower()==target_path.lower():
                matched=ed
                break
        target_path=matched if matched else (target_path+'/')

    console.print(f'[bold {C_CYAN}]{S("analyzing")}...[/bold {C_CYAN}]')
    analyzer=SmartPakAnalyzer(pak_file)
    analysis=analyzer.analyze()
    console.print(f'  [dim]{S("analysis_done")} {analysis.analysis_time_ms:.0f}ms - {analysis.total_files:,} {S("files")}[/dim]')

    picker=SmartTemplatePicker(analysis,pak_file._index)
    dry=SmartDryRunReport(analysis,picker,edit_files,target_path or ".")
    dry.build_plan(all_dirs)

    if do_dry_run:
        dry.print_report()
        dry.print_plan()
        console.print(f"[bold {C_GOLD}]{S('proceed')}[/bold {C_GOLD}]")
        try:
            ans=input("  > ").strip().lower()
        except Exception:
            ans='y'
        if ans not in ('y','yes','نعم','اه','آه','ايوة','ايوه'):
            console.print(f'[bold {C_RED}]{S("cancelled")}[/bold {C_RED}]')
            return 0

    if do_backup:
        try:
            bp=_auto_backup(pak_file._file_path)
            console.print(f'[bold {C_GREEN}]{S("backup")}:[/bold {C_GREEN}] {bp}')
        except Exception as e:
            console.print(f'[bold {C_ORANGE}]{S("backup_failed")}:[/bold {C_ORANGE}] {e}')

    edited={}
    for p,act,t,reason,ex in dry.plan:
        fp=f"{target_path.rstrip('/')}/{p.name}"
        edited[fp]=(p,t,ex)

    if not edited:
        console.print(f'[bold {C_RED}]{S("no_files_repack")}[/bold {C_RED}]')
        return 0

    console.print(f'  [bold {C_CYAN}]{S("files_to_repack")}: {len(edited)}[/bold {C_CYAN}]')

    new_files=[]
    for e in pak_file._files:
        ne=_cp.copy(e)
        ne.compressed_blocks=[_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new={id(pak_file._files[i]):new_files[i] for i in range(len(pak_file._files))}
    edited_paths={fp:(p,t,ex) for fp,(p,t,ex) in edited.items()}

    out_buf=bytearray()

    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            fp=str(PurePath(dp_str)/name).replace('\\','/')
            ne=old_to_new.get(id(old_entry))
            if ne is None:
                ne=_cp.copy(old_entry)
                ne.compressed_blocks=[_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)]=ne
            em=old_entry.encryption_method
            cm=old_entry.compression_method

            if fp in edited_paths:
                p,t,_=edited_paths[fp]
                nr=p.read_bytes()
                pak_rel=PurePath(fp)
                ne.content_hash=SHA1.new(nr).digest()
                ne.uncompressed_size=len(nr)
                ne.compression_method=t.compression_method if t else cm
                ne.encryption_method=t.encryption_method if t else em
                ne.encrypted=t.encrypted if t else old_entry.encrypted
                ne.unk1=t.unk1 if t else old_entry.unk1
                ne.unk2=t.unk2 if t else old_entry.unk2
                ne.index_new_sep=t.index_new_sep if t else old_entry.index_new_sep

                if ne.compression_method==CM_NONE:
                    cipher=(_encrypt_plaintext(nr,pak_rel,ne.encryption_method) if ne.encrypted else nr)
                    ne.offset=len(out_buf)
                    ne.size=len(cipher)
                    ne.uncompressed_size=len(nr)
                    out_buf+=cipher
                else:
                    cs=(t.compression_block_size if t and t.compression_block_size>0
                        else old_entry.compression_block_size if old_entry.compression_block_size>0
                        else 65536)
                    chunks=[nr[i:i+cs] for i in range(0,len(nr),cs)]
                    bo=PakCrypto.generate_block_indices(len(chunks),ne.encryption_method)
                    nb=[None]*len(chunks)
                    for li,ch in enumerate(chunks):
                        comp=_best_compress(ch,ne.compression_method,pak_file._zstd_dict)
                        cipher=(_encrypt_plaintext(comp,pak_rel,ne.encryption_method) if ne.encrypted else comp)
                        blk=PakCompressedBlock.__new__(PakCompressedBlock)
                        blk.start=len(out_buf)
                        blk.end=blk.start+len(cipher)
                        out_buf+=cipher
                        nb[bo[li]]=blk
                    ne.compressed_blocks=nb
                    ne.offset=min((b.start for b in nb),default=len(out_buf))
                    ne.size=sum(b.end-b.start for b in nb)
                    ne.uncompressed_size=len(nr)
                console.print(f'[{C_GREEN}]{S("processed")}: {fp}[/{C_GREEN}]')
            else:
                if cm==CM_NONE:
                    rs=(PakCrypto.align_encrypted_content_size(old_entry.size,em)
                        if old_entry.encrypted else old_entry.size)
                    ne.offset=len(out_buf)
                    out_buf+=bytes(orig_fc[old_entry.offset:old_entry.offset+rs])
                elif old_entry.compressed_blocks:
                    nb=[]
                    for ob in old_entry.compressed_blocks:
                        unc=ob.end-ob.start
                        enc=(PakCrypto.align_encrypted_content_size(unc,em)
                             if old_entry.encrypted else unc)
                        b=PakCompressedBlock.__new__(PakCompressedBlock)
                        b.start=len(out_buf)
                        b.end=b.start+unc
                        out_buf+=bytes(orig_fc[ob.start:ob.start+enc])
                        nb.append(b)
                    ne.compressed_blocks=nb
                    ne.offset=nb[0].start

    if target_path and force_add:
        for fp,(p,t,ex) in edited.items():
            proc=False
            for dp_str, dir_files in all_dirs.items():
                for name, entry in dir_files.items():
                    if str(PurePath(dp_str)/name).replace('\\','/')==fp:
                        proc=True
                        break
                if proc:
                    break
            if proc:
                continue

            ne=_cp.copy(t)
            nr=p.read_bytes()
            pak_rel=PurePath(fp)
            ne.content_hash=SHA1.new(nr).digest()
            ne.uncompressed_size=len(nr)
            ne.compression_method=t.compression_method
            ne.encryption_method=t.encryption_method
            ne.encrypted=t.encrypted
            ne.unk1=t.unk1
            fstr=mp_str+fp
            ne.unk2=SHA1.new(fstr.lower().encode('utf-8')).digest()
            ne.index_new_sep=t.index_new_sep

            if ne.compression_method==CM_NONE:
                cipher=(_encrypt_plaintext(nr,pak_rel,ne.encryption_method) if ne.encrypted else nr)
                ne.offset=len(out_buf)
                ne.size=len(cipher)
                ne.uncompressed_size=len(nr)
                out_buf+=cipher
            else:
                cs=t.compression_block_size if t.compression_block_size>0 else 65536
                chunks=[nr[i:i+cs] for i in range(0,len(nr),cs)]
                bo=PakCrypto.generate_block_indices(len(chunks),ne.encryption_method)
                nb=[None]*len(chunks)
                for li,ch in enumerate(chunks):
                    comp=_best_compress(ch,ne.compression_method,pak_file._zstd_dict)
                    cipher=(_encrypt_plaintext(comp,pak_rel,ne.encryption_method) if ne.encrypted else comp)
                    blk=PakCompressedBlock.__new__(PakCompressedBlock)
                    blk.start=len(out_buf)
                    blk.end=blk.start+len(cipher)
                    out_buf+=cipher
                    nb[bo[li]]=blk
                ne.compressed_blocks=nb
                ne.offset=min((b.start for b in nb),default=len(out_buf))
                ne.size=sum(b.end-b.start for b in nb)
                ne.uncompressed_size=len(nr)

            new_files.append(ne)
            if target_path not in all_dirs:
                all_dirs[target_path]={}
            on=next((n for n in all_dirs[target_path] if n.lower()==p.name.lower()),None)
            if on is not None:
                del all_dirs[target_path][on]
            all_dirs[target_path][p.name]=ne
            console.print(f'[{C_GREEN}]{S("added_new")}: {fp}[/{C_GREEN}]')

    eidx={id(new_files[i]):i for i in range(len(new_files))}
    idx=bytearray(_pw_string(mp_str))
    idx+=struct.pack('<I',len(new_files))
    for ne in new_files:
        idx+=_pw_entry(ne,version)
    idx+=struct.pack('<Q',len(all_dirs))
    for dp_str, dir_files in all_dirs.items():
        idx+=_pw_string(dp_str)
        idx+=struct.pack('<Q',len(dir_files))
        for name, old_e in dir_files.items():
            idx+=_pw_string(name)
            fi=eidx.get(id(old_e))
            if fi is None:
                m=old_to_new.get(id(old_e))
                if m is not None:
                    fi=eidx.get(id(m))
            if fi is None:
                for i,e in enumerate(new_files):
                    if e.offset==old_e.offset and e.size==old_e.size:
                        fi=i
                        break
            idx+=struct.pack('<i',~fi if fi is not None else 0)

    index_plain=bytes(idx)
    new_sha1=SHA1.new(index_plain).digest()

    if pak_file._pak_info.index_encrypted:
        key=PakCrypto.rsa_extract(pak_file._pak_info.packed_key,RSA_MOD_1)
        iv=PakCrypto.rsa_extract(pak_file._pak_info.packed_iv,RSA_MOD_1)
        aes=AES.new(key,MODE_CBC,iv[:16])
        pad=(-len(index_plain))%AES.block_size or AES.block_size
        index_bytes=aes.encrypt(index_plain+bytes([pad]*pad))
    else:
        index_bytes=index_plain

    new_idx_offset=len(out_buf)
    new_idx_size=len(index_bytes)
    out_buf+=index_bytes

    fsz=TencentPakInfo._mem_size(version)
    nf=bytearray(orig_fc[-fsz:])
    hk=struct.pack('<5I',*ks[4:9])
    nf[-36:-16]=bytes(a^b for a,b in zip(new_sha1,hk))
    nf[-16:-8]=((new_idx_size^(ks[10]<<32|ks[11])).to_bytes(8,'little'))
    nf[-8:]   =((new_idx_offset^(ks[0]<<32|ks[1])).to_bytes(8,'little'))
    out_buf+=nf

    with open(output_path,'wb') as f:
        f.write(out_buf)

    if force_add:
        console.print(f'[bold {C_CYAN}]{S("verifying")}...[/bold {C_CYAN}]')
        ev={fp:(p,t) for fp,(p,t,_) in edited.items()}
        _verify_repacked_files(output_path,ev,is_od=getattr(pak_file,'_is_od',False))
        console.print(f'[bold {C_GREEN}]{S("verified")}[/bold {C_GREEN}]')

    return len(edited)


def _ui_width():
    return max(16,min(92,console.width-2))


def _print_output(message, title=None, border_style=C_CYAN):
    if title is None:
        title = S('output')
    fw=_ui_width()
    left=" "*max(0,(console.width-fw)//2)
    cw=max(8,fw)
    st=Text()
    st.append(f"{title.strip()}: ",style=f"bold {border_style}")
    try:
        body=Text.from_markup(message)
    except Exception:
        body=Text(message)
    st.append_text(body)
    for line in st.wrap(console,width=cw):
        console.print(Text(left)+line)


def safe_input(prompt=""):
    label=" ".join(prompt.replace('\n',' ').split()).strip() or S('your_choice')
    fw=_ui_width()
    ind=max(0,(console.width-fw)//2)
    left=" "*ind
    pw=max(8,fw-4)
    if len(label)>pw:
        label=label[:pw-1]+"..."
    console.print(Text(left)+Text.from_markup(f"[bold {C_GOLD}]{label}[/bold {C_GOLD}] ")
                  +Text.from_markup(f"[bold {C_CYAN}]>[/bold {C_CYAN}] "),end="")
    console.file.flush()
    try:
        return input()
    except (EOFError,RuntimeError):
        try:
            if sys.platform!='win32':
                with open('/dev/tty','r') as t:
                    return t.readline().rstrip('\n')
            else:
                with open('CON','r') as c:
                    return c.readline().rstrip('\r\n')
        except Exception:
            return ''
    except Exception:
        return ''
    finally:
        console.print()


_CUSTOM_BANNER = [
    "⠀⡀⠤⡀⠄⠀⠀⠀⢀⠀⠆⢠⣀⠀⠀⢀⣅⠤⠀⠀⠀⠀⠀⢀⠠⢄⠠⠀",
    "⠀⡄⠐⡄⠂⠀⠀⢠⢡⡌⢣⣿⣿⣿⣾⣿⣿⡗⡄⢡⠀⡄⠀⢡⠀⢣⠈⠀",
    "⠈⣄⢙⡌⢃⠉⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢀⢡⡘⣇⠙⡈",
    "⠈⠆⣉⠄⡁⠀⣈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⠀⠱⢈⡧⢈⠀",
    "⠀⡁⠤⡀⠄⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣿⣿⣿⣿⡿⢊⠀⢆⠠⠀",
    "⠰⡀⠰⡀⠆⠀⣿⣿⣿⣿⡿⠹⣿⣿⡿⠁⢀⣾⣿⣿⣿⣿⡀⢆⠀⢇⠰⠀",
    "⠄⠄⣙⠄⠣⣾⣿⣿⣿⣿⣧⣄⠈⠋⢀⣴⣿⣿⣿⣿⣿⣿⣧⡡⢈⡣⠈⠄",
    "⢈⠦⣩⠄⡡⠈⢍⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⡿⠏⠡⡱⢌⡧⢈⠄",
    "⠀⡁⠤⡀⠄⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⢈⠀⢇⠠⠀",
    "⠀⡀⠤⠀⠄⠀⠀⠀⢃⠘⡻⣿⣿⣿⣿⣿⣿⠿⠀⠃⠀⠀⠀⢀⠠⢄⠠⠀",
    "⢀⠄⣐⢄⡂⡀⢀⠀⡠⢐⡢⣙⢋⠀⡀⢙⠏⣐⢄⡀⡀⢀⠀⡢⢐⠢⣐⢀",
]


def _fit_center(v,w):
    if w<=1:
        return v[:1]
    if len(v)>w:
        v=v[:w-1]+"..."
    return v.center(w)


def _menu_panel(panel_width=None):
    panel_width=panel_width or max(14,_ui_width()-4)
    items=[("1",S('m4'),C_PURPLE),
           ("2",S('m0'),C_RED)]
    lines=[]
    for num,label,color in items:
        lines.append(Text.from_markup(f"[bold {C_GOLD}][ {num} ][/bold {C_GOLD}] "
                                       f"[bold {color}]{label}[/bold {color}]"))
    return Panel(Group(*lines),title=f" {S('menu_title')} ",
                 title_align="center",border_style=C_FROST,box=ROUNDED,
                 padding=(1,max(0,min(2,(panel_width-10)//2))),width=panel_width)


def print_banner():
    os.system('cls' if os.name=='nt' else 'clear')
    fw=_ui_width()
    ipw=max(10,fw-6)
    cw=max(6,ipw-4)
    hl=[]
    for line in _CUSTOM_BANNER:
        if len(line)>cw:
            line=line[:cw]
        hl.append(Text(line.center(cw),style=f"bold {C_PURPLE}"))
    hl.append(Text(""))
    hl.append(Text(_fit_center(S('subtitle'),cw),style=f"bold {C_GOLD}"))
    hl.append(Text(_fit_center(f"{S('title')}",cw),style=f"bold {C_PURPLE}"))
    hp=Panel(Group(*hl),title=f" {S('header')} ",title_align="center",
             border_style=C_FROST,box=DOUBLE_EDGE,padding=(1,1),width=ipw)
    ol=Group(Text.from_markup(f"[bold {C_GREEN}]{S('owner')} :[/bold {C_GREEN}] SAAD - INJ"),
             Text.from_markup(f"[bold {C_CYAN}]{S('telegram')} :[/bold {C_CYAN}] @r1_ub"),
             Text.from_markup(f"[bold {C_GOLD}]{S('contact')} :[/bold {C_GOLD}] +967780379327"))
    op=Panel(ol,title=f" {S('owner')} ",title_align="center",
             border_style=C_TEAL,box=ROUNDED,padding=(0,1),width=ipw)
    console.print(Align.center(Panel(Group(hp,op,_menu_panel(ipw)),
                    title=f" {S('menu_border')} ",title_align="center",
                    border_style=C_FROST,box=DOUBLE_EDGE,padding=(1,1),width=fw)))
    console.print()


def ensure_directories():
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    LUA_DIR.mkdir(parents=True, exist_ok=True)
    DONE_DIR.mkdir(parents=True, exist_ok=True)


def display_file_selector(title, folder, pattern="*.pak"):
    files=sorted(list(folder.glob(pattern)))
    if not files:
        _print_output(f"[bold {C_RED}]{S('no_pak')} {folder}[/]",
                      f" {S('error')} ",C_RED)
        return None,None
    t=Table(title=f"[bold {C_CYAN}]{title}[/]",box=ROUNDED,border_style=C_TEAL)
    t.add_column("[bold #]",justify="center",style=f"bold {C_GOLD}",width=4)
    t.add_column(S('file_label'),style=f"bold {C_GREEN}")
    t.add_column(S('size_label'),justify="right",style=f"bold {C_PURPLE}")
    for i,f in enumerate(files,1):
        t.add_row(str(i),f.name,human_size(f.stat().st_size))
    console.print(t)
    try:
        i=int(safe_input(f"{S('select_file')} (1-{len(files)})"))-1
        if i<0 or i>=len(files):
            _print_output(f"[bold red]{S('invalid_sel')}[/]",
                          f" {S('error')} ",C_RED)
            return None,None
        return files[i],files
    except ValueError:
        _print_output(f"[bold red]{S('valid_number')}[/]",
                      f" {S('error')} ",C_RED)
        return None,None


def _open_pak(fp):
    try:
        return TencentPakFile(fp)
    except Exception as e1:
        try:
            console.print(f"  [dim {C_GOLD}]{S('std_open_fail')}...[/dim {C_GOLD}]")
            return TencentPakFile(fp,is_od=True)
        except Exception as e2:
            raise RuntimeError(f"{S('cannot_open')}.\n  1: {e1}\n  2: {e2}") from e2


def run_smart_option4():
    if not INPUT_DIR.exists():
        _print_output(f"[bold {C_RED}]{S('pak_not_found')}[/]",
                      f" {S('error')} ",C_RED)
        return
    pak_file,_=display_file_selector(S('select_pak'),INPUT_DIR)
    if not pak_file:
        return
    if not LUA_DIR.exists() or not any(LUA_DIR.iterdir()):
        _print_output(f'[bold {C_RED}]{S("no_files")}[/bold {C_RED}]',
                      f" {S('error')} ",C_RED)
        return

    _print_output(f'[bold {C_GOLD}]{S("target_path")}:[/bold {C_GOLD}]\n'
                  f'[dim]{S("default_path")}: {ADD_TO_PATH_TARGET}[/dim]',
                  f" {S('target_path')} ",C_GOLD)
    tp_in=safe_input(f"  {S('path_prompt')} > ").strip() or ADD_TO_PATH_TARGET
    if not tp_in:
        _print_output(f'[bold {C_RED}]{S("path_required")}[/bold {C_RED}]',
                      f" {S('error')} ",C_RED)
        return
    tp_in=tp_in.replace('\\','/').strip('/')
    if not tp_in:
        _print_output(f'[bold {C_RED}]{S("invalid_path")}[/bold {C_RED}]',
                      f" {S('error')} ",C_RED)
        return

    n=sum(1 for _ in LUA_DIR.rglob('*') if _.is_file())
    _print_output(f'[bold {C_CYAN}]{S("smart_repack")} {pak_file.name}...[/bold {C_CYAN}]\n'
                  f'[dim]{S("files")}: {n}[/dim]\n[dim]{S("target")}: {tp_in}[/dim]',
                  f" {S('processing')} ",C_CYAN)
    try:
        pak=_open_pak(pak_file)
        out=DONE_DIR/pak_file.name
        c=repack_pak_file_full(pak,LUA_DIR,out,target_path=tp_in,
                                force_add=True,do_dry_run=True,do_backup=True)
        if c>0:
            _print_output(f'[bold {C_GREEN}]{S("successfully")} {c} {S("file_s")}![/bold {C_GREEN}]\n'
                          f'[bold {C_GREEN}]{S("output")}: {out}[/bold {C_GREEN}]\n'
                          f'[bold {C_GREEN}]{S("verified")}[/bold {C_GREEN}]\n'
                          f'[bold {C_GREEN}]{S("game_ready")}[/bold {C_GREEN}]',
                          f" {S('success')} ",C_GREEN)
        else:
            _print_output(f'[bold {C_RED}]{S("no_processed")}[/bold {C_RED}]',
                          f" {S('error')} ",C_RED)
    except Exception as e:
        err=str(e).replace('[','\\[').replace(']','\\]')
        _print_output(f'[bold {C_RED}]{S("repack_failed")}:[/bold {C_RED}] {err}',
                      f" {S('error')} ",C_RED)
        import traceback
        traceback.print_exc()


def pick_language():
    global LANG
    os.system('cls' if os.name=='nt' else 'clear')
    fw=_ui_width()
    ipw=max(10,fw-6)
    console.print()
    console.print(Align.center(Panel(
        Group(
            Text(_fit_center("Choose language / اختر اللغة",ipw-6),style=f"bold {C_GOLD}"),
            Text(""),
            Text(_fit_center("1  >  English",ipw-6),style=f"bold {C_GREEN}"),
            Text(_fit_center("2  >  العربية",ipw-6),style=f"bold {C_CYAN}"),
        ),
        title=" LANGUAGE / اللغة ", title_align="center",
        border_style=C_FROST, box=DOUBLE_EDGE, padding=(1,2), width=ipw,
    )))
    console.print()
    while True:
        c=safe_input("1 / 2")
        if c=="1":
            LANG="en"
            return
        if c=="2":
            LANG="ar"
            return


def main_menu():
    ensure_directories()
    while True:
        print_banner()
        ch=safe_input(S('your_choice')+" >").strip()
        console.print()
        if ch=='1':
            run_smart_option4()
            safe_input(f'\n{S("press_enter")}')
        elif ch=='2':
            _print_output(f"[bold {C_PURPLE}]{S('exit_msg')}[/bold {C_PURPLE}]\n"
                          f"[bold {C_FROST}]{S('goodbye')}[/bold {C_FROST}]",
                          f" {S('m0')} ",C_PURPLE)
            time.sleep(1)
            break
        else:
            _print_output(f'[bold {C_RED}]{S("invalid")}[/bold {C_RED}]',
                          f" {S('error')} ",C_RED)
            time.sleep(1)


if __name__=='__main__':
    try:
        pick_language()
        main_menu()
    except KeyboardInterrupt:
        console.print(f'\n[bold {C_GOLD}]{S("interrupted")}[/bold {C_GOLD}]')
        sys.exit(0)
    except Exception as e:
        err=str(e).replace('[','\\[').replace(']','\\]')
        console.print(f'[bold {C_RED}]{S("error_label")}:[/bold {C_RED}] {err}')
        import traceback
        traceback.print_exc()
        safe_input(f'\n{S("press_enter")}')
        sys.exit(1)
        
        #S A. A D