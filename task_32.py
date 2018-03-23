import csv
titanic = r'C:\Users\Konstantin\IdeaProjects\pyhton_hw\titanic_data.csv'

def get_data_from_csv(path):
    with open(path, "r") as f:
        list_dicts = [row for row in csv.DictReader(f)]
    return list_dicts


titanic_data = get_data_from_csv(titanic)


def distribution_of_survivals(titanic_data, field_name):
    # finding quontity of groups in the field
    list_of_groups_with_dublicates = []
    for passanger in titanic_data:
        list_of_groups_with_dublicates.append(passanger[field_name])
    list_of_groups = sorted(list(set(list_of_groups_with_dublicates)))

    # finding total persons in each group
    total = []
    for group in list_of_groups:
        group = []
        total.append(group)
    for passanger in titanic_data:
        for idx in range(len(list_of_groups)):
            if passanger[field_name] == list_of_groups[idx]:
                total[idx].append(passanger)

    # finding survivals in each group
    survived = list(total)
    for i in range(len(list_of_groups)):
        temp_var = [passanger for passanger in total[i] if passanger["Survived"] == "1"]
        survived[i] = temp_var

    # comparing and printing out
    for i in range(len(list_of_groups)):
        percentage_survived = (len(survived[i]) / len(total[i])) * 100
        print("Among {} {}: {}% of people survived".format(field_name, list_of_groups[i], percentage_survived))






field_name = "Age"
distribution_of_survivals(titanic_data, field_name)