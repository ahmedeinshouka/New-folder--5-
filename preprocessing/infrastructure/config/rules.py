"""
Infrastructure Configuration: Rules

This module contains normalization rules and mappings used in the preprocessing pipeline.
These are infrastructure concerns as they represent domain knowledge encoded as data.
"""

import re
from typing import Dict, List, Tuple

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
