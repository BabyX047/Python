# # Simple To-Do List Application

# def display_menu():
#     print("\nTo-Do List Menu:")
#     print("1. View To-Do List")
#     print("2. Add a Task")
#     print("3. Remove a Task")
#     print("4. Exit\n")

# def view_tasks(tasks):
#     if len(tasks) == 0:
#         print("\nYour to-do list is empty.")
#     else:
#         print("\nYour To-Do List:")
#         for index, task in enumerate(tasks, start=1):
#             print(f"{index}. {task}")

# def add_task(tasks):
#     task = input("\nEnter the task you want to add: ")
#     tasks.append(task)
#     print(f'"{task}" has been added to your to-do list.')

# def remove_task(tasks):
#     try:
#         task_number = int(input("\nEnter the number of the task you want to remove: "))
#         if 1 <= task_number <= len(tasks):
#             removed_task = tasks.pop(task_number - 1)
#             print(f'"{removed_task}" has been removed from your to-do list.')
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Please enter a valid number.")

# def main():
#     tasks = []
#     while True:
#         display_menu()
#         choice = input("Choose an option (1-4): ")

#         if choice == '1':
#             view_tasks(tasks)
#         elif choice == '2':
#             add_task(tasks)
#         elif choice == '3':
#             remove_task(tasks)
#         elif choice == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()



####### Version 2 ########

import os

# Load tasks from a file
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task, status, priority = line.strip().split('|')
                tasks.append({"task": task, "status": status, "priority": priority})
    return tasks

# Save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['status']}|{task['priority']}\n")

def add_task(tasks):
    task = input("Enter the new task: \n")
    priority = input("Set priority (high/medium/low): \n").lower()
    tasks.append({"task": task, "status": "incomplete", "priority": priority})

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} [Priority: {task['priority']}] - {task['status']}")
    print("\n")

def edit_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number you want to edit: \n")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task description: \n")
        new_priority = input("Set new priority (high/medium/low): \n").lower()
        tasks[task_num]["task"] = new_task
        tasks[task_num]["priority"] = new_priority
    else:
        print("Invalid task number!\n")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to remove: \n")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    else:
        print("Invalid task number!\n")

def mark_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: \n")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["status"] = "complete"
    else:
        print("Invalid task number!\n")

def sort_by_priority(tasks):
    # Assign a numerical value to each priority
    priority_order = {"high": 1, "medium": 2, "low": 3}

    # Sort the list of tasks based on their priority value
    tasks.sort(key=lambda task: priority_order[task["priority"]])


def main():
    filename = "todo_list.txt"
    tasks = load_tasks(filename)
    
    while True:
        print("To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Mark Task as Completed")
        print("6. Save and Exit\n")

        choice = input("Enter your choice (1-6): \n")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
