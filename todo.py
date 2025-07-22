import os
import json

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty!")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
