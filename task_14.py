def is_even(number):
    if (number % 2) == 0:
        return 1
    else:
        return None


number = int(input("Please enter the number you want to test: "))

if is_even(number):
    print("Number '{}' is even.".format(number))
else:
    print("Number '{}' isn't even.".format(number))
