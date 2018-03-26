import random

print("*" * 20)
print("Task 7")
print("*" * 20)


def fibonacci(f1, f2, list_fib):
    number_limit = 10
    f3 = f1 + f2
    list_fib.append(f3)
    if len(list_fib) == number_limit:
        print(list_fib)
        return sum(list_fib)
    f1, f2 = f2, f3
    return fibonacci(f1, f2, list_fib)


first_fibanacci_number = 0
second_fibanacci_number = 1
list_fibanacci_number =[first_fibanacci_number, second_fibanacci_number]
print(fibonacci(first_fibanacci_number, second_fibanacci_number, list_fibanacci_number))

print("*" * 20)
print("Task 8")
print("*" * 20)

def swap_max_min(lower_limit, upper_limit, quantity_of_numbers):
    random_list = [random.randint(lower_limit, upper_limit) for _ in range(quantity_of_numbers)]
    print(random_list)
    max_num_index = random_list.index(max(random_list))
    min_num_index = random_list.index(min(random_list))
    max_num = max(random_list)
    min_num = min(random_list)
    random_list[max_num_index], random_list[min_num_index] = min_num, max_num
    return random_list

print(swap_max_min(0, 100, 10))

print("*" * 20)
print("Task 9")
print("*" * 20)

def normilize_list(lower_limit, upper_limit, quantity_of_numbers):
    random_list = [random.randint(lower_limit, upper_limit) for _ in range(quantity_of_numbers)]
    print(random_list)
    norm_range = range(-1, 1)
    max_list_value = max(abs(max(random_list)), abs(min(random_list)))
    max_range_value = max(abs(list(norm_range)[-1]), abs(list(norm_range)[0]))
    ratio = max_range_value / max_list_value
    normalized_list = [elem * ratio for elem in random_list]
    return normalized_list

print(normilize_list(-5, 5, 5))