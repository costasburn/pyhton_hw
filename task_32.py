import csv

# persons = [
#     {'name': 'Alice', 'age': 23, 'gender': 'f'},
#     {'name': 'Bob', 'age': 22, 'gender': 'm'},
#     {'name': 'Stacy', 'age': 33, 'gender': 'f'},
#     {'name': 'Clark', 'age': 43, 'gender': 'm'},
#     {'name': 'Bill', 'age': 42, 'gender': 'm'}]
#
# totals = {}
# field = 'gender'
# for person in persons:
#     totals[person[field]] = totals.get(person[field], 0) + 1
#
#
# print('Gender distribution:')
# for k, v in totals.items():
#     print('%s: %.2f%%' % (k, v / len(persons) * 100))



titanic = r'C:\Users\Konstantin\IdeaProjects\pyhton_hw\titanic_data.csv'

def get_data_from_csv(path):
    with open(path, "r") as f:
        list_dicts = [row for row in csv.DictReader(f)]
    return list_dicts


titanic_data = get_data_from_csv(titanic)


def distribution_of_survivals(titanic_data, field_name):
    totals = {}
    for person in titanic_data:
        totals[person[field_name]] = totals.get(person[field_name], 0) + 1


    survived = {}
    for person in titanic_data:
        if person["Survived"] == "1":
            survived[person[field_name]] = survived.get(person[field_name], 0) + 1


    for key_total, value_total in totals.items():
        for key_survived, value_survived in survived.items():
            if key_total == key_survived:
                print("Survival rate in %s %s: %.2f%%" % (field_name, key_total, value_survived / value_total * 100))






field_name = "Pclass"
distribution_of_survivals(titanic_data, field_name)