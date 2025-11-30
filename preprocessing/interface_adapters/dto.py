"""
Interface Adapters: Data Transfer Objects

This module defines DTOs for converting between external formats
and domain entities.
"""

from dataclasses import dataclass
from typing import Optional

from domain.entities.name import Name


@dataclass
class NamePreprocessingRequest:
    """
    Request DTO for name preprocessing.
    
    Attributes:
        name: The name string to preprocess
        remove_duplicates: Whether to remove duplicate tokens
        sort_tokens: Whether to sort tokens alphabetically
        preserve_order: Whether to preserve original token order
        min_token_length: Minimum length for tokens to be kept
    """
    name: Optional[str]
    remove_duplicates: bool = True
    sort_tokens: bool = True
    preserve_order: bool = False
    min_token_length: int = 2


@dataclass
class NamePreprocessingResponse:
    """
    Response DTO for name preprocessing.
    
    Attributes:
        processed_name: The processed name as a string
        tokens: List of individual tokens
        is_empty: Whether the result has no tokens
    """
    processed_name: str
    tokens: list[str]
    is_empty: bool
    
    @classmethod
    def from_name_entity(cls, name: Name) -> 'NamePreprocessingResponse':
        """
        Create a response DTO from a Name domain entity.
        
        Args:
            name: The Name entity
            
        Returns:
            NamePreprocessingResponse with data from the entity
        """
        return cls(
            processed_name=name.to_string(),
            tokens=list(name.tokens),
            is_empty=name.is_empty(),
        )
