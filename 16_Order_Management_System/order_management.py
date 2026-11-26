


def check_discount(total_price , discount):

    if isinstance(discount , bool):
        return "Invalid  discount"

    try:
        discount = float(discount)

    except (ValueError , TypeError):
        return "Enter valid discount"


    if discount < 0:
        return "Invalid discount"

    if discount > total_price:
        return "Discount cannot exceed total price"

    return discount


def generate_order(*args , **kwargs):
    # price validation

    if not args:
        return "Enter at least one price"

    prices = []

    try:

        for price in args:
            if isinstance(price , bool):
               return "Invalid price"

            price = float(price)

        if price <= 0:
            return "Invalid price"

        prices.append(price)


    except (ValueError , TypeError):
        return "Enter vlaid price only"

    total_price = sum(prices)


    # customer name validation
    name = kwargs.get("customer", "Unknown customer")

    if not isinstance(name , str):
        return "Enter valid customer name"

    if not name.replace(" ", "").isalpha():
        return "Enter name in alphabets only"

    # 3. Phone validation

    phone = kwargs.get("phone")


    if phone is not None:
        if not isinstance(phone , str):
            return "Invalid phone number"

        if len(phone) != 10 or not phone.isdigit():
            return "Invalid phone number"


    else:
        phone = "Phone provided"


    # 4. Quantity validation

    quantity = kwargs.get("quantity", 1)

    if isinstance(quantity , bool):
        return "Invalid quantity"


    try:
        quantity = int(quantity)

    except(ValueError , TypeError):
        return "Enter valid quantity"


    if quantity < 1:
        return "Invalid quantity"

    total_price = total_price * quantity


    # Discount validation

    discount =  kwargs.get("discount", 0)

    discount_result = check_discount(total_price , discount)

    if isinstance(discount_result ,str):
        return discount_result

    discount = discount_result
    
    # Payment validation

    payment = kwargs.get("Payment" , "cash")

    if not isinstance(payment, str):
        return "Invalid payment method"

    payment = payment.lower()

    if payment not in ("cash", "card" , "upi"):
        return "Invalid payment method"

    

    # Final calculation

    processing_fees = 0
    tax = 0

    final_amount = (total_price - discount + processing_fees + tax)

    return(name , phone , quantity , total_price , discount , processing_fees , tax , final_amount , payment)

#==============================
# MODE 1: DIRECT VALUES

#==============================

# result = generate_order(500,
#     customer="Ravi Kumar",
#     discount=100,
#     phone="1234512345",
#     payment="CASH",
#     quantity=2
# )




# =================================
# MODE 2: USER INPUT
# =================================



price = input("Enter product price: ")
customer = input("Enter customer name: ")
phone = input("Enter phone number: ")
quantity = input("Enter quantity: ")
discount = input("Enter discount: ")
payment = input("Enter payment method: ")

result = generate_order(
    price,
    customer=customer,
    phone=phone,
    quantity=quantity,
    discount=discount,
    payment=payment
)


# =================================
# DISPLAY ORDER
# =================================

if isinstance(result, str):

    print(result)

else:

    (
        name, phone, quantity, total,
        discount, processing_fees, tax,
        final, payment
    ) = result

    print("\n===== ORDER DETAILS =====")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total}")
    print(f"Discount: {discount}")
    print(f"Processing Fees: {processing_fees}")
    print(f"Tax: {tax}")
    print(f"Final Amount: {final}")
    print(f"Payment: {payment}")


