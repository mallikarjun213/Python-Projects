from datetime  import datetime

customer_list = []

def customer_registration():

    while True:
        customer_name = input("Enter the customer name: ").strip()
        if not customer_name:
            print("Please enter the cutomer name")
            continue
        if not customer_name.replace(" ","").isalpha():
            print("Please Enter in alphabets only")
            continue
        break


    while True:
        movie_name = input("Enter the movie name: ").strip()
        if not movie_name:
            print("Please enter the movie name")
            continue
        if not movie_name.replace(" ","").isalnum():
            print("Please Enter in alphabets only")
            continue
        break

    while True:
        show_time = input("Enter the show time: (H:M:S AM/PM): ").strip()
        if not show_time: 
            print("Please enter the showtime")
            continue

        try:

            time = datetime.strptime(show_time , "%I:%M:%S %p")

        except ValueError:
            print("Invalid time format")
            continue

        break
    while True:
        seats = input("Enter the  number of seats: ").strip()
        if not seats:
            print("Pleasr enter the seats number")
            continue

        try:
            seats = int(seats)
        
        except ValueError:
            print("Enter number only")
            continue


        if seats < 1 or seats > 5:
            print("Invalid seat count. Enter 1 to 5 seats")
            continue

        break


    customer = {"Customer Name" : customer_name , "Movie Name":movie_name , "Showtime":show_time , "Seats":seats}

    customer_list.append(customer)



    print("------Customer Details-------")
    print(f"Customer Name : {customer_name}")
    print(f"Movie Name : {movie_name}")
    print(f"Show Time : {show_time}")
    print(f"Seats : {seats}")

    return customer


def booking_price_calculation(**kwargs):
    seats = kwargs.get("seats")
    movie_name = kwargs.get("movie_name")
    show_time = kwargs.get("show_time")
    customer_name = kwargs.get("customer_name")

    if seats is None:
        return "Please Enter seat count" 

    if isinstance(seats , bool) or not isinstance(seats , int):
        return "Please enter number only"

    if seats < 1 or seats > 5:
        return "Invalid seat count. Enter 1 to 5 seats"

    ticket_price = 200
    total_price = ticket_price * seats

    discount = 0 
    
    if seats == 3 or seats == 4:
        discount = total_price * 5 / 100
        final_price = total_price - discount

    elif seats == 5:
        discount = total_price * 10 / 100
        final_price = total_price - discount

    else:
        final_price = total_price


    return {"Total Price": total_price,
            "Discount" : discount,
            "Final Price" : final_price,
            "Seats" : seats,
            "Movie Name" : movie_name,
            "Show Time" : show_time,
            "Customer Name" : customer_name}

while True:
    custmoer_details = customer_registration()

    result = booking_price_calculation(seats = custmoer_details.get("Seats"),
                                    customer_name = custmoer_details.get("Customer Name"),
                                    movie_name = custmoer_details.get("Movie Name"),
                                    show_time = custmoer_details.get("Showtime"),)

    if isinstance(result , str):
        print(result)

    else:
        print("-----Booking Bill-----")
        print(f"Customer Name : {result.get('Customer Name')}")
        print(f"Movie Name : {result.get('Movie Name')}")
        print(f"Show Time : {result.get('Show Time')}")
        print(f"Seats : {result.get('Seats')}")
        print(f"Total Price : {result.get('Total Price'):.2f}")
        print(f"Discount : {result.get('Discount'):.2f}")
        print(f"Final Price : {result.get('Final Price'):.2f}")



    choice = input("Do you want to add another customer? (yes/no): ").strip().lower()

    if choice == "no":
        break

print("\n====== FINAL BOOKING SUMMARY ======")
total_customers = len(customer_list)
total_seats = 0
total_collection = 0

for customer in customer_list:
    total_seats += customer.get("Seats")
    price_details = booking_price_calculation(seats = customer.get("Seats"))
    total_collection += price_details.get("Final Price")


print(f"Total Customers : {total_customers}")
print(f"Total Seats Booked : {total_seats}")
print(f"Total Collection : ₹{total_collection:.2f}")
