from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Name:
    original: str
    normalized: str = ""
    
    def __str__(self):
        return self.normalized if self.normalized else self.original

@dataclass(frozen=True)
class Token:
    value: str
    is_noise: bool = False
    is_title: bool = False
