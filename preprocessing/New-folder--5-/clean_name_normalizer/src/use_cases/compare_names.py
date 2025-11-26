from .normalize_name import NormalizeNameUseCase

class CompareNamesUseCase:
    def __init__(self, normalizer: NormalizeNameUseCase):
        self.normalizer = normalizer

    def execute(self, name1: str, name2: str) -> bool:
        norm1 = self.normalizer.normalize(name1)
        norm2 = self.normalizer.normalize(name2)
        return norm1.normalized == norm2.normalized
    
    def similarity_score(self, name1: str, name2: str) -> float:
        norm1 = self.normalizer.normalize(name1)
        norm2 = self.normalizer.normalize(name2)
        
        tokens1 = set(norm1.normalized.split())
        tokens2 = set(norm2.normalized.split())
        
        if not tokens1 or not tokens2:
            return 0.0
            
        intersection = tokens1 & tokens2
        union = tokens1 | tokens2
        
        return len(intersection) / len(union) if union else 0.0
