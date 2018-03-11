import random


def get_max_digit(number):
    converted_digit = list(str(number))
    return max(converted_digit)


number = random.randint(1e11, 1e12-1)

print(get_max_digit(number))
