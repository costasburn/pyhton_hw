import math

def gen_primes(lower_limit, upper_limit):
    prime_numbers = []
    for i in range(lower_limit, upper_limit + 1):
        for j in range(1, i):
            print("{} / {}".format(i, j))
            if i % j == 0 and j != 1:
                print("Break")
                break
            elif j == i - 1 or j == math.ceil(math.sqrt(i)): #alternative condition j == (i - 1) / 2
                prime_numbers += [i]
                print("Found")
                break
    return prime_numbers


print(gen_primes(1, 100))
