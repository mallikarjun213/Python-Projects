customers = []

bookings = []


def customers_details():
    while True:
        customer_id = input("Enter the customer id: ").strip()
        customer_name = input("Enter the customer name: ").strip()
        customer_age = input("Enter the age: ").strip()
        customer_phone_number = input("Enter the phone number: ").strip()
        customer_address = input("Enter the customer address: ").strip()

        # Empty input validation
        if (not customer_id or not customer_name or
            not customer_age or not customer_phone_number or
            not customer_address
            ):
            print("Empty input is not valid")
            continue

        # Phone number validation

        elif not customer_phone_number.isdigit():
            print("Phone number should be in digits")
            continue

        elif not len(customer_phone_number) == 10:
            print("Phone number should be 10 digits")
            continue

        # Integer converstion
        try: 
            customer_id = int(customer_id)
            customer_age = int(customer_age)

        # Input validation
            if customer_id <= 0 or customer_age <= 0 or customer_age > 100:
                print("Invalid input")
                continue

        except ValueError:
            print("Plese Enter in integers only")
            continue

        if not customer_name.replace(" ","").isalpha() or not customer_address.replace(" ", "").isalpha():
            print("Plese use alphabets only")
            continue


        # Duplicate Customer Id  and phone number validation
        customer_id_check = False
        customer_phone_number_check = False
        for i in customers:
            if i["Customer ID"] == customer_id:
                customer_id_check = True
             

            if i["Customer Phone Number"] == customer_phone_number:
                customer_phone_number_check = True
              
        
        if customer_id_check:
            print("Customer Id already exists")
            continue

        if customer_phone_number_check:
            print("Customer phone number already exists")
            continue

        # Storeing Customer details
        customer_detail = {"Customer ID": customer_id,
                           "Customer Name": customer_name,
                           "Customer Age": customer_age,
                           "Customer Phone Number" : customer_phone_number,
                           "Customer Address": customer_address
                           }
        # Transfor to list
        customers.append(customer_detail)
        print("Customer details recevied succsussfully")
        return

# view customers
def view_customers():
    # Empty input validation
    if not customers:
        print("No customers available")
        return
    
    for index , i in enumerate(customers , start= 1):
        print(f"{index}.Customer Serial number")
        
        print(f"Customer ID: {i['Customer ID']}")
        print(f"Customer Name: {i['Customer Name']}")
        print(f"Customer Age: {i['Customer Age']}")
        print(f"Customer Phone Number: {i['Customer Phone Number']}")
        print(f"Customer Address: {i['Customer Address']}")

# search customer
def search_customer():
    while True:
        customer_id = input("Enter the customer id: ").strip()
        # Empty input validation
        if not customer_id:
            print("Please enter the customer id")
            continue

        # Integer converstion
        try:
            customer_id = int(customer_id)
            
            # Input validation
            if customer_id <= 0:
                print("Invalid input")
                continue
        
        except ValueError:
            print("Enter in integer only")
            continue

        # Flag
        found = False
        for index ,  i in enumerate(customers , start= 1):
            if i["Customer ID"] == customer_id:
                found = True
                print(f"{index}.Customer Serial number")
                print(f"Customer ID: {i['Customer ID']}")
                print(f"Customer Name: {i['Customer Name']}")
                print(f"Customer Age: {i['Customer Age']}")
                print(f"Customer Phone Number: {i['Customer Phone Number']}")
                print(f"Customer Address: {i['Customer Address']}")
                return

        if not found:
            print("Customer Id not found")
            continue


# update customer
def update_Customer():
    if not customers:
        print("No customers available")
        return
    
    while True:
        
        print("\n====Update Customer details====")
        print("1. Customer ID")
        print("2. Customer Name")
        print("3. Customer Age")
        print("4. Customer Phone Number")
        print("5. Customer Address")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

       
        if not choice:
            print("Please enter your choice")
            continue

        # Input validation
        if not choice.isdigit():
            print("Enter in digits only")
            continue

        
        # Customer id updating
        if choice == "1":
            customer_id = input("Enter customer id: ").strip()
            if not customer_id:
                print("Please Enter customer id")
                continue
            
            # Integer converstion
            try:
                customer_id = int(customer_id)

                # Input validation
                if customer_id <= 0:
                    print("Invalid input")
                    continue

            except ValueError:
                print("Enter integer only")
                continue

        
            # Flag
            found = False
            target_customer_id = None

            # Find customer Id 
            for i in customers:
                if i["Customer ID"] == customer_id:
                    found = True
                    target_customer_id = i
                    break

            if not found:
                print("Customer Id not found")
                continue

            while True:
                # New customer Id input
                customer_id_update = input("Enter new customer id: ").strip()
                if not customer_id_update:
                    print("Please Enter new customer id")
                    continue

                try: # Integer converstion
                    customer_id_update = int(customer_id_update)

                    if customer_id_update <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Enter in integer only")
                    continue

                # Flag
                duplicate_id_check = False

                # Duplicate customer Id validation
                for i in customers:
                    if i is not target_customer_id and i["Customer ID"] == customer_id_update:
                        duplicate_id_check = True
                        break

                if duplicate_id_check:
                    print("Customer ID already in exists")
                    continue

                # Updatind Customer ID
                target_customer_id["Customer ID"] = customer_id_update
                print("Customer ID updated succussfully")
                return

        # Update Name
        elif choice == "2":
            while True:
                customer_id = input("Enter customer id: ").strip()
                enter_old_name = input("Enter old name: ").strip()
                enter_new_name = input("Enter the new name: ").strip()
                # Empty Input validaton
                if not customer_id or not enter_old_name or not enter_new_name:
                    print("Empty input is not valid")
                    continue

                # Input validation 
                if not enter_old_name.replace(" ","").isalpha() or not enter_new_name.replace(" ","").isalpha():
                    print("Please enter alphabets only")
                    continue

                try:
                    # Integer converstion
                    customer_id = int(customer_id)

                    # Input validation
                    if customer_id <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Enter integer only")
                    continue
                
                # Flag
                customer_id_check = False
                customer_name_check = False
                
                for i in customers:
                    if i["Customer ID"] == customer_id:
                        customer_id_check = True
                        

                        if i["Customer Name"] == enter_old_name:
                            customer_name_check = True
                            i["Customer Name"] = enter_new_name
                            print("Name updated succussfully")
                            return
                
                if not customer_id_check:
                    print("Customer id not found")
                    continue

                if not customer_name_check:
                    print("incorrect customer name")
                    continue
        
        # Update age
        elif choice == "3":
            while True:
                customer_id =  input("Enter customer id: ").strip()
                update_age = input("Enter age to update: ").strip()
                
                # Empty input validation
                if not customer_id or not update_age:
                    print("Empty input cannot be empty")
                    continue

                try: # integer converstion
                    customer_id = int(customer_id)
                    update_age = int(update_age)

                    if customer_id <= 0 or update_age <= 0 or update_age > 100:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Invalid iput Enter in integer only")
                    continue


                customer_id_check  = False
                target_update_age = None
                for i in customers:
                    if i["Customer ID"] == customer_id:
                        target_update_age = i
                        customer_id_check = True

    
                if not customer_id_check:
                    print("Customer id not found")
                    continue

                if target_update_age["Customer Age"] == update_age:
                    print("customer age already in exists")
                    continue

                target_update_age["Customer Age"] = update_age
                print("Updated age succussfully")
                return
                                            
        
        # update phone number
        elif choice == "4":
            while True:
                customer_id = input("Enter the customer id: ").strip()
                old_phone_number = input("Enter the old phone number: ").strip()
                new_phone_number = input("Enter the new phone number: ").strip()              
                
                
                if not customer_id or not old_phone_number or not new_phone_number:
                    print("Empty input is not valid")
                    continue

                if not old_phone_number.isdigit() or not new_phone_number.isdigit():
                    print("Invalid input, Enter in digits only")
                    continue 

                if not len(old_phone_number) == 10 or not len(new_phone_number) == 10:
                    print("Phone number is not in 10 digits")
                    continue 

                try:

                    customer_id = int(customer_id)

                    if customer_id <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Invalid input , Enter in integer only")
                    continue


                customer_id_check = False
                old_phone_number_check = False
                duplicate_check =  False

                target_phone_number = None

                for i in customers:
                    if i["Customer ID"] == customer_id:
                        target_phone_number = i
                        customer_id_check = True

                        if i["Customer Phone Number"] == old_phone_number:
                            old_phone_number_check = True
                        break

                if not customer_id_check:
                    print("Customer id not found")
                    continue

                if not old_phone_number_check:
                    print("Incorrect phone number")
                    continue

                for i in customers:
                    if i is not  target_phone_number and i["Customer Phone Number"] == new_phone_number:
                        duplicate_check = True
                        break

                if duplicate_check:
                    print("Customer phone numbber already in exists")
                    continue

                target_phone_number["Customer Phone Number"] = new_phone_number
                print("Updated customer phone number succussfully")
                return
        
        elif choice == "5":
            while True:
                customer_id = input("Enter customer id: ").strip()
                customer_new_address = input("Enter the customer new address: ").strip()

                if not customer_id or not customer_new_address:
                    print("Empty input is not valid")
                    continue

                if not customer_new_address.replace(" ","").isalpha():
                    print("Enter in alphabets only")
                    continue

                try:
                    customer_id = int(customer_id)

                    if customer_id <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Enter in integer only")
                    continue

                found = False
                customer_address_check  = False

                target_customer_address = None
                for i in customers:
                    if i["Customer ID"] == customer_id:
                        target_customer_address = i
                        found = True

                        if i["Customer Address"] == customer_new_address:
                            customer_address_check = True
                        break

                if not found:
                    print("Customer id is not found")
                    continue

                if customer_address_check:
                    print("Customer address already in exists")
                    continue


                target_customer_address["Customer Address"] = customer_new_address
                print("Updated customer address succussfully")
                return

        elif choice == "6":
            print("Thak you! exited")
            return

        else:
            print("Invalid choice")
            continue


def delete_customer():
    if not customers:
        print("No customers available")
        return

    while True:
        customer_id = input("Enter customer id: ").strip()
        
        if not customer_id:
            print("Empty input is not valid")
            continue

        try:
            customer_id = int(customer_id)

            if customer_id <= 0:
                print("Invalid input")
                continue

        except ValueError:
            print("Enter integer only")
            continue

        found = False
        for index , i in enumerate(customers):
            if i["Customer ID"] == customer_id:
                found = True
                del customers[index]
                print("Deleted customer succussfully")
                return

        if not found:
            print("Customer id not found")
            continue



from datetime import datetime
def book_room():
    if not customers:
        print("No customers available")
        return
    
    while True:
        customer_id = input("Enter customer id: ").strip()
        room_number = input("Enter room number: ").strip()
        booking_date = input("Enter booking date (DD-MM-yyyy): ").strip()
        booking_time = input("Enter the booking time (HH:MM AM/PM): ").strip()
        
        if not customer_id or not room_number or not booking_date or not booking_time:
            print("Empty input is not valid")
            continue

        if not room_number.isdigit():
            print("Enter in digit only")
            continue


        try:
            booking_date_obj = datetime.strptime(booking_date, "%d-%m-%Y")
            today = datetime.now().date()

            if booking_date_obj.date() < today:
                print("Past date is not allowed")
                continue

        except ValueError:
            print("Invalid date format")
            continue

        try:
            datetime.strptime(booking_time, "%I:%M %p")

        except ValueError:
            print("Invaldi time format")
            continue

        try:
            customer_id = int(customer_id)
            room_number = int(room_number)

            if customer_id <= 0 or room_number <= 0:
                print("Invalid input")
                continue
        
        except ValueError:
            print("Enter integer only")
            continue

        found = False

        for i in customers:
            if i["Customer ID"] == customer_id:
                found = True
                break
        
        if not found:
            print("Customer id is not found")
            continue

        
        duplicat_check = False
        
        for i in bookings:
            if i["Room Number"] == room_number and i["Booking Date"] == booking_date_obj:
                duplicat_check = True
                break

        if duplicat_check:
            print("Room is already booked")
            continue

        booking_details = {"Customer Id": customer_id,
                           "Room Number": room_number,
                           "Booking Date": booking_date_obj,
                           "Booking Time": booking_time}

        bookings.append(booking_details)
        print("Room Booked succussfully")
        return



def view_room_booking():
    if not bookings:
        print("No bookig available")
        return

 

    for index , i in enumerate(bookings, start= 1):
        print(f"{index}.Booking Serial Number")
        print(f"Customer Id : {i['Customer Id']}")
        print(f"Room Number : {i['Room Number']}")
        print(f"Booking Date : {i['Booking Date']}")
        print(f"Booking Time : {i['Booking Time']}")
    return


def cancel_room_booking():
    if not bookings:
        print("No bookings available")
        return

    while True:
        customer_id = input("Enter customer id: ").strip()
        booked_room_number = input("Enter room booked number: ").strip()
        booking_room_date = input("Enter room booking date (DD-MM-YYYY): ").strip()


        if not customer_id or not booked_room_number or not booking_room_date:
            print("Empty input is not valid")
            continue

        try:
            booking_room_date_obj = datetime.strptime(booking_room_date , "%d-%m-%Y")

        except ValueError:
            print("Invalid date format")
            continue

        try:
            customer_id = int(customer_id)
            booked_room_number = int(booked_room_number)

            if customer_id <= 0 or booked_room_number <= 0:
                print("Invalid input")
                continue

        except ValueError:
            print("Enter integer only")
            continue

        customer_id_check  = False
        room_check = False
        room_booking_date_check = False
        for i in bookings:
            if i["Customer Id"] == customer_id:
                customer_id_check = True

                if i["Room Number"] == booked_room_number:
                    room_check = True

                    if i["Booking Date"] ==  booking_room_date_obj:
                        room_booking_date_check = True
                    
                    break

        if not customer_id_check:
            print("Customer id not found")
            continue

        if not room_check:
            print("Incorrect room number")
            continue

        if not room_booking_date_check:
            print("Incorrect booking date")
            continue

        
        for index , i in enumerate(bookings):
            if i["Customer Id"] == customer_id and i["Room Number"] == booked_room_number and i["Booking Date"] == booking_room_date_obj:
                del bookings[index]
                print("Room canceled succussfully")
                return

import math
def calculate_bill():
    if not bookings:
        print("NO bookings availbale")
        return

    while True:
        customer_id = input("Enter Customer id: ").strip()
        room_booking_date = input("Enter room booking date (DD-MM-YYYY)").strip()
        room_number = input("Enter room number: ").strip()
        number_of_days = input("Enter number of days:  ").strip()
        room_rent_perday = input("Enter room rent per day").strip()
        food_charges = input("Enter room charges: ").strip()
    

        if not customer_id or not room_number or not number_of_days or not room_rent_perday or not food_charges or not room_booking_date:
            print("Empty input is not valid")
            continue

        try:
            room_booking_date_obj = datetime.strptime(room_booking_date, "%d-%m-%Y")

        except ValueError:
            print("Invalid date format")
            continue

        try:
            customer_id = int(customer_id)
            room_number = int(room_number)
            number_of_days = int(number_of_days)
            try:
                food_charges = float(food_charges)
                room_rent_perday = float(room_rent_perday)

            except ValueError:
                print("Enter in float type only")
                continue

            if not math.isfinite(food_charges):
                print("Invalid amount")
                continue

            if not math.isfinite(room_rent_perday):
                print("Invalid amount")
                continue

            if customer_id <= 0 or room_number <= 0 or number_of_days <= 0 or food_charges < 0 or room_rent_perday <= 0:
                print("Invalid input")
                continue
        
        except ValueError:
            print("Enter integer only")
            continue

        customer_id_check = False
        room_check = False
        booking_room_date_check = False
        for i in bookings:
            if i["Customer Id"] == customer_id:
                customer_id_check = True

                if i["Room Number"] == room_number:
                    room_check = True

                    if i["Booking Date"] == room_booking_date_obj:
                        booking_room_date_check = True
                        break

        if not customer_id_check:
            print("Customer id not found")
            continue
        if not room_check:
            print("Room number not found")
            continue

        if not booking_room_date_check:
            print("Incorrect Booking date")
            continue

        for i in bookings:
            if i["Customer Id"] == customer_id and i["Room Number"] == room_number and i["Booking Date"] == room_booking_date_obj:
                total_bill = number_of_days * room_rent_perday + food_charges

                if not math.isfinite(total_bill):
                    print("Total bill is too large")
                    continue

                print("===Hotel management bill===")
                print(f"Customer ID: {customer_id}")
                print(f"Room Number: {room_number}")
                print(f"Number Of Days: {number_of_days}")
                print(f"Room Rent Per Day: {room_rent_perday}")
                print(f"Food Charges: {food_charges}")
                print(f"Total BIll: {total_bill:.2f}")

                print("Thank you for visiting")
                return
    

def main_menu():
    while True:
        print("\n=====Wellcome TO Hotel Management System")
        print("1.Add Customer")
        print("2.View Customers")
        print("3.Search Customer")
        print("4.Update Customer")
        print("5.Delete Customer")
        print("6.Book Room")
        print("7.View Room Bookings")
        print("8.Cancel Room Booking")
        print("9.Calculate Hotel Bill")
        print("10.Exit Program")

        choice = input("Enter your choice: ").strip()
        if not choice:
            print("Please Enter your choice")
            continue

        if not choice.isdigit():
            print("Enter digits only")
            continue


        if choice == "1":
            customers_details()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            update_Customer()

        elif choice == "5":
            delete_customer()

        elif choice == "6":
            book_room()

        elif choice == "7":
            view_room_booking()

        elif choice == "8":
            cancel_room_booking()

        elif choice == "9":
            calculate_bill()
        
        elif choice == "10":
            print("Thank you for using Hotel Management System")
            return

        else:
            print("Ivalid Choice")
            continue

main_menu()

    






