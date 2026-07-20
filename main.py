from utils import show_menu, get_choice
from todo_app import TodoApp

def main():
    app = TodoApp()

    while True:
        show_menu()

        choice = get_choice()

        if choice == 1:
            app.add_task()
        elif choice == 2:
            app.view_tasks()
        elif choice == 3:
            app.mark_task_completed() 
        elif choice == 4: 
            app.delete_task()
        elif choice == 5:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()