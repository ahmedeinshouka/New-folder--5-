import re

# -----------------------
# Configuration & Constants
# -----------------------

ARABIC_NORMALIZATION_MAP = {
    # Alef variants
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ٲ": "ا", "ٳ": "ا",
    # Ya variants
    "ى": "ي", "ئ": "ي", "ۍ": "ي", "ێ": "ي",
    # Waw variants
    "ؤ": "و", "ۆ": "و",
    # Ta Marbuta
    "ة": "ه", "ۃ": "ه",
    # Ha variants
    "ھ": "ه",
}

ARABIC_DIACRITICS_PATTERN = re.compile(
    r"[\u064B-\u065F\u0670\u06D6-\u06ED\u08D4-\u08E1\u08D3-\u08FF\uFE70-\uFEFF]"
)

TITLES = {
    # English titles
    "mr", "mr.", "mrs", "mrs.", "ms", "ms.", "miss", "mister", "mistress",
    "dr", "dr.", "doctor", "prof", "prof.", "professor",
    "eng", "eng.", "engineer", "sir", "lady", "lord", "dame",
    "capt", "capt.", "captain", "col", "col.", "colonel", "gen", "gen.", "general",
    "lt", "lt.", "lieutenant", "maj", "maj.", "major", "sgt", "sergeant",
    "rev", "rev.", "reverend", "fr", "fr.", "father", "sr", "sr.", "sister",
    "hon", "hon.", "honorable", "esq", "esq.", "esquire",
    # Arabic titles
    "باشا", "بشا", "بيه", "بك", "أفندي", "افندي",
    "دكتور", "د", "د.", "دكتوره",
    "مهندس", "مهندسه", "م", "م.", "مهندسة",
    "أستاذ", "استاذ", "أ", "أ.", "ا", "ا.", "استاذه", "أستاذة",
    "شيخ", "الشيخ", "شيخة",
    "سيد", "سيدة", "آنسة", "انسة", "السيد", "السيدة",
    "حاج", "حاجة", "الحاج", "الحاجة", "حاجه",
    "قائد", "رائد", "عميد", "لواء", "فريق",
}

NOISE_WORDS = {
    # English noise
    "co", "co.", "company", "corp", "corp.", "corporation", "inc", "inc.", "incorporated",
    "group", "sons", "son", "and", "&", "the", "of", "for",
    "ltd", "ltd.", "limited", "plc", "llc", "llc.", "gmbh",
    "associates", "associate", "brothers", "brother", "bros", "bros.",
    "establishment", "est", "est.", "enterprise", "enterprises",
    # Arabic noise
    "بن", "ابن", "ابو", "أبو", "أبي", "ابي",
    "آل", "ال", "ال.", "و", "و.", "من",
    "شركة", "شركه", "شركات", "مجموعة", "مجموعه", "مجموعات",
    "واولاده", "وأولاده", "وشركاه", "وشركائه", "وأولاد",
    "مؤسسة", "مؤسسه", "مكتب", "بيت",
    # Common geographic/nationality markers
    "المصري", "المصريه", "المصرية", "مصري", "مصرية", "مصريه",
    "السعودي", "السعودية", "سعودي", "سعودية", "سعوديه",
    "اللبناني", "اللبنانية", "لبناني", "لبنانية", "لبنانيه",
    "الاردني", "الأردني", "اردني", "أردني",
    "السوري", "سوري", "سورية", "سوريه",
    "العراقي", "عراقي", "عراقية",
    "الكويتي", "كويتي", "كويتية",
    "الاماراتي", "الإماراتي", "اماراتي", "إماراتي",
}

COMPOUND_NAMES = [
    # Abd/Abdul variants - Rahman
    ("abdel", "rahman", "abdelrahman"), ("abdul", "rahman", "abdulrahman"),
    ("abd", "rahman", "abdrahman"), ("abdal", "rahman", "abdalrahman"),
    ("عبد", "الرحمن", "عبدالرحمن"), ("عبد", "رحمن", "عبدالرحمن"),
    # Abd/Abdul variants - Aziz
    ("abdel", "aziz", "abdelaziz"), ("abdul", "aziz", "abdulaziz"),
    ("abd", "aziz", "abdaziz"), ("عبد", "العزيز", "عبدالعزيز"),
    ("عبد", "عزيز", "عبدالعزيز"),
    # Abd/Abdul variants - Other
    ("abdel", "kader", "abdelkader"), ("abdul", "kader", "abdulkader"),
    ("abdel", "hamid", "abdelhamid"), ("abdul", "hamid", "abdulhamid"),
    ("abdel", "latif", "abdellatif"), ("abdul", "latif", "abdullatif"),
    ("abdel", "moneim", "abdelmoneim"), ("abdul", "moneim", "abdulmoneim"),
    ("abdel", "salam", "abdelsalam"), ("abdul", "salam", "abdulsalam"),
    ("abdel", "fattah", "abdelfattah"), ("abdul", "fattah", "abdulfattah"),
    ("abdel", "wahab", "abdelwahab"), ("abdul", "wahab", "abdulwahab"),
    ("abdel", "malik", "abdelmalik"), ("abdul", "malik", "abdulmalik"),
    ("abdel", "nasser", "abdelnasser"), ("abdul", "nasser", "abdulnasser"),
    ("abdel", "halim", "abdelhalim"), ("abdul", "halim", "abdulhalim"),
    ("abdel", "karim", "abdelkarim"), ("abdul", "karim", "abdulkarim"),
    ("abdel", "majid", "abdelmajid"), ("abdul", "majid", "abdulmajid"),
    # Abu compounds
    ("abu", "baker", "abubaker"), ("abu", "bakr", "abubakr"),
    ("abu", "el", "abuel"), ("أبو", "بكر", "أبوبكر"),
    # Mohamed/Ali compounds
    ("mohamed", "ali", "mohamedali"), ("mohammed", "ali", "mohammedali"),
    ("محمد", "علي", "محمدعلي"),
    # Arabic Abd compounds
    ("عبد", "الله", "عبدالله"), ("عبد", "الكريم", "عبدالكريم"),
    ("عبد", "الحميد", "عبدالحميد"), ("عبد", "المجيد", "عبدالمجيد"),
    ("عبد", "الناصر", "عبدالناصر"), ("عبد", "الحليم", "عبدالحليم"),
]

NULL_LIKE_VALUES = {"null", "none", "n/a", "na", "nil", "undefined", "unknown", "#n/a", "#null", "غير معروف", "غير_معروف", "لا يوجد"}

REMOVE_CHARS = {
    # Special symbols
    '~', '`', '!', '@', '#', '$', '%', '^', '*', '(', ')', 
    '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', 
    "'", '<', '>', '?', '/', '،', '؛', '؟',
    # Zero-width and invisible characters
    '\u200b', '\u200c', '\u200d', '\u200e', '\u200f',
    '\ufeff', '\u00a0', '\u202a', '\u202b', '\u202c', '\u202d', '\u202e',
}

NAME_VARIATIONS = {
    # Mohamed variants
    "mohammed": "mohamed", "mohamad": "mohamed", "muhammad": "mohamed",
    "mohammad": "mohamed", "muhamed": "mohamed", "muhammed": "mohamed",
    "muhamad": "mohamed", "mouhammad": "mohamed", "mohammod": "mohamed",
    "محمد": "mohamed", "محمود": "mahmud",
    # Ahmed variants
    "ahmad": "ahmed", "ahmmed": "ahmed", "ahmet": "ahmed",
    "ahmead": "ahmed", "احمد": "ahmed",
    # Other common variations
    "mahmoud": "mahmud", "mahmood": "mahmud", "mahmod": "mahmud",
    "hussein": "husein", "hossein": "husein", "husain": "husein", "hussain": "husein",
    "hasan": "hassan", "haasan": "hassan", "حسن": "hassan", "حسان": "hassan",
    "osama": "usama", "ousama": "usama", "اسامة": "usama", "أسامة": "usama",
    "uthman": "othman", "osman": "othman", "عثمان": "othman",
    "ibrahim": "ibrahim", "ibraheem": "ibrahim", "ابراهيم": "ibrahim", "إبراهيم": "ibrahim",
    "youssef": "yousef", "yusuf": "yousef", "youssif": "yousef", "يوسف": "yousef",
}
