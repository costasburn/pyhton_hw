import random


def calc_frequency(lst):
    if lst.count(0) == lst.count(1) or lst.count(0) == lst.count(-1) or lst.count(1) == lst.count(-1):
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
