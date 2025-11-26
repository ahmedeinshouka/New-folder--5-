import tkinter as tk
from tkinter import ttk
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

class NormalizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Normalizer")
        self.root.geometry("600x400")
        
        self.setup_pipeline()
        self.create_widgets()
        
    def setup_pipeline(self):
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
            NormalizeWhitespaceRule()
        ]
        self.normalizer = NormalizeNameUseCase(rules)
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input section
        input_label = ttk.Label(main_frame, text="Enter Name:", font=("Helvetica", 12, "bold"))
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(main_frame, textvariable=self.input_var, font=("Helvetica", 11))
        self.input_entry.pack(fill=tk.X, pady=(0, 15))
        self.input_entry.bind('<Return>', self.normalize)
        
        # Button
        normalize_btn = ttk.Button(main_frame, text="Normalize", command=self.normalize)
        normalize_btn.pack(anchor=tk.CENTER, pady=(0, 20))
        
        # Output section
        output_label = ttk.Label(main_frame, text="Normalized Result:", font=("Helvetica", 12, "bold"))
        output_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.output_text = tk.Text(main_frame, height=5, font=("Consolas", 11), state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
    def normalize(self, event=None):
        name = self.input_var.get()
        result = self.normalizer.normalize(name)
        
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.normalized)
        self.output_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = NormalizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
