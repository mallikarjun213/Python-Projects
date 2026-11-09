# Banking system

balance = 1000

def deposit(amount):
    global balance
    if amount <= 0:
        return "Invalid input"
    else:
        balance += amount

    return balance

def withdraw(amount):
    global balance
    if amount <= 0:
        return "Invalid input"
    elif amount > balance:
        return "insufficient balance"
    else:
        balance-= amount

    return balance


def check_balance():
    return balance


def main():
    print("Welcome to Banking system")
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                deposit_amount  = int(input("Enter the amount: ").strip())
            except ValueError:
                print("Please enter numbers only")
                continue

        
            result = deposit(deposit_amount)

            if result != "Invalid input":
                print("Deposit successful")
                print("Current Balance:", result)
                
            else:
                print("Deposit failed:", result)

        elif choice == "2":
            try:
                withdraw_amount = int(input("Enter the withdraw amount: ").strip())
            except ValueError:
                print("Please enter numbers only")
                continue

            result = withdraw(withdraw_amount)
            if result != "Invalid input" and result != "insufficient balance":
                print("Withdraw successful")
                print("Current Balance:", result)
                
            else:
                print("Withdraw failed:", result)

        elif choice == "3":

            result = check_balance()
            print("Current Balance:", result)
            
        
        elif choice == "4":
            print("Thank you for banking!")
            break

        else:
            print("Invalid choice")
            

main()