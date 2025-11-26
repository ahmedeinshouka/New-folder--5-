"""
Main Entry Point - Name Preprocessing Module

This module demonstrates how to use the Clean Architecture implementation
directly, including dependency injection and use case execution.
"""

from domain.services.phonetic_normalizer import PhoneticNormalizer
from domain.services.arabic_normalizer import ArabicNormalizer
from infrastructure.normalizers.compound_name_merger import CompoundNameMerger
from infrastructure.config.rules import COMPOUND_NAMES
from use_cases.preprocess_name import PreprocessNameUseCase


def main():
    """
    Demonstrate the name preprocessing functionality with various test cases.
    """
    # Set UTF-8 encoding for Windows console
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # Initialize dependencies
    phonetic_normalizer = PhoneticNormalizer()
    arabic_normalizer = ArabicNormalizer()
    compound_name_merger = CompoundNameMerger(COMPOUND_NAMES)
    
    # Create the use case with injected dependencies
    preprocess_use_case = PreprocessNameUseCase(
        phonetic_normalizer=phonetic_normalizer,
        arabic_normalizer=arabic_normalizer,
        compound_name_merger=compound_name_merger,
    )
    
    # Test cases demonstrating various normalization scenarios
    names_to_normalize = [
        # --- Demonstrating the phonetic normalization ---
        "Dr. Mohammed KHALED",
        "Mr. Mohamad Haled",
        "Eng. Muhammed khalid",
        "Ghaleb Charbel",
        "Galeb Sharbel",
        "Mahmoud Youssef",
        "Mahmud Yousef",
        "Tariq Shadi",
        "Tarek Sadi",
        "sha3ban",
        "ahmed,karim",
        # --- Demonstrating robustness with mixed and Arabic names ---
        "شركة/ أبناء يوسف وأولاده المتحدة",
        "أ.د/ مُحَمَّدٌ حُسَيْن الخالدي",
        "Mr. Abd-Elrahman Mahmoud",
        "عبد الرحمن محمود",
        "Acme Corporation Ltd. -- 1985",
        "NULL",
    ]
    
    print("=" * 60)
    print("Dynamic Name Normalization Pipeline - Clean Architecture")
    print("=" * 60)
    print()
    
    for name in names_to_normalize:
        # Execute the use case
        processed_name_entity = preprocess_use_case.execute(name)
        processed_name = processed_name_entity.to_string()
        
        print(f"Original:  '{name}'")
        print(f"Processed: '{processed_name}'")
        print()
    
    # Example showing how different spellings converge to one form
    print("-" * 60)
    print("Demonstrating phonetic convergence:")
    print("-" * 60)
    print("All the following variations:")
    
    variations = ["Mohammed", "Mohammad", "Mohamad", "Muhammed", "Mohamed", "Mhmd"]
    results = {}
    
    for v in variations:
        name_entity = preprocess_use_case.execute(v)
        processed = name_entity.to_string()
        results[v] = processed
        print(f"  - '{v}' → '{processed}'")
    
    # Check if they all normalize to the same result
    unique_results = set(results.values())
    if len(unique_results) == 1:
        print(f"\n✓ All variations normalize to: '{list(unique_results)[0]}'")
    else:
        print(f"\n⚠ Warning: Got {len(unique_results)} different results: {unique_results}")
    
    print("-" * 60)


if __name__ == "__main__":
    main()
