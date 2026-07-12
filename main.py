import json
from utils import show_menu, get_choice

def add_task(tasks):
    task_to_add = input("Enter the task to add: ")
    tasks.append({
        "task_name": task_to_add,
        "completed": False
    })
    save_tasks(tasks)


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    else:
        print("Your tasks: \n")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else ""
            print(f"{i}. [{status}] {task['task_name']}")


def mark_task_completed(tasks):
    if not tasks:
        print("No tasks available to mark as completed.")
        return
    
    print(f"Select the task you want to mark as completed: ")
    view_tasks(tasks)

    # task_no = int(input("Enter the task number to mark as completed: "))
    task_no = get_choice()

    if 1 <= task_no <= len(tasks):
        if tasks[task_no-1]["completed"]:
            print("Task is already marked as completed.")
        else:
            tasks[task_no-1]["completed"] = True
            print("Task marked as completed!")
            save_tasks(tasks)
        # for i, task in enumerate(tasks, start=1):
        #     if i == task_no:
        #         task["completed"] = True
        #         print("task mark as completed!")
        #         break

    else:
        print("Invalid task number. Please try again.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    
    print(f"Select the task you want to delete: ")
    view_tasks(tasks)

    # task_no = int(input("Enter the task number to delete: "))
    task_no = get_choice()

    if 1 <= task_no <= len(tasks):
        deleted_task = tasks[task_no-1]['task_name']
        del tasks[task_no-1]
        print(f"Task deleted: {deleted_task}")
        save_tasks(tasks)

        # for i, _ in enumerate(tasks, start=1):
        #     if i == task_no:
        #         deleted_task = tasks[i-1]['task_name']
        #         del tasks[i-1]
        #         print(f"Task deleted: {deleted_task}")
    else:
        print("Invalid task number. Please try again.")


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("tasks.json data is corrupted.")
        return []


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