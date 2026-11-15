
patients=[]

def patients_details():
    while True:
        patient_id = input("Enter the patient id: ").strip()
        if not patient_id:
            print("Please Enter the patient id")
            continue

        try:
            patient_id = int(patient_id)

            if patient_id <= 0:
                print("Invalid input, Enter valid input only")
                continue
            
            found = False
            for i in patients:
                if i["Patient id"] == patient_id:
                    found = True
                    break
            
            if found:
                print("Patient ID already exists")
                continue

        except ValueError:
            print("Entert integer only")
            continue
            

        patient_name = input("Enter the patient name: ").strip().lower()
        if not patient_name:
            print("Please Enter the patient name")
            continue
 
        if not patient_name.replace(" ", "").isalpha():
            print("Enter in alphabates only")
            continue

        patient_age = input("Enter the patient age: ").strip()
        if not patient_age:
            print("Please Enter the patient age")
            continue

        try:
            patient_age = int(patient_age)

            if patient_age <=0 or patient_age > 100:
                print("Invalid input, Enter valid age only")
                continue
        
        except ValueError:
            print("Plese Entert integer only")
            continue


        patient_phone_no = input("Enter the patient phone number: ").strip()
        if not patient_phone_no:
            print("Please enter the patient phone number")
            continue

        if not patient_phone_no.isdigit():
            print("Please enter in digits only")
            continue

        if len(patient_phone_no) != 10:
            print("Phone number must contain 10 digits")
            continue


        patient_detial = {"Patient id": patient_id ,
                "Patient name": patient_name,
                "Patient age": patient_age,
                "Patient phone number": patient_phone_no
                }

        patients.append(patient_detial)

        print("Patient details successfully added")
        return


def view_patients():

    if not patients:
        print("No patients available")
        return


    for index, i in enumerate(patients , start=1):
        print(f"{index}). Patient id : {i['Patient id']} | Patient Name : {i['Patient name']} | Patient Age:{i['Patient age']} | Patient phone number : {i['Patient phone number']}") 
        

def search_patient():
    while True:
        patient_id  = input("Enter patient id: ").strip()
        if not patient_id:
            print("Please enter patient id")
            continue

        try:
            patient_id = int(patient_id)
            if patient_id <= 0:
                print("Valid input only")
                continue

            found = False
            for i in patients:
                if i["Patient id"] == patient_id :
                    print(f"Patient ID: {i['Patient id']}")
                    print(f"Patient Name: {i['Patient name']}")
                    print(f"Patient Age: {i['Patient age']}")
                    print(f"Patient Phone: {i['Patient phone number']}")
                    found = True
                    return

            if not found:
                print("Not found patient id")
                continue
        
        except ValueError:
            print("Please Enter in integers only")
            continue
 
def update_patient_details():
    while True:
        print("===Update patient details===")
        print("1. Patient id")
        print("2. Patient name")
        print("3. Patient age")
        print("4. Patient Phone number")
        print("5. Exit")


        choice = input("Enter your choice bitween 1 to 5: ").strip()
        if not choice:
            print("Please Enter your choice")
            continue

        if not choice.isdigit():
            print("Please Enter your choice in digits only")
            continue

        if choice == "1":

            patient_id = input("Enter patient_id: ").strip()
            if not patient_id:
                print("Enter patient id")
                continue
            try:
                patient_id = int(patient_id)

                if patient_id <= 0:
                    print("Please enter valid patient id")
                    continue
            except ValueError:
                print("Please Enter integers only")
                continue

            found = False
            target_patient_id = None
            for i in patients:
                if i["Patient id"] == patient_id:
                    target_patient_id = i
                    found = True
                    break

            if not found:
                print("Patient id not found")
                continue

            while True:

                new_id = input("Enter the new patient id: ").strip()
                if not new_id:
                    print("Please Enter the new patient id")
                    continue

                try:
                    new_id = int(new_id)
                    if new_id <= 0:
                        print("Negative inputs not valid")
                        continue

                    found = False
                    for i in patients:
                        if i is not target_patient_id and i["Patient id"] == new_id:
                            print("Patient id already in exists")                            
                            found = True
                            break

                    if found:
                        continue

                    target_patient_id["Patient id"] = new_id
                    

                    appointment_found = False

                    for i in appointments:
                        if i["Patient id"] == patient_id:
                            i["Patient id"] = new_id 
                            appointment_found = True

                    if appointment_found:
                        print("Related appointments updated successfully")
                    else:
                        print("No appointments found for this patient")

                    print("Patient ID updated successfully")
                    return
                    
                except ValueError:
                    print("Please Enter valid input only")
                    continue

        elif choice == "2":
            while True:
                patient_id = input("Enter Patient id: ").strip()
                enter_old_patient_name = input("Enter old patient name: ").strip().lower()
                enter_new_patient_name = input("Enter new patient name: ").strip().lower()

                if not patient_id or not enter_old_patient_name or not enter_new_patient_name:
                    print("Empty input is not valid")
                    continue

                if not enter_old_patient_name.replace(" ","").isalpha() or not enter_new_patient_name.replace(" ","").isalpha():
                    print("Enter at alphabets only")
                    continue

                try:
                    patient_id = int(patient_id)

                    if patient_id <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Enter at integers only")
                    continue

                found = False
                old_patient_name = False
                duplicate = False

                target_patient = None
                
                for i in patients:
                    if i["Patient id"] == patient_id:
                        target_patient = i
                        found = True
                        
                        if i["Patient name"].lower() == enter_old_patient_name:
                            old_patient_name = True
                        break
     

                if not found:
                    print("Not found patient id")
                    continue

                if not old_patient_name:
                    print("Incorrect Patient name")
                    continue

                for i in patients:
                    if i is not target_patient and i["Patient name"] == enter_new_patient_name:
                        duplicate = True
                        break

                if duplicate:
                    print("Patient name already in exists")
                    continue

                target_patient["Patient name"] = enter_new_patient_name
                print("Updated Patient name succussfully")
                return

        elif choice == "3":
            while True:
                patient_id = input("Enter the patient id: ").strip()
                update_age = input("Enter the new age: ").strip()

                if not patient_id or not update_age:
                    print("Empty Input not valid")
                    continue

                try:
                    patient_id = int(patient_id)
                    update_age = int(update_age)

                    if patient_id <= 0 or update_age <= 0 or update_age > 100:
                        print("Invalid input")
                        continue
                    found = False
                    for i in patients:
                        if i["Patient id"] == patient_id:
                            found = True
                            i["Patient age"] = update_age
                            print("Updated Patient age")
                            return

                    if not found:
                        print("Patient id not found")
                        continue
            
                except ValueError:
                    print("Plese Enter in integers only")
                    continue
     

        elif choice == "4":
            while True:
                patient_id = input("Enter the patient id: ").strip()
                old_phone_number = input("Enter the old phone number: ").strip().lower()
                new_phone_number = input("Enter the new phone number: ").strip().lower()
                
                # Empty validation
                if not patient_id or not old_phone_number or not new_phone_number:
                    print("Empty inputs not valid")
                    continue
                # Phone number digit validation
                if not old_phone_number.isdigit() or not new_phone_number.isdigit():
                    print("Please enter digits only")
                    continue
                # Phone number length validation
                if len(old_phone_number) != 10 or len(new_phone_number) != 10:
                    print("Phone number must contain 10 digits")
                    continue

                try:
                    patient_id = int(patient_id)

                    if patient_id <= 0:
                        print("Invalid patient id")
                        continue

                    # Flags
                    patient_found = False
                    phone_number_old = False
                    duplicate = False

                    target_patient = None

                    # # Step 1: Find patient using ID
                    for i in patients:
                        if i["Patient id"] == patient_id:
                            patient_found = True
                            target_patient = i

                            #  # Step 2: Check old phone number
                            if i["Patient phone number"] == old_phone_number:
                                phone_number_old = True

                            break
                    if not patient_found:
                        print("Patient ID not found")
                        continue

                    if not phone_number_old:
                        print("Old phone number is incorrect")
                        continue

                    # Step 3: Check duplicate phone number
                    for p in patients:
                        if p is not target_patient and p["Patient phone number"] == new_phone_number:
                            duplicate = True
                            break

                    if duplicate:
                        print("Phone number already exists")
                        continue

                    # Step 4: Update phone number
                    target_patient["Patient phone number"] = new_phone_number

                    print("Phone number updated successfully")
                    return

                except ValueError:
                    print("Please enter integer only")
                    continue

        elif choice == "5":
            print("Exiting Update Patient Details")
            return


        else:
            print("Invalid choice")
            continue

def delete_patient():
    while True:
        patient_id = input("Enter the patient id: ").strip()
        if not patient_id:
            print("Please Enter the patient id")
            continue

        try:
            patient_id = int(patient_id)

            if patient_id <= 0:
                print("Invalid patient id")
                continue
        except ValueError:
            print("Please enter integers only")
            continue

        found = False

        for index , patient in enumerate(patients):
            if patient["Patient id"] == patient_id:
                found = True
                del patients[index]
                print("Patient deleted successfully")
                break
        if not found:
            print("Patient id not found")
            continue

        appointment_found = False

        for index in range(len(appointments)-1 , -1 , -1) :
            if appointments[index]["Patient id"] == patient_id:
                del appointments[index]
                appointment_found = True

        if appointment_found:
            print("All related appointments deleted successfully")
        else:
            print("No appointments found for this patient")
        return



from datetime import datetime           
appointments = []

def book_appointment():

    while True:
        # Step 1: Get Patient ID
        patient_id = input("Enter the patient id: ").strip()
        
        if not patient_id:
            print("Please enter patient id")
            continue

        try:
            patient_id = int(patient_id)
            if patient_id <= 0:
                print("Invalid patient id")
                continue

        except ValueError:
            print("Please enter integer only")
            continue

        # Step 2: Verify Patient ID  
        found = False
        for i in patients:
            if i["Patient id"] == patient_id:
                found = True
                break
                
        if not found:
            print("Patient id not found")
            continue

        # Step 3: Get Appointment Details
        while True:
            doctor_name = input("Enter docter name: ").strip()
            appointment_date = input("Enter appointment date (DD-MM-YYYY):").strip() 
            appointment_time = input("Enter appointment time (HH:MM AM/PM): ").strip()
            about_issue = input("Enter about issue: ").strip()

            # Step 4: Empty Input Validation
            if not doctor_name or not appointment_date or not appointment_time or not about_issue:
                print("Empty input is not valid")
                continue
            
            # Step 5: Doctor Name Validation
            if not doctor_name.replace(" ", "").isalpha():
                print("Please enter doctor name in alphabets only")
                continue

            # Step 6: Issue Validation
            if not about_issue.replace(" ", "").isalpha():
                print("Please enter issue in alphabets only")
                continue

            # Step 7: Date Validation
            try:
                datetime.strptime(appointment_date, "%d-%m-%Y")

            except ValueError:
                print("Invalid date format")
                continue

            # Step 8: Time Validation
            try:
                datetime.strptime(appointment_time, "%I:%M %p")

            except ValueError:
                print("Invalid time format")
                continue


            duplicate_found = False


            for i in appointments:
                if (
                    i["Patient id"] == patient_id
                    and i["Doctor name"].lower() == doctor_name.lower()
                    and i["Appointment date"] == appointment_date
                    and i["Appointment time"].upper() == appointment_time.upper()
                ):
                    duplicate_found = True
                    break

            if duplicate_found:
                print("Duplicate appointment already exists")
                continue
            
            # Step 9: Generate Appointment ID
            if appointments:
                appointment_id = max(i["Appointment id"] for i in appointments) + 1
            else:
                appointment_id = 1


            # Step 10: Create Appointment Dictionary
            appointment_details = {
                "Appointment id": appointment_id,
                "Patient id": patient_id,
                "Doctor name": doctor_name,
                "Appointment date": appointment_date,
                "Appointment time": appointment_time,
                "About issue": about_issue
            }

            # Step 11: Add Appointment to List
            appointments.append(appointment_details)

            print("Appointment booked successfully")
            return


def view_appointments():
    if not appointments:
        print("No appointments available")
        return

    for index , i in enumerate(appointments, start=1):
        print(f"\n Appointment number: {index}")
        print(f"Appointment id: {i['Appointment id']}")
        print(f"Patient id: {i['Patient id']}")
        print(f"Doctor name: {i['Doctor name']}")
        print(f"Appointment date: {i['Appointment date']}")
        print(f"Appointment time: {i['Appointment time']}")
        print(f"About issue: {i['About issue']}")


def cancel_appointment():
    while True:
        appointment_id = input("Enter appointment id: ").strip()
        if not appointment_id:
            print("Please Enter appointment id")
            continue

        try:
            appointment_id = int(appointment_id)

            if appointment_id <= 0:
                print("Invalid input")
                continue

        except ValueError:
            print("Enter in integers only")
            continue

        appointment_found = False
        for index, appointment in enumerate(appointments):
            if appointment["Appointment id"] == appointment_id:
                appointment_found = True
                del appointments[index]
                print("Appointment cancelled successfully")
                return

        if not appointment_found:
            print("Appointment id not found")
            continue 
              
import math
def calculate_patient_bill():
    while True:
        patient_id = input("Enter patient id: ").strip()
        if not patient_id:
            print("Please Enter patient id")
            continue

        try:
            patient_id = int(patient_id)

            if patient_id <= 0:
                print("Inalid input")
                continue

        except ValueError:
            print("Please Enter in integers only")
            continue

        found = False
        for i in patients:
            if i["Patient id"] == patient_id:
                found = True


        if not found:
            print("Patient ID not found")
            continue


        doctor_charges = input("Enter doctor consultation charges: ").strip()

        medicine_charges = input("Enter medicine charges: ").strip()

        room_charges = input("Enter room charges: ").strip()


        if not doctor_charges or not medicine_charges or not room_charges:
            print("Empty input is not valid")
            continue


        try:
            
            doctor_charges = float(doctor_charges)
            medicine_charges = float(medicine_charges)
            room_charges = float(room_charges)

            if not math.isfinite(doctor_charges):
                print("Invalid amount")
                continue
    
            if not math.isfinite(medicine_charges):
                print("Invalid amount")
                continue
    
            if not math.isfinite(room_charges):
                print("Invalid amount")
                continue
            


            if doctor_charges < 0 or medicine_charges < 0 or room_charges < 0:
                print("Invalid input")
                continue
        except ValueError:
            print("Please Enter valid input only")
            continue

        total_charges = doctor_charges + medicine_charges + room_charges

        if not math.isfinite(total_charges):
            print("Total bill is too large")
            continue

        print("=====Hospital Bill=====")
        print(f"Doctor charges:{doctor_charges}")
        print(f"Medicine charges:{medicine_charges}")
        print(f"Room charges:{room_charges}")
        print(f"Total bill: {total_charges:.2f}")
        return

def main_menu():
    while True:
        print("===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient Details")
        print("5. Delete Patient")
        print("6. Book Appointment")
        print("7. View Appointments")
        print("8. Cancel Appointment")
        print("9. Calculate Patient Bill")
        print("10. Exit")

 
        choice = input("Enter your choice: ").strip()
        if not choice:
            print("Please Enter your choice")
            continue

        if not choice.isdigit():
            print("Please enter in digits only")
            continue

        if choice == "1":
            patients_details()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient_details()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            book_appointment()

        elif choice == "7":
            view_appointments()

        elif choice == "8":
            cancel_appointment()

        elif choice == "9":
            calculate_patient_bill()

        elif choice == "10":
            print("Thank you.. Exited Hospital management system")
            return
        else:
            print("Invalid choice")

main_menu()    



        


 


        





                
                
                
  
              
        













        
