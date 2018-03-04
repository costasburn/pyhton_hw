def sum_of_digits(number):
    digit_1 = number // 100
    digit_2 = (number % 100) // 10
    digit_3 = ((number % 100) % 10) // 1
    result = digit_1 + digit_2 + digit_3
    return result


number = int(input("Please enter any 3-digit number to calculate a sum of its digits: "))


print("The sum of the digits of above mentioned number is {}".format(sum_of_digits(number)))
