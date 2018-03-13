import random
from collections import Counter


def calc_frequency(lst):
    newlist = Counter(lst)
    if newlist[0] == newlist[1] or newlist[0] == newlist[2] or newlist[1] == newlist[2]:
        return None
    else:
        return max(lst)


lst = []
for i in range(11):
    lst.append(random.randint(-1, 1))

print(calc_frequency(lst))
