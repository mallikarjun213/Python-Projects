


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
        

def main_menu():
    while True:
        print("\n===Calculator===")
        print("1.Addition (+)")
        print("2.Subtraction (-)")
        print("3.Multiplication (*)")
        print("4.Division (/)")
        print("5.Exit (E)")

        operation = input("Enter choice to opreation : ").strip()

        if not operation:
            print("Empty input is not valid")
            continue
        
        try:
            operation = int(operation)

            if operation <= 0 or operation > 5:
                print("Invalid input")
                continue
        
        except ValueError:
            print("Enter integer only")
            continue
                 
        if operation == 5:
            print("Thank you... Program exited")
            return
        
        
        num1 = input("Enter number1 : ").strip()
        num2 = input("Enter number2 : ").strip()

        if not num1:
            print("Empty input is not valid")
            continue

        if not num2:
            print("Empty input is not valid")
            continue

        try:
            num1 = float(num1)
            num2 = float(num2)

        except ValueError:
            print("Invalid put")
            continue

        if operation == 1:
            result = add(num1 , num2)
            print(result)

        elif operation == 2:
            result = sub(num1 , num2)
            print(result)

        elif operation == 3:
            result = multiply(num1 , num2)
            print(result)

        elif operation == 4:
            result = division(num1 , num2)
            print(result)

       

main_menu()

        


    