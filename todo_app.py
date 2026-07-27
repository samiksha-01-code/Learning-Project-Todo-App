from storage import load_tasks, save_tasks
from models import Task
from utils import get_choice


class TodoApp:
    def __init__(self):
        self.tasks = load_tasks()

    
    def add_task(self):
        while True:
            try:
                task_to_add = input("Enter the task to add: ")
                self.tasks.append(Task(task_to_add))
                save_tasks(self.tasks)
                print("Task added successfully!")
                break
            except ValueError as e:
                print(e)
                print("Please enter a valid task name.")

    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("Your tasks: \n")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    
    def mark_task_completed(self):

        task = self._select_task()

        if task is None:
            return
        
        if task.completed:
            print("Task is already marked as completed.")
        else:
            task.mark_completed()
            print("Task marked as completed!")
            save_tasks(self.tasks)
        # for i, task in enumerate(tasks, start=1):
        #     if i == task_no:
        #         task["completed"] = True
        #         print("task mark as completed!")
        #         break


    def delete_task(self):

        task = self._select_task()

        if task is None:
            return
        
        self.tasks.remove(task)
        print(f"Task deleted: {task.task_name}")
        save_tasks(self.tasks)

        # for i, _ in enumerate(tasks, start=1):
        #     if i == task_no:
        #         deleted_task = tasks[i-1]['task_name']
        #         del tasks[i-1]
        #         print(f"Task deleted: {deleted_task}")


    def _select_task(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("Select a task : ")

        self.view_tasks()

        task_no = get_choice()

        if 1 <= task_no <= len(self.tasks):
            return self.tasks[task_no-1]
        
        print("Invalid task number. Please try again.")
        return None