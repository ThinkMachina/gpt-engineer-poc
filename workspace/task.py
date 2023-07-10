from dataclasses import dataclass

@dataclass
class Task:
    name: str
    description: str = ""
    due_date: str = ""
    status: bool = False
