"""
Domain Rules: Name Processing Constants and Patterns

This module contains the core business rules for name processing,
including normalization constants, null-like values, and regex patterns.
These rules are part of the domain layer as they define what constitutes
valid data and how it should be processed.
"""

import re
from typing import Set, Dict, List, Tuple

# =====================================================================
# TITLES - Words indicating honorifics or professional titles
# =====================================================================

TITLES: Set[str] = {
    # English titles
    "mr", "mr.", "mrs", "mrs.", "ms", "ms.", "miss", "mister",
    "dr", "dr.", "doctor", "prof", "prof.", "professor",
    "eng", "eng.", "engineer", "sir", "lady", "lord",
    
    # Arabic titles
    "باشا", "بيه", "بك", "افندي",
    "دكتور", "د", "د.", "دكتوره", "الدكتور",
    "مهندس", "م", "م.", "المهندس",
    "أستاذ", "استاذ", "أ", "أ.",
    "شيخ", "الشيخ",
    "سيد", "سيدة", "السيد", "السيدة",
    "حاج", "الحاج",
}

# =====================================================================
# NOISE WORDS - Common words that add no identifying value
# =====================================================================

NOISE_WORDS: Set[str] = {
    # English organizational terms
    "co", "co.", "company", "corp", "corporation", "group",
    "sons", "and", "the", "of", "ltd", "limited", "plc", "llc", "inc",
    
    # Arabic connectors and organizational terms
    "بن", "ابن", "ابو", "أبو", "آل", "ال", "و", "من",
    "شركة", "مجموعة", "مجموعه", "واولاده", "مؤسسة",
}

# =====================================================================
# NULL-LIKE VALUES - Strings that represent missing/null data
# =====================================================================

NULL_LIKE_VALUES: Set[str] = {
    "null", "none", "n/a", "na", "nil", "undefined", "unknown",
    "--", "-",
    "غير معروف", "لا يوجد"
}

# =====================================================================
# REGEX PATTERNS - Compiled patterns for efficient text processing
# =====================================================================

# Pattern to match and remove special characters and punctuation
REMOVE_CHARS_PATTERN = re.compile(
    r"[~`!@#$%^&*()+=\[\]{}\\|:;\"'<>,?،؛؟«»\._\-/]"
)

# Pattern to match invisible/zero-width characters
INVISIBLE_CHARS_PATTERN = re.compile(
    r'[\u200b-\u200f\ufeff\u00a0]'
)

# Pattern to match HTML tags
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")

# Pattern to match multiple whitespace characters
WHITESPACE_PATTERN = re.compile(r'\s+')

# =====================================================================
# ARABIC NORMALIZATION
# =====================================================================

# Map Arabic letter variants to their canonical forms
ARABIC_NORMALIZATION_MAP: Dict[str, str] = {
    # Alef variants
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ٲ": "ا", "ٳ": "ا",
    
    # Ya variants
    "ى": "ي", "ئ": "ي", "ۍ": "ي", "ێ": "ي",
    
    # Waw variants
    "ؤ": "و", "ۆ": "و",
    
    # Ha/Ta marbuta variants
    "ة": "ه", "ۃ": "ه", "ھ": "ه",
}

# Pattern to match Arabic diacritical marks
ARABIC_DIACRITICS_PATTERN = re.compile(
    r"[\u064B-\u065F\u0670\u06D6-\u06ED\u08D4-\u08E1\u08D3-\u08FF\uFE70-\uFEFF]"
)

# =====================================================================
# COMPOUND NAMES
# =====================================================================

# List of compound name patterns: (first_part, second_part, combined_form)
COMPOUND_NAMES: List[Tuple[str, str, str]] = [
    # English/transliterated compound names
    ("abdel", "rahman", "abdelrahman"),
    ("abdul", "rahman", "abdulrahman"),
    ("abdel", "aziz", "abdelaziz"),
    ("abdul", "aziz", "abdulaziz"),
    
    # Arabic compound names
    ("عبد", "الرحمن", "عبدالرحمن"),
    ("عبد", "العزيز", "عبدالعزيز"),
    ("عبد", "الله", "عبدالله"),
    ("صلاح", "الدين", "صلاحالدين"),
    ("ابو", "بكر", "ابوبكر"),
]
