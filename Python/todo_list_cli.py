import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("📝 No tasks available.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Task '{title}' added!")
    else:
        print("⚠️ Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print(f"✅ Task '{tasks[index]['title']}' marked as done.")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== 🧾 To-Do List CLI App ====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
