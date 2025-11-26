from ..use_cases.normalize_name import NormalizeNameUseCase
from ..adapters.rules.cleaning import (
    HandleNullLikeValuesRule, HandleEncodingIssuesRule, RemoveHtmlEntitiesRule,
    UnicodeNormalizationRule, RemoveUnwantedCharactersRule, NormalizeSeparatorsRule,
    NormalizeWhitespaceRule
)
from ..adapters.rules.arabic import ArabicNormalizationRule, RemoveDiacriticsRule
from ..adapters.rules.english import (
    EnglishNormalizationRule, RemoveTitlesRule, RemoveNoiseWordsRule,
    MergeCompoundNamesRule, RemoveShortTokensRule, RemoveNumericTokensRule
)
from ..adapters.rules.phonetic import PhoneticNormalizationRule

def main():
    # Configure the pipeline
    rules = [
        HandleNullLikeValuesRule(),
        HandleEncodingIssuesRule(),
        RemoveHtmlEntitiesRule(),
        UnicodeNormalizationRule(),
        RemoveUnwantedCharactersRule(),
        NormalizeSeparatorsRule(),
        NormalizeWhitespaceRule(),
        ArabicNormalizationRule(),
        RemoveDiacriticsRule(),
        EnglishNormalizationRule(),
        RemoveTitlesRule(),
        RemoveNoiseWordsRule(),
        MergeCompoundNamesRule(),
        PhoneticNormalizationRule(),
        RemoveShortTokensRule(),
        RemoveNumericTokensRule(),
        NormalizeWhitespaceRule() # Final cleanup
    ]
    
    normalizer = NormalizeNameUseCase(rules)
    
    names_to_normalize = [
        "Dr. Mohammed KHALED",
        "Mr. Mohamad Haled",
        "Eng. Muhammed khalid",
        "Ghaleb Charbel",
        "Galeb Sharbel",
        "Mahmoud Youssef",
        "Mahmud Yousef",
        "Tariq Shadi",
        "Tarek Sadi",
        "شركة/ أبناء يوسف وأولاده المتحدة",
        "أ.د/ مُحَمَّدٌ حُسَيْن الخالدي",
        "Mr. Abd-Elrahman Mahmoud",
        "عبد الرحمن محمود",
        "Acme Corporation Ltd. -- 1985",
        "NULL",
    ]
    
    print("--- Clean Architecture Name Normalization ---")
    for name in names_to_normalize:
        processed_name = normalizer.normalize(name)
        print(f"Original:  '{name}'")
        print(f"Processed: '{processed_name.normalized}'\n")

if __name__ == "__main__":
    main()
