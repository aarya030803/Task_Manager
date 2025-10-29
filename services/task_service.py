# services/task_service.py
import re
from utils.file_handler import read_tasks, write_tasks
from models.task import Task

PRIORITY_PATTERN = re.compile(r'^(High|Medium|Low)$', re.I)

def _valid_text(value: str) -> bool:
    return bool(value and value.strip())

def _valid_priority(value: str) -> bool:
    return bool(PRIORITY_PATTERN.match(value.strip()))

def add_task():
    name = input("Enter task name: ").strip()
    if not _valid_text(name):
        print("❌ Invalid name.")
        return

    description = input("Enter task description: ").strip()
    if not _valid_text(description):
        print("❌ Invalid description.")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if not _valid_priority(priority):
        print("❌ Invalid priority.")
        return

    tasks = read_tasks()
    new_task = Task(name, description, priority)
    tasks.append(new_task)
    write_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks to update.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to update: ").strip()) - 1
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    if idx < 0 or idx >= len(tasks):
        print("❌ Invalid task number.")
        return

    old = tasks[idx]
    print("\n📌 Current Task Details:")
    print(f"1) Name       : {old.name}")
    print(f"2) Description: {old.description}")
    print(f"3) Priority   : {old.priority}")

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Description")
    print("3. Priority")
    print("4. Cancel")

    choice = input("👉 Enter choice: ").strip()
    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if not _valid_text(new_name):
            print("❌ Invalid name.")
            return
        tasks[idx].name = new_name
    elif choice == "2":
        new_desc = input("Enter new description: ").strip()
        if not _valid_text(new_desc):
            print("❌ Invalid description.")
            return
        tasks[idx].description = new_desc
    elif choice == "3":
        new_pr = input("Enter new priority (High/Medium/Low): ").strip().capitalize()
        if not _valid_priority(new_pr):
            print("❌ Invalid priority.")
            return
        tasks[idx].priority = new_pr
    elif choice == "4":
        print("❌ Update cancelled.")
        return
    else:
        print("❌ Invalid choice.")
        return

    write_tasks(tasks)
    print("✅ Task updated successfully!")

def delete_task():
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks to delete.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ").strip()) - 1
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    if idx < 0 or idx >= len(tasks):
        print("❌ Invalid task number.")
        return

    confirm = input(f"Are you sure you want to delete '{tasks[idx].name}'? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.pop(idx)
        write_tasks(tasks)
        print("✅ Task deleted successfully!")
    else:
        print("❌ Deletion cancelled.")
