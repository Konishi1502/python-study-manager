from datetime import date

#=======================
tasks = []
next_task_id = 1

def add_study_task():
    global next_task_id
    add_title = input('Add a title to your task: ')
    add_subject = input('Add a subject to your task: ')
    add_description = input('Add a description to your task: ')
    add_deadline = input('Add a deadline to your task: ')
    print()
    print('Task priority:')
    print('1. Low')
    print('2. Medium')
    print('3. High')
    print()
    while True:
        add_priority = input('Set the task priority: ')
        if add_priority == '1':
            priority = 'Low'
            break
        elif add_priority == '2':
            priority = 'Medium'
            break
        elif add_priority == '3':
            priority = 'High'
            break
        else:
            print('Invalid choice. Please try again.')
            print()
    task_status = False
    created_date = date.today().strftime("%d-%m-%Y")
    completed_date = ' '
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
        print(end=' ')
    else:
        task_number = int(input('Select the task you want to see the details: '))
        print()
        if 1 <= task_number <= len(tasks):
            index = task_number - 1
            selected_task = tasks[index]
            for key, value in selected_task.items():
                if key == 'Status':
                    if value == False:
                        print(f'{key}: Pending')
                    else:
                        print(f'{key}: Completed')
                else:    
                    print(f'{key}: {value}')
        else:
            print('This task does not exist.')
            
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
            if item['Status'] == True:
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
            task_number = int(input('Mark task as completed: '))
            print()        
            if 1 <= task_number <= len(pending_indices):
                actual_index = pending_indices[task_number - 1] 
                actual_index['Status'] = True
                actual_index['Completed date'] = date.today().strftime("%d-%m-%Y")
                print(f'Task marked as completed!')
            else:
                print('This task does not exist.')

def edit_task():
    display_tasks()
    print()
    while True:
        if not tasks:
            break
        else:
            task_number = int(input('Select the task you want to edit the details: '))
            print()
            if 1 <= task_number <= len(tasks):
                index = task_number - 1
                selected_task = tasks[index]
                for key, value in selected_task.items():
                    if key == 'Status':
                        if value == False:
                            print(f'{key}: Pending')
                        else:
                            print(f'{key}: Completed')
                    elif key == 'Completed date':
                        if value == False:
                            print(f'{key}: ')
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
                    details_number = input('Enter your choice: ')
                    print()
                    if details_number == '1':
                        print(f'Current Title: {selected_task["Title"]}')
                        edit_title = input('New title: ')
                        selected_task["Title"] = edit_title
                        print()
                        print('Title updated successfully!')
                        break
                    elif details_number == '2':
                        print(f'Current Subject: {selected_task["Subject"]}')
                        edit_subject = input('New subject: ')
                        selected_task["Subject"] = edit_subject
                        print()
                        print('Subject updated successfully!')
                        break
                    elif details_number == '3':
                        print(f'Current Description: {selected_task["Description"]}')
                        edit_description = input('New description: ')
                        selected_task["Description"] = edit_description
                        print()
                        print('Description updated successfully!')
                        break
                    elif details_number == '4':
                        print(f'Current Deadline: {selected_task["Deadline"]}')
                        edit_deadline = input('New deadline: ')
                        selected_task["Deadline"] = edit_deadline
                        print()
                        print('Deadline updated successfully!')
                        break
                    elif details_number == '5':
                        print(f'Current Priority: {selected_task["Priority"]}')
                        print()
                        print('Task priority:')
                        print('1. Low')
                        print('2. Medium')
                        print('3. High')
                        print()
                        while True:
                            add_priority = input('Change task priority: ')
                            if add_priority == '1':
                                edited_priority = 'Low'
                                break
                            elif add_priority == '2':
                                edited_priority = 'Medium'
                                break
                            elif add_priority == '3':
                                edited_priority = 'High'
                                break
                            else:
                                print('Invalid choice. Please try again.') 
                        selected_task["Priority"] = edited_priority
                        print()
                        print('Priority updated successfully!')                        
                        break
                    elif details_number == '6':
                        break
                    else:
                        print('Invalid choice. Please try again.')
                        print()
            else:
                print('This task does not exist.')
            break

def delete_task():
    display_tasks()
    print()
    if not tasks:
        print(end=' ')
    else:
        task_number = int(input('Select the task you want to delete: '))
        if 1 <= task_number <= len(tasks):
            index = task_number - 1
            while True:
                confirmation = input('Are you sure you want to delete this task? yes/no: ')
                if confirmation.lower() == 'yes':
                    tasks.pop(index)
                    print('Task successfully deleted!')
                    break
                elif confirmation.lower() == 'no':
                    break
                else:
                    print('Invalid answer. Please try again')
                    print()
        else:
            print('This task does not exist.')
    
def display_menu():
    print('========= Study Manager =========')
    print()
    print('1. Add study task')
    print('2. View all tasks')
    print('3. View task details')
    print('4. View pending tasks')
    print('5. View completed tasks')
    print('6. Mark task as completed')
    print('7. Edit task')
    print('8. Delete task')
    print('9. Exit')
    print()

def get_user_choice():
    choice = input('Enter your choice (1-9): ')
    print()
    return choice

def main():
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
            print('Exiting...')
            break
        
        else:
            print('Invalid choice. Please try again.')
        print()

if __name__ == '__main__':
    main()

    
