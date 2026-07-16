class Task:
    def __init__(self, task_name, completed=False):
        self.task_name = task_name
        self.completed = completed

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
    
