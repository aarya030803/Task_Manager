# main.py
from services.task_service import add_task, view_tasks, update_task, delete_task

def main_menu():
    while True:
        print("\n📋 Task Manager")
        print("A. Add Task")
        print("B. View Tasks")
        print("C. Update Task")
        print("D. Delete Task")
        print("E. Exit")

        choice = input("👉 Enter your choice: ").strip().upper()

        if choice == "A":
            add_task()
        elif choice == "B":
            view_tasks()
        elif choice == "C":
            update_task()
        elif choice == "D":
            delete_task()
        elif choice == "E":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    start = input("Do you want to start Task Manager? (y/n): ").lower()
    if start == "y":
        main_menu()
    else:
        print("👋 Program exited.")
