"""
Use Case: Preprocess Name

This use case orchestrates the complete name preprocessing workflow,
coordinating between domain services and infrastructure components.
"""

import re
import unicodedata
from typing import Optional, List, Set

from domain.entities.name import Name
from domain.services.phonetic_normalizer import PhoneticNormalizer
from domain.services.arabic_normalizer import ArabicNormalizer
from infrastructure.normalizers.compound_name_merger import CompoundNameMerger
from infrastructure.config.constants import (
    TITLES,
    NOISE_WORDS,
    NULL_LIKE_VALUES,
    REMOVE_CHARS_PATTERN,
    INVISIBLE_CHARS_PATTERN,
    HTML_TAG_PATTERN,
    WHITESPACE_PATTERN,
)


class PreprocessNameUseCase:
    """
    Use case for preprocessing and normalizing name strings.
    
    This class orchestrates the complete name preprocessing pipeline,
    following the Single Responsibility Principle by delegating specific
    tasks to domain services and infrastructure components.
    """
    
    def __init__(
        self,
        phonetic_normalizer: PhoneticNormalizer,
        arabic_normalizer: ArabicNormalizer,
        compound_name_merger: CompoundNameMerger,
        titles: Set[str] = TITLES,
        noise_words: Set[str] = NOISE_WORDS,
        null_like_values: Set[str] = NULL_LIKE_VALUES,
    ):
        """
        Initialize the use case with required dependencies.
        
        Args:
            phonetic_normalizer: Service for phonetic normalization
            arabic_normalizer: Service for Arabic text normalization
            compound_name_merger: Component for merging compound names
            titles: Set of title words to remove
            noise_words: Set of noise words to remove
            null_like_values: Set of null-like values to check
        """
        self._phonetic_normalizer = phonetic_normalizer
        self._arabic_normalizer = arabic_normalizer
        self._compound_name_merger = compound_name_merger
        self._titles = titles
        self._noise_words = noise_words
        self._null_like_values = null_like_values
    
    def execute(
        self,
        name: Optional[str],
        *,
        remove_duplicates: bool = True,
        sort_tokens: bool = True,
        preserve_order: bool = False,
        min_token_length: int = 2,
    ) -> Name:
        """
        Execute the name preprocessing pipeline.
        
        Args:
            name: The name string to preprocess
            remove_duplicates: Whether to remove duplicate tokens
            sort_tokens: Whether to sort tokens alphabetically
            preserve_order: Whether to preserve original token order
            min_token_length: Minimum length for tokens to be kept
            
        Returns:
            Name entity with processed tokens
        """
        # 1. Initial Sanity Checks and Cleaning
        if not name or not isinstance(name, str):
            return Name.from_tokens([])
        
        clean_name = name.lower().strip()
        if clean_name in self._null_like_values:
            return Name.from_tokens([])
        
        # 2. Character-level and Structural Cleaning
        clean_name = self._clean_text(clean_name)
        
        # 3. Tokenization and Noise Removal
        tokens = self._tokenize_and_filter(clean_name)
        
        # 4. Semantic and Phonetic Normalization
        tokens = self._normalize_tokens(tokens)
        
        # 5. Final Assembly
        tokens = self._finalize_tokens(
            tokens,
            remove_duplicates=remove_duplicates,
            sort_tokens=sort_tokens,
            preserve_order=preserve_order,
            min_token_length=min_token_length,
        )
        
        return Name.from_tokens(tokens)
    
    def _clean_text(self, text: str) -> str:
        """
        Apply character-level cleaning to the text.
        
        Args:
            text: The text to clean
            
        Returns:
            Cleaned text
        """
        # Unicode normalization
        try:
            text = unicodedata.normalize("NFKC", text)
        except Exception:
            pass
        
        # Remove HTML tags
        text = re.sub(HTML_TAG_PATTERN, " ", text)
        
        # Remove invisible characters
        text = re.sub(INVISIBLE_CHARS_PATTERN, '', text)
        
        # Remove special characters
        text = re.sub(REMOVE_CHARS_PATTERN, ' ', text)
        
        # Normalize Arabic text
        text = self._arabic_normalizer.normalize(text)
        
        # Collapse whitespace
        text = re.sub(WHITESPACE_PATTERN, ' ', text).strip()
        
        return text
    
    def _tokenize_and_filter(self, text: str) -> List[str]:
        """
        Tokenize the text and filter out noise words.
        
        Args:
            text: The text to tokenize
            
        Returns:
            List of filtered tokens
        """
        tokens = text.split()
        
        # Filter out titles, noise words, and pure digits
        tokens = [
            t for t in tokens 
            if t not in self._titles 
            and t not in self._noise_words 
            and not t.isdigit()
        ]
        
        return tokens
    
    def _normalize_tokens(self, tokens: List[str]) -> List[str]:
        """
        Apply semantic and phonetic normalization to tokens.
        
        Args:
            tokens: List of tokens to normalize
            
        Returns:
            List of normalized tokens
        """
        # First, merge compound names
        tokens = self._compound_name_merger.merge(tokens)
        
        # Apply phonetic normalization to English-like tokens only
        normalized_tokens = []
        for token in tokens:
            # Check if token is pure ASCII letters
            if re.match(r'^[a-z]+$', token):
                normalized_tokens.append(self._phonetic_normalizer.normalize(token))
            else:
                # Keep non-English tokens (e.g., Arabic) as-is
                normalized_tokens.append(token)
        
        return normalized_tokens
    
    def _finalize_tokens(
        self,
        tokens: List[str],
        *,
        remove_duplicates: bool,
        sort_tokens: bool,
        preserve_order: bool,
        min_token_length: int,
    ) -> List[str]:
        """
        Apply final processing to tokens.
        
        Args:
            tokens: List of tokens to finalize
            remove_duplicates: Whether to remove duplicate tokens
            sort_tokens: Whether to sort tokens
            preserve_order: Whether to preserve order
            min_token_length: Minimum token length
            
        Returns:
            Finalized list of tokens
        """
        # Filter by minimum length
        tokens = [t for t in tokens if len(t) >= min_token_length]
        
        # Remove duplicates while preserving order
        if remove_duplicates:
            seen = set()
            tokens = [t for t in tokens if not (t in seen or seen.add(t))]
        
        # Sort tokens if requested and order preservation is not required
        if sort_tokens and not preserve_order:
            tokens.sort()
        
        return tokens
