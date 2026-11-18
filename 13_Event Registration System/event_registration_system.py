

participants_list = []
def register_participant():
    while True:
        # Input name
        name = input("Enter a name: ").strip()
        # Empty input validation
        if not name:
            print("Please enter a name")
            continue
        
        # Input validation
        if not name.replace(" ","").isalpha():
            print("Please enter name in alphabet only")
            continue
        break
    while True:
        # Input age
        age = input("Enter an age: ").strip()
        # Empty input validation
        if not age:
            print("Please enter an age")
            continue

        try:
            # Integer Converstion
            age = int(age)

            # Input age validation
            if age <= 0 or age > 100:
                print("Invalid input")
                continue
        
        except ValueError:
            print("Enter integers only")
            continue
        break

    while True:

        # Input event name
        event_name = input("Enter an event name: ").strip()
        
        # Empty input validation
        if not event_name:
            print("Please enter an event name")
            continue
        
        # Input validation
        if not event_name.replace(" ","").isalpha():
            print("Please Enter an event name in alphabet only")
            continue
        break


    while True:
        # Input city
        city = input("Enter a city name: ").strip()
        
        # Empty input validation
        if not city:
            print("Please enter a city name")
            continue
        
        # Input validation
        if not city.replace(" ","").isalpha():
            print("Please enter a city in alphabets only")
            continue
        break

    details = participant_details(name= name,age=age,event_name=event_name,city=city)
    participants_list.append(details)

    print("Participant added succussfullly")


def participant_details(name,age,event_name,city):
    participants = {"Name" : name,
            "Age"  : age,
            "Event Name" : event_name,
            "City" : city}
    return participants
    

def view_participant_details():
    if not participants_list:
        print("No participants avilable")
        return

    for index , i in enumerate(participants_list, start= 1):
        print(f"{index}.Participants serial number")
        print(f"Name : {i['Name']}")
        print(f"Age : {i['Age']}")
        print(f"Event Name : {i['Event Name']} ")
        print(f"City : {i['City']}")

def search_participant():
    if not participants_list:
        print("No participant available")
        return
    while True:
        name = input("Enter a name: ").strip()
        if not name:
            print("Please Enter a name")
            continue

        if not name.replace(" ","").isalpha():
            print("Enter name in alphabets only")
            continue

        found = False
        for index, i in enumerate(participants_list, start=1):
            if i['Name'] == name:
                found = True
                print(f"{index}. Participant serail number")
                print(f"Name : {i['Name']}")
                print(f"Age : {i['Age']}")
                print(f"Event Name : {i['Event Name']} ")
                print(f"City : {i['City']}")
                return
        if not found:
            print("Participant name is not found")
            continue

def main_menu():

    while True:

        print("===== Event Registration System =====")
        print("1. Register Participant")
        print("2. View Participant Details")
        print("3. Search Participant")
        print("4. Exit")
        
        
        enter_your_choice = input("Enter your choice: ").strip()
        if not enter_your_choice:
            print("Please enter your choice")
            continue

        try:
            enter_your_choice = int(enter_your_choice)

            if enter_your_choice <= 0 or enter_your_choice > 4:
                print("Invalid input")
                continue

        except ValueError:
            print("Enter integer only")
            continue

        if enter_your_choice == 4:
            print("Exited.. program.. Thank you")
            return

        if enter_your_choice == 1:
            register_participant()

        elif enter_your_choice == 2:
            view_participant_details()

        elif enter_your_choice  == 3:
            search_participant()
    
          

main_menu()
            



