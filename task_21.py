import random


def get_max_digit(number):
    converted_digit = list(str(number))
    return max(converted_digit)


number = random.randint(100000000000, 999999999999)

print(get_max_digit(number))
