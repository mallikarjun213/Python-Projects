
contacts = []


def add_contact(name , phone):
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            return "Contact Already Exists"

        if contact["Phone"] == phone:
            return "Phone Number Already Exists"
    
    contact = {"Name" : name,
                "Phone" : phone
                }

    contacts.append(contact)
    return "Contact Added Successfully"

def view_contact():
    if not contacts:
        print("No Contacts  Found")
        return
    for index , contact in enumerate(contacts, start= 1):
        print(f"{index}. {contact['Name']} :- {contact['Phone']}")


def search_contact(search_name):
    for contact in contacts:
        if contact["Name"].lower() == search_name.lower():
            print("Contact Found")
            print(contact["Name"], contact["Phone"])
            return 

    print("Contact Not Found")


def delete_contact(delete_name):
    for index, contact in enumerate(contacts):
        if contact["Name"].lower() == delete_name.lower():
            del contacts[index]
            return "Contact Deleted Successfully"
    return "Contact Not Found"

def update_contact(old_name , new_name , new_phone):
    for contact in contacts:
        if contact["Name"].lower() == old_name.lower():

            for existing in contacts:
                if existing is not contact:
                    if existing["Name"].lower() == new_name.lower():
                        return "Name Already Exists"

                    if existing["Phone"] == new_phone:
                        return "Phone Number Already Exists"
            
            contact["Name"] = new_name
            contact["Phone"] = new_phone
            return "Contact Updated Successfully"
    return "Contact not found"



def main_menu():
    while True:
        print("\n ====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")


        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter Name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            phone = input("Enter Phone: ").strip()
            if not phone.isdigit():
                print("Please Enter digits only")
                continue
            
            print(add_contact(name , phone))

        elif choice == "2":
            view_contact()


        elif choice == "3":
            name = input("Enter Search Name: ").strip()
            search_contact(name)

        elif choice == "4":
            name = input("Enter Delete Name: ").strip()
            print(delete_contact(name))

        elif choice == "5":
            old_name = input("Enter old name: ").strip()
            new_name = input("Enter new name: ").strip()

            if not old_name or not new_name:
                print("Name cannot be empty")
                continue

            new_phone = input("Enter New Phone: ").strip()

            if not new_phone.isdigit():
                print("Please Enter digits only")
                continue

            print(update_contact(old_name , new_name , new_phone))


        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice")


main_menu()
