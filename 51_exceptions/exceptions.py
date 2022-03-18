# Understanding Exceptions
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

x = -1


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError):
        pass  # pass is a no-op i.e. does nothing. It is to construct empty blocks to avoid runtime errors
    return x


convert("one three around grillion".split())

convert("one three three two".split())

convert(512)

convert("elephant".split())
