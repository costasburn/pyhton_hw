import random

print("*" * 20)
print("Task 10")
print("*" * 20)

def generate_matrix(rows, columns, lower_limit, upper_limit):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(lower_limit, upper_limit) for _ in range(columns)])
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        print()
        for elem in matrix[i]:
            print("%3d" % (elem), end=" ")
    print()

def find_base_elem(matrix):
    print()
    base_elem_coord_list = []
    for i in range(len(matrix)):
        base_elem_coord = []
        min_val = min(matrix[i])
        index_min_val = matrix[i].index(min_val)
        column_list = []
        for j in range(len(matrix)):
            column_list.append(matrix[j][index_min_val])
        if min_val is max(column_list):
            base_elem_coord.append(i)
            base_elem_coord.append(matrix[i].index(min_val))
            base_elem_coord_list.append(base_elem_coord)
    return base_elem_coord_list


new_matrix = generate_matrix(3, 3, -5, 5)
print_matrix(new_matrix)
print(find_base_elem(new_matrix))

print("*" * 20)
print("Task 11")
print("*" * 20)

matrix_task_11 = generate_matrix(5, 5, -100, 100)

def sort_matrix(matrix):
    print_matrix(matrix)
    for column in range(len(matrix[0])):
        list_of_column_elems = []
        for row in range(len(matrix)):
            list_of_column_elems.append(matrix[row][column])
        if column % 2 == 0:
            list_of_column_elems = sorted(list_of_column_elems)
        else:
            list_of_column_elems = sorted(list_of_column_elems, reverse=True)
        for row in range(len(matrix)):
            matrix[row][column] = list_of_column_elems[row]
    print()
    print_matrix(matrix)


sort_matrix(matrix_task_11)