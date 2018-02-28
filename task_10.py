data = "Marcus Aurelius*121-04-26*180-03-17"

name, date_born, date_died = data.split("*")
born_year, born_month, born_day = date_born.split("-")
died_year, died_month, died_day = date_died.split("-")

new_born_year = int(born_year)
new_born_month = int(born_month)
new_born_day = int(born_day)
new_died_year = int(died_year)
new_died_month = int(died_month)
new_died_day = int(died_day)


if new_died_month - new_born_month > 0 or new_died_month - new_born_month == 0 and (new_died_day - new_born_day >= 0):
    age = new_died_year - new_born_year
else:
    age = new_died_year - new_born_year - 1

print(name + ", ", age)