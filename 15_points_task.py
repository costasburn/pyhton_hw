import random

def after_summer_test(quantity_of_problems_to_generate):
    temp_list = []
    result_list = []
    # generating multiplication table
    for x in range(2, 10):
        for y in range(2, 10):
            temp_list.append([x, y])
    # removing duplicates from generated table
    for problem in temp_list:
        for problem_to_compare in temp_list:
            if (problem[0], problem[1]) == (problem_to_compare[1], problem_to_compare[0]) and problem[0] != problem[1]:
                temp_list.remove(problem)
    # choosing 15 random problems from the table
    for _ in range(quantity_of_problems_to_generate):
        result_list.append(random.choice(temp_list))
    # printing out
    for problem in result_list:
        print("{} x {} = ?".format(problem[0], problem[1]))
    return result_list



after_summer_test(15)