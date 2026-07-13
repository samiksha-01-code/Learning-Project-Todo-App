from utils import show_menu, get_choice
from storage import load_tasks
from task_manager import add_task, view_tasks, mark_task_completed, delete_task

def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = get_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_completed(tasks) 
        elif choice == 4: 
            delete_task(tasks)
        elif choice == 5:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()