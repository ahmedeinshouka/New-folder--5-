import re
from ...domain.interfaces import INormalizationRule
from ...infrastructure.config import ARABIC_NORMALIZATION_MAP, ARABIC_DIACRITICS_PATTERN

class ArabicNormalizationRule(INormalizationRule):
    def apply(self, text: str) -> str:
        if not text:
            return ""
        for original, normalized in ARABIC_NORMALIZATION_MAP.items():
            text = text.replace(original, normalized)
        return text

class RemoveDiacriticsRule(INormalizationRule):
    def apply(self, text: str) -> str:
        return re.sub(ARABIC_DIACRITICS_PATTERN, "", text)
