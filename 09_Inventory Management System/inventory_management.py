

products = []
def add_product():

    while True:
        product_name = input("Enter product name: ").strip().lower()
        if not product_name:
            print("Please Enter Product name")
            continue

        found = False
        for i in products:
            if i[ "Product name"].lower() == product_name:
                print("Product already exists")
                found = True
                break
        if found:
            continue
 
        price_input = input("Enter product price: ").strip()
        
        if not price_input:
            print("Please Enter product price")
            continue
        
        try:
            price = float(price_input)
            
            if price < 0:
                print("Negative inputs not valid")  
                continue

        
        except ValueError:
            print ("Invalid input , Enter valid input onnly")
            continue

    
        quantity_input = input("Enter quantity: ").strip()
        if not quantity_input:
                print("Please Enter product quantity")
                continue

        try:
            quantity = int(quantity_input)
            if quantity < 0:
                print("Negative inputs not valid")
                continue


        except ValueError:
            print("Invalid input , Enter valid input only)")
            continue

        
        dic_product = {
            "Product name": product_name,
            "Product price": price,
            "Product quantity": quantity

        }

        products.append(dic_product)
        print("Product added successfully!")
        break


def view_products():
    if not products:
        print("No products available")
        return

    for index , product in enumerate(products , start=1):
        print(f"\n Product number: {index}")
        print(f"Product Name : {product['Product name']}")
        print(f"Product Price : {product['Product price']}")
        print(f"Product Quantity : {product['Product quantity']}")


def search_product():
    while True:
        search_product_name = input("Enter the product name: ").strip().lower()
        if not search_product_name:
            print("Please Enter the product name:")
            continue

        found = False
        for i in products:
            if i["Product name"].lower() == search_product_name:
                print("Product Found", i)
                found = True
                break

        if not found:
            print("Product not found")
        break

def delete_product():
    while True:
        delete_product_name = input("Enter product name to delete: ").strip().lower()
        if not delete_product_name:
            print("Please Enter name to delete")
            continue

        found = False
        for  i in products:
            if i["Product name"].lower() == delete_product_name:
                products.remove(i)
                print("Successfully deleted")               
                found = True
                break 

        if not found:
            print("Not found")

        break      



def update_product():

    while True:
        print("\n choose for Update products")
        print("1.Product name")
        print("2.Product price")
        print("3.Product Quantity")
        print("4.Exit")
        
        chooice = input("Enter your choice for update products: ").strip()
        if not chooice:
            print("Please enter your choice for update products")
            continue
        elif not chooice.isdigit():
            print("Invalid input Enter digits only")
            continue

        if chooice == "1":

            old_product_name = input("Enter old product name: ").strip().lower()
            if not old_product_name:
                print("Please enter old product name: ")
                continue

            new_product_name = input("Enter new product name: ").strip().lower()
            if not new_product_name:
                print("Please enter product name to update")
                continue

            found = False
            for i in products:
                if i["Product name"].lower() == old_product_name:
                    old_product = i
                    found = True
                    

                    duplicate = False
                    for i in products:
                        if i is not old_product:
                            if i["Product name"].lower()== new_product_name:
                                duplicate = True
                                print("Product name already exists")
                                break   

                    
                    if duplicate:
                        continue
                    old_product["Product name"] = new_product_name
                    print("Product name updated successfully")
                    break

            if not found:
                print("Not found")
            continue

        elif chooice == "2":
       
            product_name= input("Enter product name: ").strip().lower()
            if not product_name:
                print("Please Enter product name")
                continue

            found = False
            target_product = None
            
            for i in products:
                if i["Product name"].lower() == product_name:
                    target_product = i
                    found = True
                    break   
                 

            if not found:
                print("Not found")
                continue

            while True:
                update_product_price = input("Enter the product price: ").strip()
                if not update_product_price:
                    print("Please enter product price")
                    continue

                try:
                    update_product_price = float(update_product_price)
                    if update_product_price < 0:
                        print("Negative inputs not valid")
                        continue

                    target_product["Product price"] = update_product_price
                    print("Updated product price successfully")
                    break

                except ValueError:
                    print("Invalid input")
                    continue


        elif chooice == "3":
            product_name = input("Enter product name: ").strip().lower()
            if not product_name:
                print("Please Enter product name")
                continue

            found = False
            target_quantity = None
            for i in products:
                if i["Product name"].lower() == product_name:
                    target_quantity = i
                    found = True
                    break

            
            if not found:
                print("Not found")
                continue
            
            while True :
                update_quantiy = input("Enter the quantiy: ").strip()
                if not update_quantiy:
                    print("Please enter the quanttity")
                    continue


                try:
                    update_quantiy = int(update_quantiy)

                    if update_quantiy < 0:
                        print("Negative inputs not valid")
                        continue

                    target_quantity["Product quantity"] = update_quantiy
                    print("Product quantity update successfully")
                    break

                except ValueError:
                    print("Invalid input")
                    continue
            
        elif chooice == "4":
            print("Exited Succussfully")
            return

                    
def update_stock():
    while True:
        print("1. Add stock")
        print("2. Reduce stock")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if not choice:
            print("Please Enter your choice")
            continue

        if not choice.isdigit():
            print("Invalid input, Enter in digit only")
            continue

        if choice == "1":
            product_name = input("Enter the product name: ").strip().lower()
            if not product_name:
                print("Please Enter the product name")
                continue

            found = False
            target_stock = None
            for i in products:
                if i["Product name"].lower() == product_name:
                    target_stock = i
                    found = True
                    break

            if not found:
                print("Not found")
                continue
            
            while True:
                add_stock_quantity = input("Add Stock quantity:  ").strip()
                if not add_stock_quantity:
                    print("Please add stock quentity")
                    continue
                try:
                    add_stock_quantity = int(add_stock_quantity)

                    if add_stock_quantity <= 0:
                        print("Enter Postive quantity only")
                        continue
                    
                    
                    target_stock["Product quantity"] += add_stock_quantity
                    print("Stock quantity successfully added")
                    break
                
                
                except ValueError:
                    print("Invalid input")
                    continue
            
        elif choice == "2":
            while True:
                product_name = input("Enter the product name: ").strip().lower()
                if not product_name:
                    print("Please enter the product name")
                    continue

                found = False
                target_reduce_stock = None
                for i in products:
                    if i["Product name"].lower() == product_name:
                        target_reduce_stock = i
                        found = True
                        break

                if not found:
                    print("Not found")
                    continue

                while True:
                    reduce_quatity = input("Enter reduce quantity: ").strip()
                    if not reduce_quatity:
                        print("Please enter reduce quantity")
                        continue

                    try:
                        reduce_quatity = int(reduce_quatity)

                        if reduce_quatity <= 0:
                            print("Enter Positive quantity only")
                            continue

                        if reduce_quatity > target_reduce_stock["Product quantity"]:
                            print("Insufficient stock")
                            continue

                        target_reduce_stock["Product quantity"] -= reduce_quatity
                        print("Product stock reduced successfully")
                        return

                    except ValueError:
                        print("Invalid input")
                        continue
        
        
        elif choice == "3":
            print("Exited successfully")
            return

def calculate_stock_value():
    total_Stock_value = 0
    
    for i in products:
        total_value = i["Product price"] * i["Product quantity"]
        total_Stock_value += total_value
    return total_Stock_value


def low_stock_alert():
    found = False
    for i in products:
        if i["Product quantity"] <= 5:
            print(f"Product Name: {i['Product name']}, Product Quntity: {i['Product quantity']}")
            found = True
    if not found:
        print("No low stock products found")


def main_menu_system():
    print("\n Welcome to Inventory Management System")
    while True:
        print("1. Add Product")
        print("2. View Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Update Stock")
        print("7. Total Stock value")
        print("8. Low Stock Alert")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if not choice:
            print("Plese Enter your choice")
            continue

        if not choice.isdigit():
            print("Invalid input")
            continue


        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            update_stock()

        elif choice == "7":
            result = calculate_stock_value()
            print(result)

        elif choice == "8":
            low_stock_alert()

        elif choice == "9":
            print("Exited Successfully , thank you!")
            break

        else:
            print("Invalid choice")
            continue

main_menu_system()





                        

                    




























        