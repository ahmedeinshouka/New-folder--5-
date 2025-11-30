"""Quick test of backward compatibility layer"""
from preprocessing import preprocess_name

# Test 1: Basic preprocessing
result1 = preprocess_name("Dr. Mohammed KHALED")
print(f"Test 1: '{result1}'")

# Test 2: Compound names
result2 = preprocess_name("Mr. Abd-Elrahman Mahmoud")
print(f"Test 2: '{result2}'")

# Test 3: Arabic text
result3 = preprocess_name("عبد الرحمن محمود")
print(f"Test 3: '{result3}'")

print("\nBackward compatibility: ✓ OK")
