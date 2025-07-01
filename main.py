import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_specials=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    # Ensure at least one of each selected character type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_specials:
        password.append(random.choice(string.punctuation))
    password += random.choices(characters, k=length - len(password))

    random.shuffle(password)
    return ''.join(password)
