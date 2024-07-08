import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": task, "done": False})
    save_tasks(tasks)
    print("Task added...")

def view_tasks():
    tasks = load_tasks()
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        print(f"{task['id']}. {task['task']} - {status}")

def update_task(task_id, new_task):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_task
            save_tasks(tasks)
            print("Task Updated...")
            return
    print("Task Not Found...")

def mark_task_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Task marked as Done...")
            return
    print("Task Not Found...")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task Deleted...")

def main():
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            task = input("Enter Task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter Task ID to update: "))
            new_task = input("Enter New Task: ")
            update_task(task_id, new_task)
        elif choice == '4':
            task_id = int(input("Enter Task ID to Mark as Done: "))
            mark_task_done(task_id)
        elif choice == '5':
            task_id = int(input("Enter Task ID to Delete: "))
            delete_task(task_id)
        elif choice == '6':
            break
        else:
            print("INVALID CHOICE!!...PLEASE TRY AGAIN...")

if __name__ == "__main__":
    main()
              
