""" Pedro is developing a registration system and needs to generate secure passwords for
 users. He wants a program that creates random passwords containing uppercase letters, 
 lowercase letters, numbers, and special characters.

Create a program that generates a random 12-character password containing at least one 
uppercase letter, one lowercase letter, one number, and one special character. Display 
the generated password.

Expected output:
Generated password: A1b@C3d$E5f& """

import random
import string


def generate_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]

    all_characters = uppercase + lowercase + numbers + special

    PASSWORD_LENGTH = 12

    password.extend(random.choices(all_characters, k=PASSWORD_LENGTH - len(password)))

    random.shuffle(password)

    return "".join(password)

print(f"Generated password: {generate_password()}")