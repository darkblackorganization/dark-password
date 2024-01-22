import secrets
import string

print("""\033[94m

   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
   #                                               _       #
   #                                              | |      #
   #    _ __   __ _ ___ ___ __      _____  _ __ __| |      #
   #   | '_ \ / _` / __/ __ \ \ /\ / / _ \| '__/ _` |      #
   #   | |_) | (_| \__ \__ \ \ V  V / (_) | | | (_| |      #
   #   | .__/ \__,_|___/___/  \_/\_/ \___/|_|  \__,_|      #
   #   | |                                                 #
   #   |_|                                                 #
   #                                                       #
   #                  \033[91mcode by DARK_BLACK\033[0m\033[94m                   #
   #                                                       #
   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\033[0m

        【A】【n】【o】【n】【y】【m】【o】【u】【s】

""")

def generate_password(length, characters):
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Get user input for the password length
try:
    password_length = int(input("\033[91m\nEnter password length:\033[0m "))
except ValueError:
    print("\033[92mPlease enter a valid integer for the password length.\033[0m")
    exit()

# Get user input for the types of characters
character_types = input(" \033[93ml for lowercase\n u for uppercase\n d for digits\n p for punctuation\n\033[0m \033[91mEnter the characters>")

f = input("\033[93mEnter file name:\033[0m ")

valid_characters = ""
if 'l' in character_types:
    valid_characters += string.ascii_lowercase
if 'u' in character_types:
    valid_characters += string.ascii_uppercase
if 'd' in character_types:
    valid_characters += string.digits
if 'p' in character_types:
    valid_characters += string.punctuation

if not valid_characters:
    print("\033[92mPlease select at least one character type.\033[0m")
    exit()

number_of_passwords = 100000

passwords = [generate_password(password_length, valid_characters) for _ in range(number_of_passwords)]

file_path = f"{f}"

with open(file_path, 'w') as file:
    for password in passwords:
        file.write(f"{password}\n")

print(f"\033[92mPasswords saved to:\033[0m \033[38;5;208m{file_path}\033[0m")

