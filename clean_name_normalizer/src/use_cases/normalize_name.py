from typing import List
from ..domain.models import Name
from ..domain.interfaces import INameNormalizer, INormalizationRule

class NormalizeNameUseCase(INameNormalizer):
    def __init__(self, rules: List[INormalizationRule]):
        self.rules = rules

    def normalize(self, name: str) -> Name:
        if not name:
            return Name(original=name if name is not None else "", normalized="")
        
        current_text = name
        for rule in self.rules:
            current_text = rule.apply(current_text)
            
        return Name(original=name, normalized=current_text)
