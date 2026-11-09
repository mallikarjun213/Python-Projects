
employees = []


def add_employee(name):
    if name == "":
        print("please enter a name")
    elif not name.isalpha():
        print("Enter alphabets only")

    elif name in employees:
        print("Employee already exists")
    else:        
        employees.append(name)
        print("Employee added successfully")

def view_employees():
    if not employees:
        print("No employees found")
    else:
        print("Employee list")
        for index , name in enumerate(employees, start=1):
            print(f"{index}. {name}")

def search_employee(name):
    if name == "":
        print("please enter employee name")

    elif not name.isalpha():
        print("please enter alphabets only")

    elif name in employees:
        print(f"{name} - found" )

    else:
        print("Employee not found")

def update_employee(old_name , new_name):
    if old_name == "" or new_name == "":
        print("Please enter the employee name")

    elif not old_name.isalpha() or not new_name.isalpha():
        print("Please enter the alphabets only")

    elif old_name == new_name:
        print("Entered same named employee name")

    elif new_name in employees:
        print("Employee already exists")

    elif old_name in employees:
        index = employees.index(old_name)
        employees[index] = new_name
        print("Employee updated successfully")

    else:
        print("Employee not found")

def delete_employee(name):
    if name == "":
        print("Please enter employee name")

    elif not name.isalpha():
        print("Please enter alphabets only")

    elif name in employees:
        employees.remove(name)
        print("Employee deleted successfully")
    else:
        print("Employee not found")




def main():
    while True:
        print("\n Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            employee_add = input("Enter the employee name: ").strip().lower()
            add_employee(employee_add)
       
        elif choice == "2":
            view_employees()

        elif choice == "3":
            employee_search = input("Enter the employee name: ").strip().lower()
            search_employee(employee_search)
      
        elif choice == "4":
            employee_old_name = input("Enter the employee old name: ").strip().lower()
            employee_new_name = input("Enter the employee new name: ").strip().lower()
            update_employee(employee_old_name , employee_new_name)
               
        elif choice == "5":
            employee_delete = input("Enter the employee name: ").strip().lower()
            delete_employee(employee_delete)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

    

main()





