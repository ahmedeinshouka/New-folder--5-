import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

def verify_rules_refactor():
    print("Verifying rules refactor...")
    
    # 1. Check if we can import rules from the new location
    try:
        from domain.rules import ARABIC_NORMALIZATION_MAP, ARABIC_DIACRITICS_PATTERN, COMPOUND_NAMES
        print("[OK] Successfully imported rules from domain.rules")
    except ImportError as e:
        print(f"[FAIL] Failed to import rules from domain.rules: {e}")
        return False

    # 2. Check if ArabicNormalizer uses the new rules
    try:
        from domain.services.arabic_normalizer import ArabicNormalizer
        normalizer = ArabicNormalizer()
        # Check if it has the map (just checking one key)
        if "أ" in normalizer._normalization_map:
             print("[OK] ArabicNormalizer initialized with default rules")
        else:
             print("[FAIL] ArabicNormalizer missing normalization map")
             return False
    except ImportError as e:
        print(f"[FAIL] Failed to import ArabicNormalizer: {e}")
        return False
        
    # 3. Check if main preprocessing still works (using a case that matches the rules exactly)
    # Rule is: ("abdel", "rahman", "abdelrahman")
    try:
        from preprocessing import preprocess_name
        # "Abdel Rahman" -> "abdel", "rahman" -> "abdelrahman"
        result = preprocess_name("Mr. Abdel Rahman")
        if "abdelrahman" in result:
            print(f"[OK] Preprocessing with compound names works: '{result}'")
        else:
            print(f"[FAIL] Preprocessing failed to merge compound name: '{result}'")
            return False
    except Exception as e:
        print(f"[FAIL] Preprocessing raised exception: {e}")
        return False

    print("Verification successful!")
    return True

if __name__ == "__main__":
    verify_rules_refactor()
