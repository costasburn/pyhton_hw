import re

print("*" * 20)
print("Task 4")
print("*" * 20)
def multiplication_odd_numbers():
    user_number = input("Enter 5-digit number: ")
    if user_number.isnumeric() and len(user_number) == 5:
        result = 1
        for digit in user_number:
            if int(digit) % 2 != 0:
                result *= int(digit)
        print(result)
    else:
        print("Error")

multiplication_odd_numbers()

print("*" * 20)
print("Task 5")
print("*" * 20)

def which_is_closer():
    user_number_one = input("Enter any number: ")
    user_number_two = input("Enter another number: ")
    if user_number_one.isnumeric() and user_number_two.isnumeric():
        if abs(int(user_number_one) - 10) < abs(int(user_number_two) - 10):
            print(user_number_one)
        elif abs(int(user_number_one) - 10) == abs(int(user_number_two) - 10):
            print("They are equal")
        else:
            print(user_number_two)

    else:
        print("Error")

which_is_closer()

print("*" * 20)
print("Task 6")
print("*" * 20)

def is_isogram(text):
    letters = sorted(re.findall(r"\w", text))
    temp_letter = letters[0]
    for letter in letters[1:]:
        if temp_letter == letter:
            return False
        else:
            temp_letter = letter
    return True


text = "Бесплатный сервис Google позволяет мгновенно переводить слова"
print(is_isogram(text))
