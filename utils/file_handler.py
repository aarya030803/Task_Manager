# utils/file_handler.py
import json
from models.task import Task

FILE_NAME = "tasks.json"

def read_tasks(filepath=FILE_NAME):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_tasks = json.load(f)
            return [Task.from_dict(t) for t in raw_tasks]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Could not decode task data. File might be corrupted.")
        return []

def write_tasks(tasks, filepath=FILE_NAME):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)
