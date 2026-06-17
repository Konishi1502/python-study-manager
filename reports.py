import storage
import utils
from datetime import date, timedelta


def task_report():
    if not storage.tasks:
        print("You don't have any tasks.")
        return

    print("===== Progress report =====")
    print()

    total_tasks = len(storage.tasks)
    completed_tasks = 0
    pending_tasks = 0

    high_priority_tasks = 0
    medium_priority_tasks = 0
    low_priority_tasks = 0

    for task in storage.tasks:
        if task['Status']:
            completed_tasks += 1
        else:
            pending_tasks += 1

    for task in storage.tasks:
        if task['Priority'] == "High":
            high_priority_tasks += 1
        elif task['Priority'] == "Medium":
            medium_priority_tasks += 1
        elif task['Priority'] == "Low":
            low_priority_tasks += 1

    progress = (completed_tasks / total_tasks) * 100

    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")

    if total_tasks > 0:
        print(f"Progress: {progress:.1f}%")
    else:
        print("Progress: 0%")

    print()
    print('Tasks by priority:')
    print(f"High: {high_priority_tasks}")
    print(f"Medium: {medium_priority_tasks}")
    print(f"Low: {low_priority_tasks}")

def study_sessions_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    total_minutes = 0
    subject_dict = {}

    for session in storage.sessions:
        total_minutes += session['Duration']

        subject = session['Subject']

        if subject not in subject_dict:
            subject_dict[session['Subject']] = session['Duration']
        else:
            subject_dict[session['Subject']] += session['Duration']

    print("===== Study Time Report =====")
    print()
    print(f"Total study time: {utils.format_minutes(total_minutes)}")
    print()
    print("Study time by subject:")

    for subject, minutes in subject_dict.items():
        print(f"{subject}: {utils.format_minutes(minutes)}")

def display_filtered_study_session_report(filter, filter_sessions):
    print(f"===== {filter.capitalize()} Study Report =====")
    print()

    total_minutes = 0
    subject_dict = {}

    for session in filter_sessions:
        total_minutes += session['Duration']

        subject = session['Subject']

        if subject not in subject_dict:
            subject_dict[subject] = session['Duration']
        else:
            subject_dict[subject] += session['Duration']

    print(f"Total study time this {filter[:-2]}: {utils.format_minutes(total_minutes)}")
    print()
    print("Study time by subject:")

    for subject, minutes in subject_dict.items():
        print(f"{subject}: {utils.format_minutes(minutes)}")

def weekly_study_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    today = date.today()
    start_date = today - timedelta(days = 7)

    weekly_sessions = []

    for session in storage.sessions:
        session_date = utils.convert_text_to_date(session['Date'])

        if session_date is None:
            continue

        if start_date <= session_date <= today:
            weekly_sessions.append(session)

    if not weekly_sessions:
        print("You don't have any study sessions from the last 7 days.")
        return

    display_filtered_study_session_report("weekly", weekly_sessions)

def monthly_study_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    today = date.today()

    monthly_sessions = []

    for session in storage.sessions:
        session_date = utils.convert_text_to_date(session['Date'])

        if session_date is None:
            continue

        if session_date.month == today.month and session_date.year == today.year:
            monthly_sessions.append(session)

    if not monthly_sessions:
        print("You don't have any study sessions from this month.")
        return

    display_filtered_study_session_report("monthly", monthly_sessions)

def project_report():
    if not storage.projects:
        print("You don't have any projects!")
        return

    project_status_not_started = 0
    project_status_in_progress = 0
    project_status_paused = 0
    project_status_completed = 0

    print("===== Project Report =====")
    print()
    print(f"Total projects: {len(storage.projects)}")
    for project in storage.projects:
        if project['Status'] == "Not started":
            project_status_not_started += 1

        elif project['Status'] == "In progress":
            project_status_in_progress += 1

        elif project['Status'] == "Paused":
            project_status_paused += 1

        else:
            project_status_completed += 1

    print(f"Not started: {project_status_not_started}")
    print(f"In progress: {project_status_in_progress}")
    print(f"Paused: {project_status_paused}")
    print(f"Completed: {project_status_completed}")

def project_progress_report():
    project_id = utils.choose_project()
    if project_id is None:
        print("Project not found.")
        return

    selected_project = None
    for project in storage.projects:
        if project["ID"] == project_id:
            selected_project = project
            break

    total_tasks = 0
    completed_tasks = 0
    pending_tasks = 0

    for task in storage.tasks:
        if task.get('Project ID') == project_id:
            total_tasks += 1
            if task['Status']:
                completed_tasks += 1
            else:
                pending_tasks += 1

    if total_tasks > 0:
        task_progress = (completed_tasks / total_tasks) * 100
    else:
        task_progress = 0

    total_time_spent = 0
    sessions = 0

    for session in storage.sessions:
        if session.get('Project ID') == project_id:
            sessions += 1
            total_time_spent += session['Duration']

    print()
    print("===== Project Progress =====")
    print()
    print(f"Project: {selected_project['Name']}")
    print(f"Status: {selected_project['Status']}")
    print()
    print("Tasks:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Task progress: {task_progress:.0f}%")
    print()
    print("Study time:")
    print(f"Total time spent: {utils.format_minutes(total_time_spent)}")
    print(f"Sessions: {sessions}")

def dashboard():
    print(get_dashboard_text())

def get_dashboard_text():
    pending_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0
    total_study_time = 0

    project_not_started = 0
    project_in_progress = 0
    project_paused = 0
    project_completed = 0

    today = date.today()

    for task in storage.tasks:
        if task['Status']:
            completed_tasks += 1
        else:
            pending_tasks += 1

        deadline = utils.convert_text_to_date(task['Deadline'])

        if deadline is not None and not task['Status'] and deadline < today:
            overdue_tasks += 1

    for session in storage.sessions:
        total_study_time += session['Duration']

    for project in storage.projects:
        if project['Status'] == "Not started":
            project_not_started += 1
        elif project['Status'] == "In progress":
            project_in_progress += 1
        elif project['Status'] == "Paused":
            project_paused += 1
        else:
            project_completed += 1

    lines = [
        "========== Dashboard ==========",
        "",
        "Tasks:",
        f"Total tasks: {len(storage.tasks)}",
        f"Completed: {completed_tasks}",
        f"Pending: {pending_tasks}",
        f"Overdue tasks: {overdue_tasks}",
        "",
        "Study:",
        f"Total study time: {utils.format_minutes(total_study_time)}",
        f"Sessions: {len(storage.sessions)}",
        "",
        "Projects:",
        f"Total projects: {len(storage.projects)}",
        f"Not started: {project_not_started}",
        f"In progress: {project_in_progress}",
        f"Paused: {project_paused}",
        f"Completed: {project_completed}",
    ]

    return "\n".join(lines)

def export_dashboard():
    dashboard_text = get_dashboard_text()

    with open("dashboard_report.txt", "w", encoding = "utf-8") as file:
        file.write(dashboard_text)

    print("Dashboard exported successfully to dashboard_report.txt")