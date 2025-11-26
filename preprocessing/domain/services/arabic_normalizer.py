"""
Domain Service: Arabic Normalizer

This service normalizes Arabic text by standardizing letter forms and
removing diacritical marks to create canonical representations.
"""

import re
from typing import Dict


class ArabicNormalizer:
    """
    Normalizes Arabic text by mapping variant letter forms to standard forms
    and removing diacritical marks.
    
    This helps match Arabic names that may have different letter forms or
    diacritics but represent the same name.
    """
    
    def __init__(self, 
                 normalization_map: Dict[str, str] = None,
                 diacritics_pattern: re.Pattern = None):
        """
        Initialize the Arabic normalizer.
        
        Args:
            normalization_map: Dictionary mapping variant forms to standard forms
            diacritics_pattern: Regex pattern for matching diacritical marks
        """
        # Default normalization map if not provided
        self._normalization_map = normalization_map or {
            "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ٲ": "ا", "ٳ": "ا",
            "ى": "ي", "ئ": "ي", "ۍ": "ي", "ێ": "ي",
            "ؤ": "و", "ۆ": "و",
            "ة": "ه", "ۃ": "ه", "ھ": "ه",
        }
        
        # Default diacritics pattern if not provided
        self._diacritics_pattern = diacritics_pattern or re.compile(
            r"[\u064B-\u065F\u0670\u06D6-\u06ED\u08D4-\u08E1\u08D3-\u08FF\uFE70-\uFEFF]"
        )
    
    def normalize(self, text: str) -> str:
        """
        Normalize Arabic text by standardizing letters and removing diacritics.
        
        This method implements the Normalizer protocol interface.
        
        Args:
            text: The Arabic text to normalize
            
        Returns:
            The normalized Arabic text
        """
        # Apply character-level normalization
        for old_char, new_char in self._normalization_map.items():
            text = text.replace(old_char, new_char)
        
        # Remove diacritical marks
        text = re.sub(self._diacritics_pattern, "", text)
        
        return text
