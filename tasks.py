from datetime import date
import storage
import utils

def add_study_task():
    task_title = input('Add a title to your task: ')
    task_subject = input('Add a subject to your task: ')
    task_description = input('Add a description to your task: ')
    task_deadline = utils.get_valid_date('Add a deadline to your task (dd/mm/yyyy): ')
    priority = utils.choose_priority()
    task_status = False
    created_date = date.today().strftime("%d/%m/%Y")
    task_completed_date = ''

    task = {
        'ID': storage.next_task_id,
        'Title': task_title,
        'Subject': task_subject,
        'Description': task_description,
        'Priority': priority,
        'Status': task_status,
        'Created date': created_date,
        'Deadline': task_deadline,
        'Completed date': task_completed_date
    }

    storage.tasks.append(task)
    storage.next_task_id += 1
    storage.save_tasks()

def display_single_task(task):
    for key, value in task.items():
        status = utils.get_task_status_text(task)
        if key == 'Status':
            print(f'{key}: {status}')
        elif key == 'Completed date':
            if value:
                print(f'{key}: {value}')
            else:
                print(f'{key}:')

        else:
            print(f'{key}: {value}')

def display_tasks():
    if not storage.tasks:
        print("You don't have any tasks!")

    else:
        print('=== Your tasks ===')
        print()
        for index, task in enumerate(storage.tasks, start=1):
            status = utils.get_task_status_text(task)
            print(f'{index}. {task["Title"]} - {status}')

def display_task_details():
    display_tasks()
    if not storage.tasks:
        return

    print()
    task_number = utils.get_number_input(
        'Select the task you want to see the details: ',
        1,
        len(storage.tasks)
    )
    print()

    index = task_number - 1
    selected_task = storage.tasks[index]

    display_single_task(selected_task)

def display_pending_tasks():
    pending_indices = []

    if not storage.tasks:
        print("You don't have any tasks!")

    else:
        print('=== Your pending tasks ===')
        print()
        for task in storage.tasks:
            if not task['Status']:
                pending_indices.append(task)

        if not pending_indices:
            print('All your tasks are completed!')
        else:
            for index, task in enumerate(pending_indices, start=1):
                print(f'{index}. {task["Title"]}')

    return pending_indices

def display_completed_tasks():
    completed_indices = []

    if not storage.tasks:
        print("You don't have any tasks!")

    else:
        print('=== Your completed tasks ===')
        print()
        for task in storage.tasks:
            if task['Status']:
                completed_indices.append(task)

        if not completed_indices:
            print("You don't have any completed tasks!")
        else:
            for index, task in enumerate(completed_indices, start=1):
                print(f'{index}. {task["Title"]}')

def mark_task_as_completed():
    pending_indices = display_pending_tasks()

    if not storage.tasks:
        return
    if not pending_indices:
        return

    print()

    task_number = utils.get_number_input(
        'Select the task you want to mark as completed: ',
        1,
        len(pending_indices)
    )

    print()
    selected_task = pending_indices[task_number - 1]
    selected_task['Status'] = True
    selected_task['Completed date'] = date.today().strftime("%d/%m/%Y")
    storage.save_tasks()
    print(f'Task marked as completed!')


def edit_task():
    display_tasks()
    if not storage.tasks:
        return

    print()
    task_number = utils.get_number_input(
        'Select the task you want to edit: ',
        1,
        len(storage.tasks)
    )
    print()

    index = task_number - 1
    selected_task = storage.tasks[index]

    display_single_task(selected_task)
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

    details_number = utils.get_number_input('Enter your choice (1-6): ', 1, 6)
    print()

    if details_number == 1:
        print(f'Current Title: {selected_task["Title"]}')
        edit_title = input('New title: ')
        selected_task["Title"] = edit_title
        print()
        storage.save_tasks()
        print('Title updated successfully!')

    elif details_number == 2:
        print(f'Current Subject: {selected_task["Subject"]}')
        edit_subject = input('New subject: ')
        selected_task["Subject"] = edit_subject
        print()
        storage.save_tasks()
        print('Subject updated successfully!')

    elif details_number == 3:
        print(f'Current Description: {selected_task["Description"]}')
        edit_description = input('New description: ')
        selected_task["Description"] = edit_description
        print()
        storage.save_tasks()
        print('Description updated successfully!')

    elif details_number == 4:
        print(f'Current Deadline: {selected_task["Deadline"]}')
        edit_deadline = utils.get_valid_date('New deadline (dd/mm/yyyy): ')
        selected_task["Deadline"] = edit_deadline
        print()
        storage.save_tasks()
        print('Deadline updated successfully!')

    elif details_number == 5:
        print(f'Current Priority: {selected_task["Priority"]}')
        print()
        selected_task["Priority"] = utils.choose_priority()
        storage.save_tasks()
        print('Priority updated successfully!')

    elif details_number == 6:
        return

def delete_task():
    display_tasks()
    if not storage.tasks:
        return

    print()
    task_number = utils.get_number_input(
        'Select the task you want to delete: ',
        1,
        len(storage.tasks)
    )
    index = task_number - 1

    while True:
        confirmation = input('Are you sure you want to delete this task? yes/no: ')
        if confirmation.lower() == 'yes':
            storage.tasks.pop(index)
            storage.save_tasks()
            print('Task successfully deleted!')
            break

        elif confirmation.lower() == 'no':
            print('Delete cancelled.')
            break

        else:
            print('Invalid answer. Please try again')
            print()