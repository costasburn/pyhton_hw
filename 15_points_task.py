import random

def after_summer_test(quantity_of_problems_to_generate):
    temp_list = []
    result_list = []
    # generating multiplication table
    for x in range(2, 10):
        for y in range(2, 10):
            if (y, x) not in temp_list:
                temp_list.append((x, y))
    # choosing 15 random problems from the table
    for _ in range(quantity_of_problems_to_generate):
        result_list.append(random.choice(temp_list))
    # printing out
    for i, problem in enumerate(result_list):
        print("{}) {} x {} = ?".format(i + 1, problem[0], problem[1]))
    return result_list


after_summer_test(15)
