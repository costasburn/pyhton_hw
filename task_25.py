from random import random

def shuffle_list(list_to_shuffle):
    shuffled_list = sorted(list_to_shuffle, key=lambda x: random())
    print(shuffled_list)

list_to_shuffle = []
for i in range(0, 100):
    if i % 2 != 0:
        list_to_shuffle.append(i)

shuffle_list(list_to_shuffle)