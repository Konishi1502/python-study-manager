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


sessions = []
next_session_id = 1
SESSIONS_FILE = Path(__file__).parent / "sessions.json"

def save_sessions():
    with open(SESSIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4, ensure_ascii=False)

def load_sessions():
    global sessions
    global next_session_id

    try:
        with open(SESSIONS_FILE, "r", encoding="utf-8") as file:
            sessions = json.load(file)

        if sessions:
            next_session_id = max(session['ID'] for session in sessions) + 1
        else:
            next_session_id = 1

    except FileNotFoundError:
        sessions = []
        next_session_id = 1
    except json.JSONDecodeError:
        sessions = []
        next_session_id = 1

projects = []
next_project_id = 1
PROJECTS_FILE = Path(__file__).parent / "projects.json"

def save_projects():
    with open(PROJECTS_FILE, "w", encoding="utf-8") as file:
        json.dump(projects, file, indent=4, ensure_ascii=False)

def load_projects():
    global projects
    global next_project_id

    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            projects = json.load(file)

        if projects:
            next_project_id = max(project['ID'] for project in projects) + 1
        else:
            next_project_id = 1
            
    except FileNotFoundError:
        projects = []
        next_project_id = 1
    except json.JSONDecodeError:
        projects = []
        next_project_id = 1