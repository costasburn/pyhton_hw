day = int(input("Please enter the day in dd format: "))
month = int(input("Please enter the month in mm format: "))
year = int(input("Please enter the year in yyyy format: "))
print("American format of the date: {}.{}.{}".format(month, day, year))
request = input("Would you like to format the date to EU standard Y/N: ")
if request == "Y":
    print("The date in EU format: {}.{}.{}".format(day, month, year))
else:
    print("The request has been declined")
