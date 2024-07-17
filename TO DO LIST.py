tasks = []

def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")  # Display tasks starting from 1

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def update_task():
    show_tasks()  # Display the list of tasks to the user
    task_num = int(input("Enter the task number to update: "))  # Ask the user for the task number to update

    # Check if the entered task number is valid (1-based index)
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task: ")  # Ask the user for the new task description
        tasks[task_num - 1] = new_task  # Update the task in the list (0-based index)
        print("Task updated.")  # Confirm the update to the user
    else:
        print("Invalid task number.")  # Inform the user of an invalid task number

while True:
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
