import json
from models import Task
TASKS_FILE = "tasks.json"


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        task_data = [task.to_dict() for task in tasks]
        json.dump(task_data, file, indent=4)


def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            task_data = json.load(file)
            return [Task.from_dict(task) for task in task_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("tasks.json data is corrupted.")
        return []
