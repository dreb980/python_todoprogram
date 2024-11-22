todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is currently empty.")
        print("Add more tasks to see them appear here!")
    else:
        print("Your current to-do tasks: ")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

while True:
    print("\nWelcome to the To-Do List Program.")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the name of the new task to add to list: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the name of the task to remove from the list (Inreverrsible) : ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Quitting the To-Do List Program.")
        break
    else:
        print("Invalid input. Please try again.")