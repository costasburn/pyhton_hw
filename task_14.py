def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


number = int(input("Please enter the number you want to test: "))

if is_even(number):
    print("Number '{}' is even.".format(number))
else:
    print("Number '{}' isn't even.".format(number))
commit