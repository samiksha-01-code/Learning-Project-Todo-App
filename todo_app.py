from storage import load_tasks, save_tasks
from models import Task
from utils import get_choice


class TodoApp:
    def __init__(self):
        self.tasks = load_tasks()

    
    def add_task(self):
        task_to_add = input("Enter the task to add: ")
        self.tasks.append(Task(task_to_add))
        save_tasks(self.tasks)

    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("Your tasks: \n")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔️" if task.completed else " "
            print(f"{i}. [{status} ] {task.task_name}")

    
    def mark_task_completed(self):
        if not self.tasks:
            print("No tasks available to mark as completed.")
            return
        
        print(f"Select the task you want to mark as completed: ")
        self.view_tasks()

        # task_no = int(input("Enter the task number to mark as completed: "))
        task_no = get_choice()

        if 1 <= task_no <= len(self.tasks):
            if self.tasks[task_no-1].completed:
                print("Task is already marked as completed.")
            else:
                self.tasks[task_no-1].mark_completed()
                print("Task marked as completed!")
                save_tasks(self.tasks)
            # for i, task in enumerate(tasks, start=1):
            #     if i == task_no:
            #         task["completed"] = True
            #         print("task mark as completed!")
            #         break

        else:
            print("Invalid task number. Please try again.")


    def delete_task(self):
        if not self.tasks:
            print("No tasks available to delete.")
            return
        
        print("Select the task you want to delete: ")
        self.view_tasks()

        # task_no = int(input("Enter the task number to delete: "))
        task_no = get_choice()

        if 1 <= task_no <= len(self.tasks):
            deleted_task = self.tasks[task_no-1].task_name
            del self.tasks[task_no-1]
            print(f"Task deleted: {deleted_task}")
            save_tasks(self.tasks)

            # for i, _ in enumerate(tasks, start=1):
            #     if i == task_no:
            #         deleted_task = tasks[i-1]['task_name']
            #         del tasks[i-1]
            #         print(f"Task deleted: {deleted_task}")
        else:
            print("Invalid task number. Please try again.")