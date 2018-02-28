name = str(input("Please enter your first name: "))
surname = str(input("Please enter your surname: "))

print("Hello, {} {}!".format(name, surname))
request = input("Would you like to swap your name? Y/N: ")
if request == "Y":
    print("Your new name is {} {}".format(surname, name))
else:
    print("your name remains unchanged.")
