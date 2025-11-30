"""
Infrastructure Normalizer: Compound Name Merger

This infrastructure component handles the merging of compound names
(e.g., "abdel rahman" -> "abdelrahman").
"""

from typing import List, Set, Tuple


class CompoundNameMerger:
    """
    Merges multi-token compound names into single tokens.
    
    This is an infrastructure concern because it depends on external
    configuration data (the list of compound name patterns).
    """
    
    def __init__(self, compound_patterns: List[Tuple[str, str, str]]):
        """
        Initialize the compound name merger.
        
        Args:
            compound_patterns: List of (first_part, second_part, merged_form) tuples
        """
        self._compound_patterns = compound_patterns
        self._first_parts: Set[str] = {pattern[0] for pattern in compound_patterns}
    
    def merge(self, tokens: List[str]) -> List[str]:
        """
        Merge compound names in the token list.
        
        Args:
            tokens: List of name tokens
            
        Returns:
            List of tokens with compound names merged
        """
        i = 0
        output_tokens = []
        
        while i < len(tokens):
            # Check if this token could be the start of a compound name
            if tokens[i] in self._first_parts and i + 1 < len(tokens):
                merged = False
                
                # Try to match against all compound patterns
                for first, second, compound in self._compound_patterns:
                    if tokens[i] == first and tokens[i+1] == second:
                        output_tokens.append(compound)
                        i += 2
                        merged = True
                        break
                
                # If no match, add the token as-is
                if not merged:
                    output_tokens.append(tokens[i])
                    i += 1
            else:
                output_tokens.append(tokens[i])
                i += 1
        
        return output_tokens
