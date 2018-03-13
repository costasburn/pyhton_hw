import random
from collections import Counter


def calc_frequency(lst):
    counted_lst = Counter(lst)
    if counted_lst[0] == counted_lst[1] or counted_lst[0] == counted_lst[2] or counted_lst[1] == counted_lst[2]:
        return None
    elif lst.count(-1) > lst.count(0) and lst.count(-1) > lst.count(1):
        return -1
    elif lst.count(0) > lst.count(-1) and lst.count(0) > lst.count(1):
        return 0
    elif lst.count(1) > lst.count(-1) and lst.count(1) > lst.count(0):
        return 1


lst = []
for i in range(11):
    lst.append(random.randint(-1, 1))

print(calc_frequency(lst))
