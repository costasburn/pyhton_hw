import random


def diff_even_odd(num_limit=100, lower_bound=1, upper_bound=100):
    random_list_of_numbers = []
    for i in range(num_limit):
        random_list_of_numbers.append(random.randint(lower_bound, upper_bound))

    even_list = []
    odd_list = []
    for i in random_list_of_numbers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    sum_even = 0
    for i in even_list:
        sum_even += i
    sum_odd = 0
    for i in odd_list:
        sum_odd += i

    result = sum_even - sum_odd
    return result


print(diff_even_odd())

