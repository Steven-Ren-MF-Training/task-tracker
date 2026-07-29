terminate_program = False


#dictionary used to store user detail as dictionary
contacts = {"0412345678":"Steven","04555666777":"Sam","0412309876":"Logan"}
def display_options():
    print("Please Enter your option:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contact")
    print("6. EXIT")
    print("Please Enter your option:")

def add_contact(contacts,contact_ph,contact_name):
    contacts[contact_ph] = contact_name

def display_contact(contacts):
    print("Here is current contact table")
    for phone, name in contacts.items():
        print(phone, name)

def update_contact(contacts,old_phone):
    print("Please enter your option to update conatct")
    print("1. Change both name and phone number")
    print("2. Change phone number only")
    print("3. Change name only")
    choice = input("Choose an option: ")
    if choice == "1":
        new_name = input("Enter the new name: ")
        new_phone = input("Enter the new phone number: ")

        contacts[new_phone] = new_name
        del contacts[old_phone]
        print("Name and phone number updated successfully.")

    elif choice == "2":
        new_phone = input("Enter the new phone number: ")
        old_name = contacts[old_phone]
        contacts[new_phone] = old_name
        del contacts[old_phone]
        print("Phone number updated successfully.")

    elif choice == "3":
        new_name = input("Enter the new name: ")
        contacts[old_phone] = new_name

        print("Name updated successfully.")

    else:
        print("Invalid option.")

def delete_contact(contacts,phone):
    del contacts[phone]
    print("Contact was deleted  successfully.")

# Try-except handling is included for future integration with external data sources.
def search_contact(contacts,phone):
    phone_exist = True
    try:
        if phone in contacts:
            print(phone,contacts[phone])
        else:
            phone_exist = False
            raise KeyError
    except KeyError:
            print("Phone number not found")
    return phone_exist

while not terminate_program:
    display_options()
    option_selected = input("Please Enter Option 1-6: ")
    if option_selected == "6":
        print("Thanks for using the program!")
        terminate_program = True
    elif option_selected == "1":
        new_phone = input("please enter new contact phone:")
        new_name = input("please enter new contact name:")
        add_contact(contacts,new_phone,new_name)
        display_contact(contacts)
    elif option_selected == "2":
        search_ph = input("Please enter the phone number to be searched:")
        search_contact(contacts,search_ph)
    elif option_selected == "3":
        search_ph = input("Please enter the phone number to be updated:")
        exist = search_contact(contacts,search_ph)
        if exist :
            update_contact(contacts,search_ph)
    elif option_selected == "4":
        search_ph = input("Please enter the phone number to be deleted:")
        exist =search_contact(contacts,search_ph)
        if exist :
            delete_contact(contacts,search_ph)
    elif option_selected == "5":
        display_contact(contacts)
    else:
        print("Invalid Option!")



