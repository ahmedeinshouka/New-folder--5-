"""
Infrastructure Configuration: Constants

This module contains all configuration constants used throughout the preprocessing pipeline.
These constants are infrastructure concerns as they represent external knowledge and rules.
"""

import re
from typing import Set

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
