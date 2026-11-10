# Expense Tracker

expenses = []

def add_expense(name , amount):
    if amount <= 0:
        return "Invalid amount"

    for expense_name , expense_amount in expenses:
        if expense_name == name:
            return "Expense Already Exists"
    expenses.append((name , amount))
    return "Expense Added Successfully"



def calculate_total():
    total = 0
    for name , amount in expenses:
        total += amount
       
    return total 

def view_expenses():
    found = False
    for name , amount in expenses:
        print(name , amount)
        found = True


    if not found:
        print("No Expenses Found")


def search_name(name_search):
    found = False
    for name , amount in expenses:
        if name == name_search:
            print(name , amount)
            found = True

    if not found:
        print("Expense Not Found")


def delete_expense(delete_name):

    for index , (name , amount) in enumerate(expenses):
        if name == delete_name:
            del expenses[index]
            return "Expense Deleted Successfully"
    return  "Expense Not Found"


        
def update_expense(old_expense_name , new_expense_name, new_expense_amount):
    if new_expense_amount <= 0:
        return "Invalid Amount"
    for name , amount in expenses:
        if name != old_expense_name and name == new_expense_name:
            return "Expense Already Exists"

    for index , (name , amount ) in enumerate(expenses):
        if name == old_expense_name:
            expenses[index] = (new_expense_name , new_expense_amount)
            return "Expense Updated Successfully"
    
    return  "Expense Not Found"


def main_menu():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Update Expense")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "7":
            print("Thank You!")
            break



        if choice == "1":
            print("Add Expense Selected")
            expense_name = input("Enter Expense Name: ").strip().lower()
            if not expense_name:
                print("Invalid Expense Name")
                continue
            try:
                expense_amount = float(input("Enter The Amount: ").strip())
                
                result = add_expense(expense_name , expense_amount)
                print(result)

            except ValueError:
                print("Invalid input, Enter in float type only. 0.00")

        
        elif choice == "2":
            print("View Expenses Selected")
            view_expenses()
        

        elif choice == "3":
            print("Calculate Total Selected")
            result = calculate_total()
            print(result)

        elif choice == "4":
            print("Search Expenses Selected")
            search = input("Enter The Expense Name: ").strip().lower()
            if not search:
                print("Invalid Expense Search Name")
                continue
            search_name(search)
       
        elif choice == "5":
            print("Delete Expenses Selected")
            delete_name = input("Enter The Delete Expense Name: ").strip().lower()
            if not delete_name:
                print("Invalid Delete Expense Name")
                continue
            result = delete_expense(delete_name)
            print(result)

        elif choice == "6":
            print("Update Expenses Selected")
            old_expense_name  = input("Enter The Old Expense Name: ").strip().lower()
            new_expense_name = input("Enter The New Expensse Name: ").strip().lower()
            if not old_expense_name or not new_expense_name:
                print("Invalid Update Expense Name")
                continue
            try:
                new_expense_amount = float(input("Enter The Amount: ").strip())
                result = update_expense(old_expense_name, new_expense_name , new_expense_amount)
                print(result)

            except ValueError:
                print("Invalid input, Enter in float type only. 0.00")


        else:
            print("Invalid Choice")


main_menu()





