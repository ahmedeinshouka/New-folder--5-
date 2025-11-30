import re
from typing import List
from ...domain.interfaces import INormalizationRule
from ...infrastructure.config import NAME_VARIATIONS, TITLES, NOISE_WORDS, COMPOUND_NAMES

class EnglishNormalizationRule(INormalizationRule):
    def apply(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"(.)\1{2,}", r"\1", text)  # Remove excessive repetition
        tokens = text.split()
        normalized_tokens = [NAME_VARIATIONS.get(t, t) for t in tokens]
        return " ".join(normalized_tokens)

class RemoveTitlesRule(INormalizationRule):
    def apply(self, text: str) -> str:
        tokens = text.split()
        return " ".join(t for t in tokens if t.lower() not in TITLES)

class RemoveNoiseWordsRule(INormalizationRule):
    def apply(self, text: str) -> str:
        tokens = text.split()
        return " ".join(t for t in tokens if t.lower() not in NOISE_WORDS)

class MergeCompoundNamesRule(INormalizationRule):
    def apply(self, text: str) -> str:
        tokens = text.split()
        i = 0
        merged = []
        while i < len(tokens):
            merged_flag = False
            for first, second, compound in COMPOUND_NAMES:
                if i + 1 < len(tokens) and tokens[i] == first and tokens[i + 1] == second:
                    merged.append(compound)
                    i += 2
                    merged_flag = True
                    break
            if not merged_flag:
                merged.append(tokens[i])
                i += 1
        return " ".join(merged)

class RemoveShortTokensRule(INormalizationRule):
    def __init__(self, min_length: int = 2):
        self.min_length = min_length

    def apply(self, text: str) -> str:
        tokens = text.split()
        return " ".join(t for t in tokens if len(t) >= self.min_length)

class RemoveNumericTokensRule(INormalizationRule):
    def apply(self, text: str) -> str:
        tokens = text.split()
        return " ".join(t for t in tokens if not t.isdigit())
