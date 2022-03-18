# Understanding Exceptions
import sys
from math import log

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


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        pass  # pass is a no-op i.e. does nothing. It is to construct empty blocks to avoid runtime errors
        # return -1
        raise  # re raise the current exception


# convert("one three around grillion".split())
# print(convert("one three three two".split()))
# convert(512)
# convert("elephant".split())

def string_log(s):
    v = convert(s)
    return log(v)


# string_log("ouch!".split())

string_log("two five".split())

# string_log(235)
string_log("tw".split())
