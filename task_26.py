import random


def calc_frequency(lst):
    counted_list = []
    counted_list.append(lst.count(-1))
    counted_list.append(lst.count(0))
    counted_list.append(lst.count(0))
    counted_list = sorted(counted_list)
    if counted_list[2] != counted_list[1]:
        return counted_list[2]
    else:
        return None


lst = []
for i in range(11):
    lst.append(random.randint(-1, 1))

print(calc_frequency(lst))
