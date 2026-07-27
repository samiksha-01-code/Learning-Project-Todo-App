class Task:
    def __init__(self, task_name, completed=False):
        self.task_name = task_name
        self.completed = completed

    @property
    def task_name(self):
        return self._task_name
    
    @task_name.setter
    def task_name(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Task name cannot be empty or whitespace.")
        self._task_name = cleaned_value

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_name": self.task_name,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_name"],
            data["completed"]
        )
    
    def __str__(self):
        status = "✔" if self.completed else " "
        return f"[{status}] {self.task_name}"

    def __repr__(self):
        return f"Task(task_name={self.task_name!r}, completed={self.completed!r})"
