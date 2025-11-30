"""
Domain Entity: Name

This module defines the Name value object, representing a processed name
as an immutable collection of tokens.
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Name:
    """
    Value object representing a processed name.
    
    A name consists of normalized, validated tokens. This class is immutable
    to ensure that once created, a Name object cannot be modified.
    
    Attributes:
        tokens: List of normalized name tokens
    """
    tokens: tuple[str, ...]
    
    def __post_init__(self):
        """Validate the name tokens after initialization."""
        if not isinstance(self.tokens, tuple):
            # Convert to tuple if a list was provided
            object.__setattr__(self, 'tokens', tuple(self.tokens))
        
        # Validate that all tokens are non-empty strings
        for token in self.tokens:
            if not isinstance(token, str) or not token:
                raise ValueError(f"Invalid token: {token}")
    
    @classmethod
    def from_tokens(cls, tokens: List[str]) -> 'Name':
        """
        Create a Name object from a list of tokens.
        
        Args:
            tokens: List of name tokens
            
        Returns:
            Name object with the given tokens
        """
        return cls(tokens=tuple(tokens))
    
    def to_string(self, separator: str = " ") -> str:
        """
        Convert the name to a string representation.
        
        Args:
            separator: String to use for joining tokens (default: space)
            
        Returns:
            String representation of the name
        """
        return separator.join(self.tokens)
    
    def __str__(self) -> str:
        """Return string representation of the name."""
        return self.to_string()
    
    def __repr__(self) -> str:
        """Return detailed representation of the name."""
        return f"Name(tokens={self.tokens})"
    
    def is_empty(self) -> bool:
        """Check if the name has no tokens."""
        return len(self.tokens) == 0
