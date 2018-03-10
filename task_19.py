import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    random_list_of_numbers = []

    for i in range(0, num_limit):
        random_list_of_numbers.append(random.randrange(lower_bound, upper_bound, 1))

    highest = max(random_list_of_numbers)
    lowest = min(random_list_of_numbers)

    result = highest - lowest
    return result




print(diff_min_max(5, 1, 20))
