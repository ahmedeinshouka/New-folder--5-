"""
Domain Interface: Normalizer Protocol

This module defines the abstract interface that all normalizers must implement.
Following the Dependency Inversion Principle, this allows the domain layer to
define contracts without depending on concrete implementations.
"""

from typing import Protocol


class Normalizer(Protocol):
    """
    Protocol defining the contract for all text normalizers.
    
    Any class implementing this protocol must provide a normalize method
    that takes a string and returns a normalized string.
    """
    
    def normalize(self, text: str) -> str:
        """
        Normalize the given text according to the normalizer's rules.
        
        Args:
            text: The text to normalize
            
        Returns:
            The normalized text
        """
        ...
