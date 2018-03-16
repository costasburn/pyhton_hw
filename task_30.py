def gen_primes(lower_limit, upper_limit):
    prime_numbers = []
    for i in range(lower_limit, upper_limit + 1):
        for j in range(1, i):
            if i % j == 0 and j != 1:
                break
            if j == i - 1:
                prime_numbers += [i]
    return prime_numbers


print(gen_primes(1, 20))