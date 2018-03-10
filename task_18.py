def sum_symbol_codes(first, last):
    num_first = ord(first)
    num_last = ord(last)
    result = 0
    for i in range(num_first, (num_last+1)):
        result += i
    return result


print(sum_symbol_codes("e", "l"))
