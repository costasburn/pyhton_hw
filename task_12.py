def sum_of_digits(number):
    iterator_number = iter(number)
    result = 0
    result += int(next(iterator_number)) + int(next(iterator_number)) + int(next(iterator_number))
    return result


number = str(input("Please enter any 3-digit number to calculate a sum of its digits: "))


print("The sum of the digits of above mentioned number is {}".format(sum_of_digits(number)))