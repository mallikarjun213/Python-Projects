

customer_data = []
def add_customer_details():
    while True:
        # customer name input   
        customer_name = input("Enter a customer name: ").strip()
        # Empty input validation
        if not customer_name:
            print("Please Enter a customer name")
            continue
        
        # Input validation
        if not customer_name.replace(" ","").isalpha():
            print("Enter customer name in alphabets only")
            continue
        break

    while True:
        # Input item name
        item_name = input("Enter an item name: ").strip()
        # Empty input validation
        if not item_name:
            print("Please Enter an item name")
            continue
        break

    while True:
        # Quantity input
        quantity = input("Enter a quantity: ").strip()
        # Empty input validation
        if not quantity:
            print("Please Enter a quantity")
            continue

        try:
            # integer conversion
            quantity = int(quantity)

            # negative input validation
            if quantity <= 0:
                print("Quantity must be greater than zero")
                continue
        except ValueError:
            print("Enter integers only")
            continue
        break

    while True:
        # Iinput price
        price = input("Enter a price: ").strip()
        # Empty input validation
        if not price:
            print("Please enter a price")
            continue

        try:
            # float conversion
            price = float(price)

            # negative input validation
            if price <= 0:
                print("Price must be greater than zero")
                continue

        except ValueError:
            print("Enter numbers only")
            continue
        break

    while True:
    # Tax input
        tax_input = input("Enter a tax value: (Enter for default 5%)").strip()
        if not tax_input:
            use_default_tax = True
            tax_input = 5
            break
        else:
            try:
                # Tax input float conversion 
                tax_input = float(tax_input)

                # Negative input validation
                if tax_input < 0:
                    print("Tax cannot be negative")
                    continue
      
            
            except ValueError:
                print("Enter numbers only")
                continue
            use_default_tax = False
            break
        
    if use_default_tax:
        total_price = total_bill_amount_calculate(price, quantity)
    else:
        total_price = total_bill_amount_calculate(price, quantity,tax_input)
  



    details = customer_details(customer_name=customer_name, item_name=item_name, 
    quantity=quantity , price=price, tax_input=tax_input, total_price=total_price)
    customer_data.append(details)


    print("Customer details received successfully")
    print(f"Total bill Amount: Rs. {total_price:.2f}")
            
def customer_details( customer_name, item_name, quantity, price, tax_input, total_price):
    customer = {"Customer Name": customer_name,
                "Item Name": item_name,
                "Quantity": quantity,
                "Price":price,
                "Tax" : tax_input,
                "Total Bill": total_price}

    return customer


def view_customer_details():
    if not customer_data:
        print("No customer data available")
        return

    for index , i in enumerate(customer_data, start= 1):
        print(f"{index}. customer serial number")
        print(f"Customer Name : {i['Customer Name']}")
        print(f"Item Name : {i['Item Name']}")
        print(f"Quantity : {i['Quantity']}")
        print(f"Price : {i['Price']}")
        print(f"Tax : {i['Tax']}")
        print(f"Total Bill: Rs. {i['Total Bill']:.2f}")
    return


def search_customer():
    if not customer_data:
        print("No customer data available")
        return

    while True:
        customer_name = input("Enter a customer name: ").strip()
        if not customer_name:
            print("Please enter a customer name")
            continue
        
        if not customer_name.replace(" ","").isalpha():
            print("Enter Customer name in alphabets only ")
            continue

        found = False
        for index , i in enumerate(customer_data, start= 1):
            if i["Customer Name"].lower() == customer_name.lower():
                found = True
                print(f"{index}. customer serial number")
                print(f"Customer Name : {i['Customer Name']}")
                print(f"Item Name : {i['Item Name']}")
                print(f"Quantity : {i['Quantity']}")
                print(f"Price : {i['Price']}")
                print(f"Tax : {i['Tax']}")
                print(f"Total Bill: Rs. {i['Total Bill']:.2f}")
                return
        if not found:
            print("Customer name not found")
            continue


def total_bill_amount_calculate(price, quantity, tax=5):

    bill = price * quantity 
    tax_value = bill * tax / 100

    total_bill = bill + tax_value

    return total_bill


def main_menu():
    while True:
        print("1. Add Customer Details")
        print("2. View Customer Details")
        print("3. Search Customer Details")
        print("4. Exit")

        choice = input("Enter Your choice: ").strip()
        if not choice:
            print("Please Enter your choice")
            continue

        try:
            choice = int(choice)

            if choice <= 0 or choice > 4:
                print("Invalid Choice")
                continue

        except ValueError:
            print("Enter integers only")
            continue

        if choice == 4:
            print("Thank you.. exited")
            return
        


        if choice == 1:
            add_customer_details()

        elif choice == 2:
            view_customer_details()

        elif choice == 3:
            search_customer()

main_menu()