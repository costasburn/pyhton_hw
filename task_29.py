import math
import random
from string import ascii_lowercase, ascii_uppercase, digits


def gen_password():
    encrypt_list_symbols = '_'
    password_length = 8
    password = ''
    quantity_letter_symbols = 0
    reserve_for_title_and_digits = 2
    while quantity_letter_symbols < 1 or password_length - quantity_letter_symbols < reserve_for_title_and_digits:
        quantity_letter_symbols = round(random.random() * password_length)
    print("Quantity of letter symbols: ", quantity_letter_symbols)
    quantity_title_symbols = 0
    while quantity_title_symbols < 1 or password_length - quantity_title_symbols - quantity_letter_symbols == 0:
        quantity_title_symbols = round(random.random() * (password_length - quantity_letter_symbols))
    print("Quantity of title symbols: ", quantity_title_symbols)
    quantity_digits_symbols = 0
    while quantity_digits_symbols < 1:
        quantity_digits_symbols = math.ceil(
            random.random() * (password_length - quantity_title_symbols - quantity_letter_symbols))
    print("Quantity of digits symbols: ", quantity_digits_symbols)
    quantity_symbol = max(0,
                          password_length - quantity_letter_symbols - quantity_title_symbols - quantity_digits_symbols)
    print("Quantity of symbols: ", quantity_symbol)

    quotas = [quantity_letter_symbols, quantity_title_symbols, quantity_digits_symbols, quantity_symbol]
    symb_sources = [ascii_lowercase, ascii_uppercase, digits, encrypt_list_symbols]

    for i, quota in enumerate(quotas):
        for _ in range(quota):
            password += random.choice(symb_sources[i])

    print("Sorted password: ", password)
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print("Shuffled password: ", password)
    return password


gen_password()
