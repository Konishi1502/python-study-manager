from datetime import datetime
import storage
import os

def get_number_input(message, min_value = None, max_value = None):
    while True:
        try:
            number = int(input(message))

            if min_value is not None and number < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue

            if max_value is not None and number > max_value:
                print(f"Please enter a number less than or equal to {max_value}.")
                continue

            return number

        except ValueError:
            print("Please enter a valid number.")

def get_valid_date(message):
    while True:
        date_text = input(message)

        try:
            valid_date = datetime.strptime(date_text, "%d/%m/%Y")
            return valid_date.strftime("%d/%m/%Y")

        except ValueError:
            print("Invalid date. Please use dd/mm/yyyy.")
            print()

def choose_priority():
    print("Task priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print()

    choice = get_number_input("Set the task priority: ", 1, 3)
    if choice == 1:
        return "Low"
    elif choice == 2:
        return "Medium"
    else:
        return "High"

def choose_project_status():
    print("Project status:")
    print("1. Not started")
    print("2. In progress")
    print("3. Paused")
    print("4. Completed")

    choice = get_number_input("Set the project status: ", 1, 4)
    if choice == 1:
        return "Not started"
    elif choice == 2:
        return "In progress"
    elif choice == 3:
        return "Paused"
    else:
        return "Completed"

def choose_project():
    if not storage.projects:
        print("You haven't added any projects yet!")
        return None

    print("=== Your projects ===")

    print()
    for index, project in enumerate(storage.projects, start=1):
        print(f"{index}. {project['Name']} - {project['Status']}")
    print()

    choice = get_number_input(
        "Select a project: ",
        1,
        len(storage.projects)
    )

    selected_project = storage.projects[choice - 1]

    return selected_project['ID']

def get_task_status_text(task):
    if task['Status']:
        status = "Completed"
        return status
    else:
        status = "Pending"
        return status

def convert_text_to_date(date_text):
    try:
        return datetime.strptime(date_text, "%d/%m/%Y").date()
    except ValueError:
        return None

def format_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours == 0:
        return f"{remaining_minutes} minutes"
    elif remaining_minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {remaining_minutes}min"

def pause():
    input("\nPress Enter to continue...")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")