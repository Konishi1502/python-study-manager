import time

#=============== Version 1 ===============
tasks = []

def display_tasks():
    print('=== Your tasks ===')
    print()
    n_task = 1
    for item in tasks:
        print(f'{n_task}. {item[0]}')
        n_task += 1
    print()

def display_pending_tasks():
    pending_indices = []
    print('=== Your pending tasks ===')
    print()
    n_task = 1
    if not tasks:
        print("You don't have any tasks!")
    for i, item in enumerate(tasks):
        if not item[2]:
            print(f'{n_task}. {item[0]}')
            pending_indices.append(i)
            n_task += 1
    elif not pending_indices:
        print('All your tasks are completed!')
    print()

def add_study_task():
    add_title = input('Add a title to your task: ')
    add_subject = input('Add a subject to your task: ')
    task_status = False
    task = [add_title, add_subject, task_status]
    tasks.append(task)
    
def display_menu():
    print('====== Study Manager ======')
    print()
    print('1. Add study task')
    print('2. View all tasks')
    print('3. View pending tasks')
    print('4. Mark task as completed')
    print('5. Delete task')
    print('6. Exit')
    print()

def get_user_choice():
    choice = input('Enter your choice (1-6): ')
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
            if not tasks:
                print("You don't have any tasks!")
            else:
                display_tasks()
                task_number = int(input('Enter the number of the task you want to see the details: '))
                print()
                if 1 <= task_number <= len(tasks):
                    index = task_number - 1
                    selected_task = tasks[index]
                    print(f'Title - {selected_task[0]}')
                    print(f'Subject - {selected_task[1]}')
                    if selected_task[2] == False:
                        print('Status - Pending')
                    else:
                        print('Status - Completed')
                else:
                    print("This task does not exist.")
            
        elif choice == '3':
            print('--View pending tasks selected--')
            print()
            display_pending_tasks()            
            
        elif choice == '4':
            print('--Mark task as completed selected--')
            print()
            if not tasks:
                print("You don't have any tasks!")
            else:
                pending_indices = []
                print('=== Your pending tasks ===')
                print()
                n_task = 1
                for i, item in enumerate(tasks):
                    if not item[2]:
                        print(f'{n_task}. {item[0]}')
                        pending_indices.append(i)
                        n_task += 1
                if not pending_indices:
                    print('All your tasks are completed!')
                else:
                    task_number = int(input('Mark task as completed: '))
                    print()        
                    if 1 <= task_number <= len(pending_indices):
                        actual_index = pending_indices[task_number - 1] 
                        tasks[actual_index][2] = True
                        print(f'Task marked as completed!')
                    else:
                        print('This task does not exist.')
                      
        elif choice == '5':
            print('--Delete task selected--')
            print()
            if not tasks:
                print("You don't have any tasks!")
            else:
                display_tasks()
                task_number = int(input('Select the task you want to delete: '))
                if 1 <= task_number <= len(tasks):
                    index = task_number - 1
                    tasks.pop(index)
            
        elif choice == '6':
            print('Exiting...')
            time.sleep(1.5)
            break
        
        else:
            print('Invalid choice. Please try again.')
        print()

if __name__ == '__main__':
    main()

    
