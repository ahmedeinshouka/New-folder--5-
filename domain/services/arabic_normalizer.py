"""
Domain Service: Arabic Normalizer

This service normalizes Arabic text by standardizing letter forms and
removing diacritical marks to create canonical representations.
"""

import re
from typing import Dict
from domain.rules import ARABIC_NORMALIZATION_MAP, ARABIC_DIACRITICS_PATTERN


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
        self._normalization_map = normalization_map or ARABIC_NORMALIZATION_MAP
        
        # Default diacritics pattern if not provided
        self._diacritics_pattern = diacritics_pattern or ARABIC_DIACRITICS_PATTERN
    
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
