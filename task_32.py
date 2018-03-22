import csv
titanic = r'C:\Users\Konstantin\IdeaProjects\pyhton_hw\titanic_data.csv'

def get_data_from_csv(path):
    with open(path, "r") as f:
        list_dicts = [row for row in csv.DictReader(f)]
    return list_dicts


titanic_data = get_data_from_csv(titanic)

survived_list = []
survived_m = []
survived_w = []
survived_1class = []
survived_2class = []
survived_3class = []

total_m = []
total_w = []
total_1class = []
total_2class = []
total_3class = []

for passenger in titanic_data:
    if passenger["Survived"] == "1":
        survived_list.append(passenger)
for passenger in survived_list:
    if passenger["Sex"] == "male":
        survived_m.append(passenger)
    if passenger["Sex"] == "female":
        survived_w.append(passenger)
    if passenger["Pclass"] == "1":
        survived_1class.append(passenger)
    if passenger["Pclass"] == "2":
        survived_2class.append(passenger)
    elif passenger["Pclass"] == "3":
        survived_3class.append(passenger)

for passenger in titanic_data:
    if passenger["Sex"] == "male":
        total_m.append(passenger)
    if passenger["Sex"] == "female":
        total_w.append(passenger)
    if passenger['Pclass'] == "1":
        total_1class.append(passenger)
    if passenger["Pclass"] == "2":
        total_2class.append(passenger)
    elif passenger["Pclass"] == "3":
        total_3class.append(passenger)

men_survive_rate = (len(survived_m) / len(total_m)) * 100
print("{}% of men survived".format(men_survive_rate))

wmen_survive_rate = (len(survived_w) / len(total_w)) * 100
print("{}% of women survived".format(wmen_survive_rate))

first_class_survive_rate = (len(survived_1class) / len(total_1class) * 100)
print("{}% of first class survived".format(first_class_survive_rate))

second_class_survive_rate = (len(survived_2class) / len(total_2class) * 100)
print("{}% of second class survived".format(second_class_survive_rate))

third_class_survive_rate = (len(survived_3class) / len(total_3class) * 100)
print("{}% of third class survived".format(third_class_survive_rate))