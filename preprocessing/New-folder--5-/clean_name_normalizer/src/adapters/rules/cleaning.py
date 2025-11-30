import re
import unicodedata
from ...domain.interfaces import INormalizationRule
from ...infrastructure.config import NULL_LIKE_VALUES, REMOVE_CHARS

class HandleNullLikeValuesRule(INormalizationRule):
    def apply(self, text: str) -> str:
        if text.lower().strip() in NULL_LIKE_VALUES:
            return ""
        return text

class HandleEncodingIssuesRule(INormalizationRule):
    def apply(self, text: str) -> str:
        try:
            if isinstance(text, bytes):
                text = text.decode('utf-8', errors='ignore')
            # Remove non-printable characters except spaces
            text = ''.join(char for char in text if char.isprintable() or char.isspace())
        except:
            pass
        return text

class RemoveHtmlEntitiesRule(INormalizationRule):
    def apply(self, text: str) -> str:
        text = re.sub(r'&[a-zA-Z]+;', '', text)
        text = re.sub(r'&#\d+;', '', text)
        text = re.sub(r'<[^>]+>', '', text)
        return text

class UnicodeNormalizationRule(INormalizationRule):
    def apply(self, text: str) -> str:
        return unicodedata.normalize("NFKC", text)

class RemoveUnwantedCharactersRule(INormalizationRule):
    def apply(self, text: str) -> str:
        for char in REMOVE_CHARS:
            text = text.replace(char, ' ')
        return text

class NormalizeSeparatorsRule(INormalizationRule):
    def apply(self, text: str) -> str:
        separators = ['-', '_', '.', '/', '\\', '|', '،', '؛']
        for sep in separators:
            text = text.replace(sep, ' ')
        return text

class NormalizeWhitespaceRule(INormalizationRule):
    def apply(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()
