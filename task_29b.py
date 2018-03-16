import random
from string import ascii_lowercase, ascii_uppercase, digits


def gen_password():
    def generate_new_password():
        password = ''
        for password_symbol in range(password_length):
            password += random.choice(ascii_lowercase + ascii_uppercase + digits + encrypt_list_symbols)
        return password

    encrypt_list_symbols = '_'
    password_length = 8

    def check_password_for_obligatory_symbols(password):
        for password_symbol in password:
            for lowercase_symbol in ascii_lowercase:
                if password_symbol == lowercase_symbol:
                    for password_symbol in password:
                        for uppercase_symbol in ascii_uppercase:
                            if password_symbol == uppercase_symbol:
                                for password_symbol in password:
                                    for digit in digits:
                                        if password_symbol == digit:
                                            return password
    result = check_password_for_obligatory_symbols(generate_new_password())
    while result is None:
        result = check_password_for_obligatory_symbols(generate_new_password())
    return result


print(gen_password())
