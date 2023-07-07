import re

CYRILLIC_SYMBOLS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "g",
    "d",
    "e",
    "ie",
    "zh",
    "z",
    "y",
    "i",
    "i",
    "i",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "kh",
    "ts",
    "ch",
    "sh",
    "shch",
    "",
    "yu",
    "ia",
)

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    right_name = name.translate(TRANS)
    right_name = re.sub(r"\W", "_", right_name)
    return right_name

