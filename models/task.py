# models/task.py
class Task:
    def __init__(self, name: str, description: str, priority: str):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.name} | {self.description} | Priority: {self.priority}"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["description"], data["priority"])
