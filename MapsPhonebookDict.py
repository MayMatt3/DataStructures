phonebook = {}

def add_entry(name, phone_number):
    phonebook[name] = phone_number
    return

def search_entry(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("entry not found")

def delete_entry(name):
    phonebook.pop(name)
    return



add_entry("Sam", "123-456-7890")
add_entry("Emily", "987-654-3210")
add_entry("Henry", "321-654-0987")
add_entry("David", "682-440-0200")
print("After adding entries :", phonebook)
search_entry("Henry")
delete_entry("Sam")
print("After deleting entry :", phonebook)