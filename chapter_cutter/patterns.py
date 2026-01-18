import re

# Patterns keyed by normalized language name (lowercase English names)
PATTERNS = {
    'spanish': [
        r'^\s*(cap[ií]tulo)\b',
        r'^\s*(cap[ií]tulo)\s+\d+',
    ],
    'english': [
        r'^\s*(chapter)\b',
        r'^\s*(chapter)\s+\d+',
    ],
    'french': [
        r'^\s*(chapitre)\b',
    ],
    'german': [
        r'^\s*(kapitel)\b',
    ],
    'italian': [
        r'^\s*(capitolo)\b',
    ],
    'portuguese': [
        r'^\s*(cap[ií]tulo)\b',
    ],
    'russian': [
        r'^\s*(глава)\b',
    ],
    'chinese': [
        r'^\s*(第[^\n]{1,20}章)',
    ],
    'japanese': [
        r'^\s*(第[^\n]{1,20}章)',
    ],
    'korean': [
        r'^\s*(제\s*\d+\s*장)',
        r'^\s*(제\s*[IVXLCM]+\s*장)',
    ],
}

def get_patterns(lang_name):
    if not lang_name:
        return []
    key = lang_name.strip().lower()
    return [re.compile(p, re.IGNORECASE) for p in PATTERNS.get(key, [])]
