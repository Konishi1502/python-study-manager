import storage
import utils
from datetime import date

def search_tasks():
    found_results = False

    if not storage.tasks:
        print('You do not have any tasks yet.')
        return
    search = input('Search: ').strip().lower()
    if not search:
        print("Please type something to search.")
        return

    print()
    print('=== Search results ===')
    print()

    for task in storage.tasks:
        title = task["Title"].lower()
        subject = task["Subject"].lower()
        description = task["Description"].lower()
        if search in title or search in subject or search in description:
            found_results = True
            status = utils.get_task_status_text(task)
            print(f'{task["Title"]} - {status}')

    if not found_results:
        print('No tasks found.')

def filter_tasks():
    if not storage.tasks:
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
            for task in storage.tasks:
                if task["Subject"] in subject_list:
                    continue
                else:
                    subject_list.append(task["Subject"])
            for index, item in enumerate(subject_list, start=1):
                print(f'{index}. {item}')
            print()
            subject_number = utils.get_number_input(
                'Select the subject you want to filter by: ',
                1,
                len(subject_list)
            )
            selected_subject = subject_list[subject_number - 1]
            print()
            print(f'=== {selected_subject} tasks ===')
            print()
            for task in storage.tasks:
                if task ["Subject"] == selected_subject:
                    status = utils.get_task_status_text(task)
                    print(f'{subject_number_tasks}. {task["Title"]} - {status}')
                    subject_number_tasks += 1
                else:
                    continue
            break

        elif filter_number == '2':
            found_results = False
            priority_number_tasks = 1
            print()
            priority_chosen = utils.choose_priority()
            print()
            print(f'=== {priority_chosen} Priority tasks ===')
            print()
            for task in storage.tasks:
                if task["Priority"] == priority_chosen:
                    found_results = True
                    status = utils.get_task_status_text(task)
                    print(f'{priority_number_tasks}. {task["Title"]} - {status}')
                    priority_number_tasks += 1
            if not found_results:
                print('No tasks found with this priority.')
            break

        elif filter_number == '3':
            break

        else:
            print('Invalid choice. Please try again.')

def overdue_tasks():
    if not storage.tasks:
        print("You do not have any tasks yet.")
        return

    today = date.today()
    found_overdue_tasks = False
    task_number = 1

    print("=== Overdue tasks ===")
    print()

    for task in storage.tasks:
        deadline = utils.convert_text_to_date(task["Deadline"])

        if deadline is None:
            continue

        if not task["Status"] and deadline < today:
            found_overdue_tasks = True
            print(f'{task_number}. {task["Title"]} - Deadline: {task["Deadline"]}')
            task_number += 1

    if not found_overdue_tasks:
        print("You do not have any overdue tasks.")
