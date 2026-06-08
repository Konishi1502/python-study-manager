from datetime import datetime

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
    print('Task priority:')
    print('1. Low')
    print('2. Medium')
    print('3. High')
    print()

    choice = get_number_input('Set the task priority: ', 1, 3)
    if choice == 1:
        return 'Low'
    elif choice == 2:
        return 'Medium'
    else:
        return 'High'

def get_task_status_text(task):
    if task["Status"]:
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
        return f'{remaining_minutes} minutes'
    elif remaining_minutes == 0:
        return f'{hours}h'
    else:
        return f'{hours}h {remaining_minutes}min'