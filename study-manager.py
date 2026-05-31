import json
from datetime import date
from pathlib import Path

#=======================
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

def add_study_task():
    global next_task_id
    add_title = input('Add a title to your task: ')
    add_subject = input('Add a subject to your task: ')
    add_description = input('Add a description to your task: ')
    add_deadline = input('Add a deadline to your task: ')
    priority = choose_priority()
    task_status = False
    created_date = date.today().strftime("%d-%m-%Y")
    completed_date = ''
    task = {
        'ID': next_task_id,
        'Title': add_title,
        'Subject': add_subject,
        'Description': add_description,
        'Priority': priority,
        'Status': task_status,
        'Created date': created_date,
        'Deadline': add_deadline,
        'Completed date': completed_date
    }
    tasks.append(task)
    next_task_id += 1
    save_tasks()

def display_tasks():
    n_task = 1
    if not tasks:
        print("You don't have any tasks!")
        print()
    else:
        print('=== Your tasks ===')
        print()
        for item in tasks:
            if not item['Status']:
                print(f'{n_task}. {item["Title"]} - Pending')
            else:
                print(f'{n_task}. {item["Title"]} - Completed')
            n_task += 1

def display_task_details():
    display_tasks()
    print()
    if not tasks:
        return
    task_number = get_number_input(
        'Select the task you want to see the details: ',
        1,
        len(tasks)
    )
    index = task_number - 1
    selected_task = tasks[index]
    for key, value in selected_task.items():
        if key == 'Status':
            if not value:
                print(f'{key}: Pending')
            else:
                print(f'{key}: Completed')
        else:
                print(f'{key}: {value}')
            
def display_pending_tasks():
    pending_indices = []
    n_task = 1
    if not tasks:
        print("You don't have any tasks!")
    else:
        print('=== Your pending tasks ===')
        print()
        for item in tasks:
            if not item['Status']:
                print(f'{n_task}. {item["Title"]}')
                pending_indices.append(item)
                n_task += 1
        if not pending_indices:
            print('All your tasks are completed!')

def display_completed_tasks():
    completed_indices = []
    n_task = 1
    if not tasks:
        print("You don't have any tasks!")
    else:
        print('=== Your completed tasks ===')
        print()
        for item in tasks:
            if item['Status']:
                print(f'{n_task}. {item["Title"]}')
                completed_indices.append(item)
                n_task += 1
        if not completed_indices:
            print("You don't have any completed tasks!")

def mark_task_as_completed():
    pending_indices = []
    n_task = 1
    if not tasks:
        print("You don't have any tasks!")
    else:
        print('=== Your pending tasks ===')
        print()
        for item in tasks:
            if not item['Status']:
                print(f'{n_task}. {item["Title"]}')
                pending_indices.append(item)
                n_task += 1
        if not pending_indices:
            print('All your tasks are completed!')
        else:
            print()
            task_number = get_number_input(
                'Select the task you want to mark as completed: ',
                1,
                len(pending_indices)
            )
            print()
            selected_task = pending_indices[task_number - 1]
            selected_task['Status'] = True
            selected_task['Completed date'] = date.today().strftime("%d-%m-%Y")
            save_tasks()
            print(f'Task marked as completed!')

def edit_task():
    display_tasks()
    print()
    while True:
        if not tasks:
            break
        else:
            task_number = get_number_input(
                'Select the task you want to see the details: ',
                1,
                len(tasks)
            )
            print()
            index = task_number - 1
            selected_task = tasks[index]
            for key, value in selected_task.items():
                if key == 'Status':
                    if not value:
                        print(f'{key}: Pending')
                    else:
                        print(f'{key}: Completed')
                elif key == 'Completed date':
                    if not value:
                        print(f'{key}:')
                    else:
                        print(f'{key}: {value}')
                else:
                    print(f'{key}: {value}')
            print()
            print('=== What do you want to edit? ===')
            print()
            print(f'1. Title - {selected_task["Title"]}')
            print(f'2. Subject - {selected_task["Subject"]}')
            print(f'3. Description - {selected_task["Description"]}')
            print(f'4. Deadline - {selected_task["Deadline"]}')
            print(f'5. Priority - {selected_task["Priority"]}')
            print('6. Go back')
            print()
            while True:
                details_number = input('Enter your choice (1-6): ')
                print()
                if details_number == '1':
                    print(f'Current Title: {selected_task["Title"]}')
                    edit_title = input('New title: ')
                    selected_task["Title"] = edit_title
                    print()
                    save_tasks()
                    print('Title updated successfully!')
                    break
                elif details_number == '2':
                    print(f'Current Subject: {selected_task["Subject"]}')
                    edit_subject = input('New subject: ')
                    selected_task["Subject"] = edit_subject
                    print()
                    save_tasks()
                    print('Subject updated successfully!')
                    break
                elif details_number == '3':
                    print(f'Current Description: {selected_task["Description"]}')
                    edit_description = input('New description: ')
                    selected_task["Description"] = edit_description
                    print()
                    save_tasks()
                    print('Description updated successfully!')
                    break
                elif details_number == '4':
                    print(f'Current Deadline: {selected_task["Deadline"]}')
                    edit_deadline = input('New deadline: ')
                    selected_task["Deadline"] = edit_deadline
                    print()
                    save_tasks()
                    print('Deadline updated successfully!')
                    break
                elif details_number == '5':
                    print(f'Current Priority: {selected_task["Priority"]}')
                    print()
                    selected_task["Priority"] = choose_priority()
                    save_tasks()
                    print('Priority updated successfully!')
                    break
                elif details_number == '6':
                    break
                else:
                    print('Invalid choice. Please try again.')
                    print()
        break

def delete_task():
    display_tasks()
    print()
    if not tasks:
        return
    task_number = get_number_input(
        'Select the task you want to see the details: ',
        1,
        len(tasks)
    )
    index = task_number - 1
    while True:
        confirmation = input('Are you sure you want to delete this task? yes/no: ')
        if confirmation.lower() == 'yes':
            tasks.pop(index)
            save_tasks()
            print('Task successfully deleted!')
            break
        elif confirmation.lower() == 'no':
            print('Delete cancelled.')
            break
        else:
            print('Invalid answer. Please try again')
            print()

def progress_report():
    print('===== Progress report =====')
    print()
    if not tasks:
        print('You do not have any tasks yet.')
        return
    total_tasks = len(tasks)
    completed_tasks = 0
    pending_tasks = 0
    high_priority_tasks = 0
    medium_priority_tasks = 0
    low_priority_tasks = 0
    for task in tasks:
        if task["Status"]:
            completed_tasks += 1
        else:
            pending_tasks += 1
    for task in tasks:
        if task["Priority"] == "High":
            high_priority_tasks += 1
        elif task["Priority"] == "Medium":
            medium_priority_tasks += 1
        elif task["Priority"] == "Low":
            low_priority_tasks += 1
    progress = (completed_tasks / total_tasks) * 100
    print(f'Total tasks: {total_tasks}')
    print(f'Completed tasks: {completed_tasks}')
    print(f'Pending tasks: {pending_tasks}')
    if total_tasks > 0:
        print(f'Progress: {progress:.1f}%')
    else:
        print('Progress: 0%')
    print()
    print('Tasks by priority:')
    print(f'High: {high_priority_tasks}')
    print(f'Medium: {medium_priority_tasks}')
    print(f'Low: {low_priority_tasks}')

def search_tasks():
    if not tasks:
        print('You do not have any tasks yet.')
        return
    search = input('Search: ').strip().lower()
    if not search:
        print("Please type something to search.")
        return
    print()
    found_results = False
    print('=== Search results ===')
    print()
    for task in tasks:
        title = task["Title"].lower()
        subject = task["Subject"].lower()
        description = task["Description"].lower()
        if search in title or search in subject or search in description:
            found_results = True
            if task["Status"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f'{task["Title"]} - {status}')
    if not found_results:
        print('No tasks found.')

def filter_tasks():
    if not tasks:
        print('You do not have any tasks yet.')
        return
    print('=== Filter tasks ===')
    print()
    print('1. Filter by subject')
    print('2. Filter by priority')
    print('3. Go back')
    print()
    while True:
        filter_number = input('Enter your choice (1-3): ')
        if filter_number == '1':
            subject_list = []
            subject_number_tasks = 1
            print()
            print('=== Subjects ===')
            print()
            for task in tasks:
                if task["Subject"] in subject_list:
                    continue
                else:
                    subject_list.append(task["Subject"])
            for index, item in enumerate(subject_list, start=1):
                print(f'{index}. {item}')
            print()
            subject_number = get_number_input(
                'Select the subject you want to filter by: ',
                1,
                len(subject_list)
            )
            selected_subject = subject_list[subject_number - 1]
            print()
            print(f'=== {selected_subject} tasks ===')
            print()
            for task in tasks:
                if task ["Subject"] == selected_subject:
                    if task["Status"]:
                        print(f'{subject_number_tasks}. {task["Title"]} - Completed')
                        subject_number_tasks += 1
                    else:
                        print(f'{subject_number_tasks}. {task["Title"]} - Pending')
                        subject_number_tasks += 1
                else:
                    continue
            break
        elif filter_number == '2':
            found_results = False
            priority_number_tasks = 1
            print()
            priority_chosen = choose_priority()
            print()
            print(f'=== {priority_chosen} Priority tasks ===')
            print()
            for task in tasks:
                if task["Priority"] == priority_chosen:
                    found_results = True
                    if task["Status"]:
                        print(f'{priority_number_tasks}. {task["Title"]} - Completed')
                        priority_number_tasks += 1
                    else:
                        print(f'{priority_number_tasks}. {task["Title"]} - Pending')
                        priority_number_tasks += 1
            if not found_results:
                print('No tasks found with this priority.')
                break
        elif filter_number == '3':
            break
        else:
            print('Invalid choice. Please try again.')

def display_menu():
    print('========== Study Manager ==========')
    print()
    print('1. Add study task')
    print('2. View all tasks')
    print('3. View task details')
    print('4. View pending tasks')
    print('5. View completed tasks')
    print('6. Mark task as completed')
    print('7. Edit task')
    print('8. Delete task')
    print('9. Progress report')
    print('10. Search tasks')
    print('11. Filter tasks')
    print('12. Exit')
    print()

def get_user_choice():
    choice = input('Enter your choice (1-12): ')
    print()
    return choice

def main():
    load_tasks()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            print('--Add study task selected--')
            print()
            add_study_task()

        elif choice == '2':
            print('--View all tasks selected--')
            print()
            display_tasks()

        elif choice == '3':
            print('--View task details selected--')
            print()
            display_task_details()

        elif choice == '4':
            print('--View pending tasks selected--')
            print()
            display_pending_tasks()

        elif choice == '5':
            print('--View completed tasks selected--')
            print()
            display_completed_tasks()

        elif choice == '6':
            print('--Mark task as completed selected--')
            print()
            mark_task_as_completed()
            
        elif choice == '7':
            print('--Edit task selected--')
            print()
            edit_task()
                      
        elif choice == '8':
            print('--Delete task selected--')
            print()
            delete_task()

        elif choice == '9':
            print('--Progress report selected--')
            print()
            progress_report()


        elif choice == '10':
            print('--Search selected--')
            print()
            search_tasks()

        elif choice == '11':
            print('--Filter selected--')
            print()
            filter_tasks()
            
        elif choice == '12':
            print('Exiting...')
            break
        
        else:
            print('Invalid choice. Please try again.')
        print()

if __name__ == '__main__':
    main()

    
