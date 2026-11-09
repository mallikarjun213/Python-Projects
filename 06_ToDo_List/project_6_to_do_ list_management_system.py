
tasks = []

def add_tasks():
    task_name = input("Enter the task name: ").strip().lower()
    if task_name == "":
        print("Task cannot be empty")
    else:
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks avilable")
    else:
        for index , task in enumerate(tasks , start=1):
            print(f"{index}. {task['name']}")

            if task["completed"]:
                print("Status: Completed")
            else:
                print("Status: Pending")

def search_task():
    search_name = input("Enter task name to search: ").strip().lower()
    if any(task["name"] == search_name for task in tasks):
        print(f"Task found: {search_name}")
    else: 
        print(f"Task not found: {search_name}")


def complete_task():
    task_name = input("Enter task name to complete: ").strip().lower()
    found = False
    for task in tasks:
        if task["name"] == task_name:
            print(f"Task completed: {task_name}")
            task["completed"]= True
            found = True

    if not found:
        print(f"Task not found: {task_name}")


def delete_task():
    task_name = input("Enter task name to delete: ").strip().lower()
    found = False

    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            print(f"Delete successfully: {task_name}")
            found = True
            break

    if not found:
        print(f"Task not found: {task_name}")


def main_menu():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter the choice: ").strip()
        if not choice.isdigit():
            print("Please enter the digits only")
        else:

            if choice == "1":
                add_tasks()

            elif choice == "2":
                view_tasks()

            elif choice == "3":
                search_task()

            elif choice == "4":
                complete_task()

            elif choice == "5":
                delete_task()

            elif choice == "6":
                print("Thank you !")
                break
            else:
                print("Invalid choice")

main_menu()      