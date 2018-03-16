import random
import math

def gen_password():
    encrypt_list = 'ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz0123456789_'
    encrypt_list_title = list(encrypt_list[encrypt_list.find("A"):encrypt_list.find('Z') + 1])
    encrypt_list_letter = list(encrypt_list[encrypt_list.find("a"):encrypt_list.find('z') + 1])
    encrypt_list_digits = list(encrypt_list[encrypt_list.find("0"):encrypt_list.find('9') + 1])
    encrypt_list_symbols = list(encrypt_list[encrypt_list.find("9") + 1:])
    password_length = 8
    password = ''
    quantity_letter_symbols = 0
    while quantity_letter_symbols < 1 or password_length - quantity_letter_symbols < 3:
        quantity_letter_symbols = round(random.random() * password_length)
    print("Quantity of letter symbols: ", quantity_letter_symbols)
    quantity_title_symbols = 0
    while quantity_title_symbols < 1 or password_length - quantity_title_symbols - quantity_letter_symbols == 0:
        quantity_title_symbols = round(random.random() * (password_length - quantity_letter_symbols))
    print("Quantity of title symbols: ", quantity_title_symbols)
    quantity_digits_symbols = 0
    while quantity_digits_symbols < 1:
        quantity_digits_symbols = math.ceil(random.random() * (8 - quantity_title_symbols - quantity_letter_symbols))
    print("Quantity of digits symbols: ", quantity_digits_symbols)
    quantity_symbol = 0
    if password_length - quantity_letter_symbols - quantity_title_symbols - quantity_digits_symbols != 0:
        quantity_symbol = password_length - quantity_letter_symbols - quantity_title_symbols - quantity_digits_symbols
        print("Quantity of symbols: ", quantity_symbol)

    for letter_symbol in range(quantity_letter_symbols):
        random_position = random.randint(0, len(encrypt_list_letter) - 1)
        password += encrypt_list_letter[random_position]
    print("Password with letters: ", password)

    for title_symbol in range(quantity_title_symbols):
        random_position = random.randint(0, len(encrypt_list_title) - 1)
        password += encrypt_list_title[random_position]
    print("Password with letters, titles: ", password)

    for digit_symbol in range(quantity_digits_symbols):
        random_position = random.randint(0, len(encrypt_list_digits) - 1)
        password += encrypt_list_digits[random_position]
    print("Password with letters, titles, digits: ", password)

    if quantity_symbol != 0:
        for symbol in range(quantity_symbol):
            random_position = random.randint(0, len(encrypt_list_symbols) - 1)
            password += encrypt_list_symbols[random_position]
        print("Password with letters, titles, digits, symbols: ", password)
    print("Sorted password: ", password)
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print("Shuffled password: ", password)
    return password

gen_password()