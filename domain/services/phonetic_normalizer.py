"""
Domain Service: Phonetic Normalizer

This service normalizes English/transliterated name tokens into a canonical form
using phonetic and character-based rules. It handles common variations in spelling
that represent the same phonetic sound.
"""

import re


class PhoneticNormalizer:
    """
    Normalizes English/transliterated name tokens into a canonical form
    using a series of phonetic and character-based rules.
    
    This normalizer helps match names that sound the same but are spelled
    differently (e.g., "Mohammed" and "Muhammad").
    """
    
    def __init__(self):
        """Initialize the phonetic normalizer with default rules."""
        # Rules are applied in order. More specific rules should come first.
        self._PHONETIC_RULES = [
            # 1. Digraphs and common transliterations (most specific)
            (r'kh', 'h'),      # Khaled -> Haled
            (r'gh', 'g'),      # Ghada -> Gada
            (r'sh', 's'),      # Shadi -> Sadi
            (r'th', 't'),      # Thamer -> Tamer
            (r'ph', 'f'),      # Philip -> Filip
            (r'ch', 's'),      # Charbel -> Sarbel (can also be 'k', but 's' is common in names)
            (r'ou', 'u'),      # Mahmoud -> Mahmud
            (r'ei', 'i'),      # Leila -> Lila
            (r'ie', 'i'),      # Nadim -> Nadim
            
            # 2. Vowel Normalization and reduction
            (r'aa', 'a'),      # Aamer -> Amer
            (r'ee', 'i'),      # Jameel -> Jamil
            (r'oo', 'u'),      # Mahmood -> Mahmud
            (r'y', 'i'),       # Youssef -> Iussef
            (r'ea', 'i'),      # Jean -> Jin
            
            # 3. Consonant Normalization (map many-to-one)
            (r'q', 'k'),       # Tariq -> Tarik
            (r'c', 'k'),       # Carol -> Karol
            (r'z', 's'),       # Ziad -> Siad
            (r'w', 'u'),       # Walid -> Ualid (often a vowel sound)
            
            # 4. Remove silent/doubled letters
            (r'([a-z])\1+', r'\1'), # Tammam -> Tamam, Mohammed -> Mohamed
        ]
    
    def normalize(self, text: str) -> str:
        """
        Apply phonetic normalization to the given text.
        
        This method is the public interface implementing the Normalizer protocol.
        
        Args:
            text: The text to normalize
            
        Returns:
            The phonetically normalized text
        """
        return self.normalize_token(text)
    
    def normalize_token(self, token: str) -> str:
        """
        Apply all phonetic rules to a single token.
        
        Args:
            token: The token to normalize
            
        Returns:
            The normalized token
        """
        if not token:
            return ""
            
        # Basic cleanup: lowercase and keep only letters
        token = re.sub(r'[^a-z]', '', token.lower())

        # Apply all phonetic rules in sequence
        for pattern, replacement in self._PHONETIC_RULES:
            token = re.sub(pattern, replacement, token)
            
        return token
