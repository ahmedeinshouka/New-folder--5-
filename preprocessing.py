"""
Backward Compatibility Layer

This module maintains the original public API for the preprocessing functionality,
allowing existing code to continue working without changes while internally using
the new Clean Architecture implementation.
"""

from typing import Optional

from domain.services.phonetic_normalizer import PhoneticNormalizer
from domain.services.arabic_normalizer import ArabicNormalizer
from infrastructure.normalizers.compound_name_merger import CompoundNameMerger
from domain.rules import COMPOUND_NAMES
from use_cases.preprocess_name import PreprocessNameUseCase


# Initialize the use case with all dependencies
_phonetic_normalizer = PhoneticNormalizer()
_arabic_normalizer = ArabicNormalizer()
_compound_name_merger = CompoundNameMerger(COMPOUND_NAMES)

_preprocess_use_case = PreprocessNameUseCase(
    phonetic_normalizer=_phonetic_normalizer,
    arabic_normalizer=_arabic_normalizer,
    compound_name_merger=_compound_name_merger,
)


def preprocess_name(
    name: Optional[str],
    *,
    remove_duplicates: bool = True,
    sort_tokens: bool = True,
    preserve_order: bool = False,
    min_token_length: int = 2,
) -> str:
    """
    Cleans, normalizes, and standardizes a name string using structural and phonetic rules.
    
    This is the backward-compatible public API that maintains the same signature
    as the original monolithic implementation.
    
    Args:
        name: The name string to preprocess
        remove_duplicates: Whether to remove duplicate tokens (default: True)
        sort_tokens: Whether to sort tokens alphabetically (default: True)
        preserve_order: Whether to preserve original token order (default: False)
        min_token_length: Minimum length for tokens to be kept (default: 2)
        
    Returns:
        Preprocessed name as a space-separated string
        
    Examples:
        >>> preprocess_name("Dr. Mohammed KHALED")
        'haled mohamed'
        
        >>> preprocess_name("Mr. Abd-Elrahman Mahmoud")
        'abdelrahman mahmud'
    """
    # Execute the use case
    name_entity = _preprocess_use_case.execute(
        name,
        remove_duplicates=remove_duplicates,
        sort_tokens=sort_tokens,
        preserve_order=preserve_order,
        min_token_length=min_token_length,
    )
    
    # Return as string for backward compatibility
    return name_entity.to_string()


# Export the main public API
__all__ = ['preprocess_name']