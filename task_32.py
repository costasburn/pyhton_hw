import csv

titanic = r'C:\Users\Konstantin\IdeaProjects\pyhton_hw\titanic_data.csv'


def get_data_from_csv(path):
    with open(path, "r") as f:
        list_dicts = [row for row in csv.DictReader(f)]
    return list_dicts


titanic_data = get_data_from_csv(titanic)


def distribution_of_survivals(titanic_data, field_name):
    totals = {}
    survived = {}

    for person in titanic_data:
        totals[person[field_name]] = totals.get(person[field_name], 0) + 1
        if person["Survived"] == "1":
            survived[person[field_name]] = survived.get(person[field_name], 0) + 1

    for key_survived, value_survived in survived.items():
        print(
            "Survival rate in %s %s: %.2f%%" % (field_name, key_survived, value_survived / totals[key_survived] * 100))


field_name = "Pclass"
distribution_of_survivals(titanic_data, field_name)
