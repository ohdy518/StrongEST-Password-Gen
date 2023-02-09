import string
import random


def generate_strong_password(length):
    # Ensure length is at least 8
    if length < 8:
        length = 8

    # Character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!?,;:."
    emojis = "❤️🤔😎🎉🎁🎂🎃🎄🎅🏻🎈🎉🎊🎌🏼🎍🎎🎏🎐🎑🎒🎓🎠🎡🎢🎣🎤🎥🎦🎧🎨🎩🎪🎫🎬🎭🎮🎯🎰🎱🎲🎳"

    # Generate the password
    password = random.sample(uppercase_letters, 2) + random.sample(lowercase_letters, 2) + random.sample(digits, 2)
    password = password + random.sample(special_characters, 1) + random.sample(emojis, 1)
    password = "".join(password)

    # Shuffle the password
    password = random.sample(password, len(password))

    # Add random characters to reach the desired length
    while len(password) < length:
        password.append(random.choice(uppercase_letters + lowercase_letters + digits + special_characters + emojis))

    # Return the password as a string
    return "".join(password)

# Get the password length from the user
password_length = int(input("Enter password length: "))

# Generate and print the password
print("Your strong password: ", generate_strong_password(password_length))
