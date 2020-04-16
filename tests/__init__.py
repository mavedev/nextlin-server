import random
import string

__all__ = [
    'get_random_string'
]


def get_random_string() -> str:
    return ''.join(
        random.choices(string.ascii_uppercase, k=10)
    )
