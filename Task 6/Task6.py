import csv

# Directly providing the path to tasks.csv in your Downloads folder
FILENAME = r"C:\Users\Abdullah\Desktop\tasks.csv"

# Function to load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check if the row has the expected keys ('ID', 'Description', 'Status')
                if 'ID' in row and 'Description' in row and 'Status' in row:
                    row['ID'] = int(row['ID'])  # Convert ID to integer
                    tasks.append(row)
    except FileNotFoundError:
        # If the file doesn't exist, create it with the correct headers
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ['ID', 'Description', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    return tasks


def save_tasks(tasks):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['ID', 'Description', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

def add_task(tasks):
    task_id = len(tasks) + 1
    description = input("Enter task description: ")
    tasks.append({'ID': task_id, 'Description': description, 'Status': 'Pending'})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if tasks:
        for task in tasks:
            print(f"ID: {task['ID']}, Description: {task['Description']}, Status: {task['Status']}")
    else:
        print("No tasks available.")

def remove_task(tasks):
    task_id = int(input("Enter task ID to remove: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Task not found.")

def mark_task_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        task['Status'] = 'Completed'
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Task not found.")

def edit_task(tasks):
    task_id = int(input("Enter task ID to edit: "))
    task = next((task for task in tasks if task['ID'] == task_id), None)
    if task:
        new_description = input("Enter new task description: ")
        task['Description'] = new_description
        save_tasks(tasks)
        print("Task description updated.")
    else:
        print("Task not found.")

def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()
    found_tasks = [task for task in tasks if keyword in task['Description'].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"ID: {task['ID']}, Description: {task['Description']}, Status: {task['Status']}")
    else:
        print("No tasks found.")

def filter_tasks(tasks):
    status = input("Enter status to filter by (Pending/Completed): ")
    filtered_tasks = [task for task in tasks if task['Status'] == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['ID']}, Description: {task['Description']}, Status: {task['Status']}")
    else:
        print("No tasks with this status.")

def clear_all_tasks(tasks):
    confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirmation.lower() == 'y':
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Action canceled.")

def sort_tasks(tasks):
    choice = input("Sort by (1: ID, 2: Status): ")
    if choice == '1':
        tasks.sort(key=lambda x: x['ID'])
    elif choice == '2':
        tasks.sort(key=lambda x: x['Status'])
    else:
        print("Invalid choice.")
    save_tasks(tasks)
    print("Tasks sorted.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            search_task(tasks)
        elif choice == '7':
            filter_tasks(tasks)
        elif choice == '8':
            clear_all_tasks(tasks)
        elif choice == '9':
            sort_tasks(tasks)
        elif choice == '0':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    menu()