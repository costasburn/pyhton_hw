import random

def shuffle_list(list_to_shuffle):
    for i in range(len(list_to_shuffle)):
        k = random.randint(0, len(list_to_shuffle)-1)
        list_to_shuffle[k] = list_to_shuffle[i]
    return list_to_shuffle

list_to_shuffle = []
for i in range(0, 100):
    if i % 2 != 0:
        list_to_shuffle.append(i)

print(shuffle_list(list_to_shuffle))
