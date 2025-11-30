"""
Preprocessing Package - Clean Architecture Implementation

This package provides name preprocessing functionality following Clean Architecture principles.

## Public API

For backward compatibility, use:
```python
from preprocessing import preprocess_name

result = preprocess_name("Dr. Mohammed KHALED")
```

## Architecture

The package is organized into four layers:

1. **Domain Layer** (`domain/`):
   - Entities: `Name` value object
   - Services: `PhoneticNormalizer`, `ArabicNormalizer`
   - Interfaces: `Normalizer` protocol

2. **Use Cases Layer** (`use_cases/`):
   - `PreprocessNameUseCase`: Orchestrates the preprocessing workflow

3. **Infrastructure Layer** (`infrastructure/`):
   - Configuration: Constants and rules
   - Normalizers: `CompoundNameMerger`

4. **Interface Adapters Layer** (`interface_adapters/`):
   - DTOs for request/response handling
"""

from preprocessing import preprocess_name

__all__ = ['preprocess_name']
