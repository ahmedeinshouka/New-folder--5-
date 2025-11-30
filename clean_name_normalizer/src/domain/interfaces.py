from abc import ABC, abstractmethod
from typing import List
from .models import Name

class INormalizationRule(ABC):
    @abstractmethod
    def apply(self, text: str) -> str:
        """Apply a normalization rule to the text."""
        pass

class INameNormalizer(ABC):
    @abstractmethod
    def normalize(self, name: str) -> Name:
        """Normalize a name."""
        pass
