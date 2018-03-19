def gen_primes(lower_limit, upper_limit):
    prime_numbers = []
    for i in range(lower_limit, upper_limit + 1):
        for j in range(2, i):
            if i % j == 0 and j == i // 2:
                break
            if j == i - 1:
                prime_numbers += [i]
    return prime_numbers


print(gen_primes(1, 20))