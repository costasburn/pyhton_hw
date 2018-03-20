import pickle


running = True

# ------------------------------------------------------------------------------
phone_book = [
    {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
    {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
]
standard_lenght = 4




#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    if len(entry) > standard_lenght:
        list_entry = list(entry)
        quantity_of_extra_fields = len(entry) % standard_lenght
        for i in range(quantity_of_extra_fields):
            print("| %s:   %20s |" % (list_entry[standard_lenght + i], entry[list_entry[standard_lenght + i]]))
    print ()


#------------------------------------------------------------------------------
def print_phonebook(phone_book_to_print= phone_book):
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book_to_print:
        print_entry(number, entry)
        number += 1

#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

#------------------------------------------------------------------------------
def find_by_additional_info():
    search_info = input("    Enter additional info to search by: ")
    idx = 1
    found = False
    for entry in phone_book:
        if len(entry) > standard_lenght:
            extra_length = len(entry) % standard_lenght
            list_entry = list(entry)
            for i in range(extra_length):
                if entry[list_entry[standard_lenght + i]] == search_info:
                    print_entry(idx, entry)
                    idx += 1
                    found = True
    if not found:
        printError("Not found!!")



#------------------------------------------------------------------------------
def delete_entry_name_phonebook(phone_book_to_amend=phone_book):
    name = str(input("    Enter name of the contact you want to delete: "))
    phone_book = [entry for entry in phone_book_to_amend if entry["name"] != name]
    print_phonebook(phone_book)



#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    sorted_phone_book = sorted(phone_book, key=lambda entry: entry['age'])
    print_phonebook(sorted_phone_book)

    #------------------------------------------------------------------------------
def increase_age(phone_book_to_amend=phone_book):
    years_to_add = int(input("Enter how many years to add to each of your contacts: "))
    for entry in phone_book:
        new_age = years_to_add + entry['age']
        entry.update(age=new_age)
    print_phonebook()

def add_contact_info():
    search_name = input("Enter the name: ")
    found = False
    for entry in phone_book:
        if entry['name'] == search_name:
            found = True
            type_of_info = input("Enter type of info you want to add: ")
            contact_info = input("Enter specific info: ")
            entry[type_of_info] = contact_info
            print_phonebook()
    if not found:
            print("Not found!!")

#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    total_age = 0
    for entry in phone_book:
        total_age += entry["age"]
    average_age = total_age / len(phone_book)
    print("Average age of your phonebook contacts: ", average_age)


#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
    global running
    running = False


#------------------------------------------------------------------------------
def print_prompt():
    print()
    print()
    print()
    print("~ Welcome to phonebook ~")
    print("Select one of actions below:")
    print("     1 - Print phonebook entries")
    print("     2 - Print phonebook entries (by age)")
    print("     3 - Add new entry")
    print("     4 - Find entry by name")
    print("     5 - Find entry by age")
    print("     6 - Delete entry by name")
    print("     7 - The number of entries in the phonebook")
    print("     8 - Avr. age of all persons")
    print("     9 - Increase age by num. of years")
    print("     10 - Add info")
    print("     11 - Find by additional info")
    print("-----------------------------")
    print("     s - Save to file")
    print("     l - Load from file")
    print("     0 - Exit")
    print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                '1':  print_phonebook,
                '2':  print_phonebook_by_age,
                '3':  add_entry_phonebook,
                '4':  find_entry_name_phonebook,
                '5':  find_entry_age_phonebook,
                '6':  delete_entry_name_phonebook,
                '7':  count_all_entries_in_phonebook,
                '8':  avr_age_of_all_persons,
                '9':  increase_age,
                '10': add_contact_info,
                '11': find_by_additional_info,

                '0':  exit,
                's':  save_to_file,
                'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
