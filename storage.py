import json
from pathlib import Path

tasks = []
next_task_id = 1
DATA_FILE = Path(__file__).parent / "tasks.json"

def save_tasks():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def load_tasks():
    global tasks
    global next_task_id

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        if tasks:
            next_task_id = max(task['ID'] for task in tasks) + 1
        else:
            next_task_id = 1

    except FileNotFoundError:
        tasks = []
        next_task_id = 1
    except json.JSONDecodeError:
        tasks = []
        next_task_id = 1