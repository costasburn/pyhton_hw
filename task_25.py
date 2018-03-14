import random

def shuffle_list(list_to_shuffle):
    repeat = random.randint(2, 100)
    while repeat > 0:
        for i in range(1, len(list_to_shuffle)):
            for j in range(1, len(list_to_shuffle) - i):
                temp = list_to_shuffle[i]
                list_to_shuffle[i] = list_to_shuffle[j]
                list_to_shuffle[j] = temp
        repeat -= 1
    return list_to_shuffle


list_to_shuffle = []
for i in range(0, 100):
    if i % 2 != 0:
        list_to_shuffle.append(i)

print(shuffle_list(list_to_shuffle))
