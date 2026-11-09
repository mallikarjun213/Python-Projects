# Student Management System

students = []
pass_count = 0
fail_count = 0

def add_student(name,age,marks):
    student = {}
    student["Name"] = name
    student["Age"] = age
    student["Marks"] = marks

    return student

result = add_student("Rahul", 22 , [80, 70, 90])
students.append(result)
result = add_student("Priya", 21 , [90, 85, 95])
students.append(result)



for i in students:
    print(i["Name"], i["Age"], i["Marks"])
    total = 0
    total += sum(i["Marks"])
    i["Total"] = total
    print(i["Name"], total)

    average = total / len(i["Marks"])
    i["Average"] = average
    print(average)


    if average >= 35:
        i["Result"] = "Pass"
        print("Pass")
        pass_count += 1
    else:
        print("Fail")
        i["Result"] = "Fail"
        fail_count +=1

for i in students:
    print(i) 


search_name = input("Search name: ").strip().lower()
found = False
for i in students:
    if search_name == i["Name"].lower():
        print(i)
        found = True


if found == False:
    print("Student not found")


delete_name = input("Delete name: ").strip().lower()
found = False

for i in students:
    if delete_name == i["Name"].lower():
        students.remove(i)
        print("Student deleted successfully")
        found = True
        break

if found == False:
    print("Student not found")

print("After Delete:")



name = input("Enter student name: ").strip().lower()
age = int(input("Enter student age: ").strip())
marks = list(map(int, input("Enter student marks: ").strip().split()))

result = add_student(name, age, marks)
students.append(result)
print("Student added successfully")
print(students)


total = sum(result["Marks"])

result["Total"] = total


average = total / len(result["Marks"])
result["Average"] = average


if average >= 35:
    result["Result"] = "Pass"
   
else:
    result["Result"] = "Fail"

print(result)


for i in students:
    print(i["Name"],round(i["Average"], 2))
    print(f"Name: {i['Name']} | Total: {i['Total']} | Average: {round(i['Average'], 2)} | Result: {i['Result']} | Age: {i["Age"] } | Marks: {i["Marks"]}")

pass_count = 0
fail_count = 0

for i in students:
    if i["Result"] == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Total Students:", len(students))
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)