import string
import random


def generate_username(length=9):
    letters = string.ascii_lowercase
    digits = string.digits
    return ''.join(random.choice(letters + digits) for _ in range(length))
