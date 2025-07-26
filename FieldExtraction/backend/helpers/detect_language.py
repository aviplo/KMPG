from classes.languages import Language

def detect_primary_language(lines):
    hebrew_count = 0
    english_count = 0

    for line in lines:
        heb_chars = sum(1 for c in line.content if '\u0590' <= c <= '\u05FF')
        eng_chars = sum(1 for c in line.content if c.isascii() and c.isalpha())

        if heb_chars > eng_chars:
            hebrew_count += 1
        elif eng_chars > heb_chars:
            english_count += 1

    if hebrew_count > english_count:
        return Language.HEBREW
    elif english_count > hebrew_count:
        return Language.ENGLISH
    else:
        return "unknown"