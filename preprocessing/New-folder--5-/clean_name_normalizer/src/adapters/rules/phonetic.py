import re
from ...domain.interfaces import INormalizationRule

class PhoneticNormalizationRule(INormalizationRule):
    def __init__(self):
        self._PHONETIC_RULES = [
            # 1. Digraphs and common transliterations (most specific)
            (r'kh', 'h'),      # Khaled -> Haled
            (r'gh', 'g'),      # Ghada -> Gada
            (r'sh', 's'),      # Shadi -> Sadi
            (r'th', 't'),      # Thamer -> Tamer
            (r'ph', 'f'),      # Philip -> Filip
            (r'ch', 's'),      # Charbel -> Sarbel
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
            (r'w', 'u'),       # Walid -> Ualid
            
            # 4. Remove silent/doubled letters
            (r'([a-z])\1+', r'\1'), # Tammam -> Tamam
        ]

    def normalize_token(self, token: str) -> str:
        if not token:
            return ""
        
        # Basic cleanup: lowercase and keep only letters
        token = re.sub(r'[^a-z]', '', token.lower())

        for pattern, replacement in self._PHONETIC_RULES:
            token = re.sub(pattern, replacement, token)
            
        return token

    def apply(self, text: str) -> str:
        tokens = text.split()
        normalized_tokens = []
        for token in tokens:
            # Apply phonetic normalization ONLY to English-like tokens
            if re.match(r'^[a-z]+$', token):
                normalized_tokens.append(self.normalize_token(token))
            else:
                normalized_tokens.append(token)
        return " ".join(normalized_tokens)
