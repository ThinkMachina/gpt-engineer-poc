from typing import List
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, task: Task) -> int:
        task.id = self.task_id_counter
        self.task_id_counter += 1
        self.tasks.append(task)
        return task.id

    def edit_task(self, task_id: int, name: str, description: str, due_date: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.name = name
                task.description = description
                task.due_date = due_date
                return True
        return False

    def mark_task_as_complete(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.status = True
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_tasks(self) -> List[Task]:
        return self.tasks
