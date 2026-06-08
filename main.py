import storage
import tasks
import reports
import filters
import sessions
import utils

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
    print('12. View overdue tasks')
    print()
    print('13. Add study session')
    print('14. View study sessions')
    print('15. Edit study session')
    print('16. Delete study session')
    print('17. Study time report')
    print('18. Weekly study report')
    print('19. Monthly study report')
    print('20. Exit')
    print()

def get_user_choice():
    choice = utils.get_number_input('Enter your choice (1-20): ', 1, 20)
    print()
    return choice

def main():
    storage.load_tasks()
    storage.load_sessions()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            print('--Add study task selected--')
            print()
            tasks.add_study_task()

        elif choice == 2:
            print('--View all tasks selected--')
            print()
            tasks.display_tasks()

        elif choice == 3:
            print('--View task details selected--')
            print()
            tasks.display_task_details()

        elif choice == 4:
            print('--View pending tasks selected--')
            print()
            tasks.display_pending_tasks()

        elif choice == 5:
            print('--View completed tasks selected--')
            print()
            tasks.display_completed_tasks()

        elif choice == 6:
            print('--Mark task as completed selected--')
            print()
            tasks.mark_task_as_completed()

        elif choice == 7:
            print('--Edit task selected--')
            print()
            tasks.edit_task()

        elif choice == 8:
            print('--Delete task selected--')
            print()
            tasks.delete_task()

        elif choice == 9:
            print('--Progress report selected--')
            print()
            reports.progress_report()

        elif choice == 10:
            print('--Search selected--')
            print()
            filters.search_tasks()

        elif choice == 11:
            print('--Filter selected--')
            print()
            filters.filter_tasks()

        elif choice == 12:
            print('--View overdue tasks selected--')
            print()
            filters.overdue_tasks()

        elif choice == 13:
            print('--Add study session selected--')
            print()
            sessions.add_study_session()

        elif choice == 14:
            print('--View study sessions selected--')
            print()
            sessions.display_sessions()

        elif choice == 15:
            print('--Edit study session selected--')
            print()
            sessions.edit_study_session()

        elif choice == 16:
            print('--Delete study session selected--')
            print()
            sessions.delete_study_session()

        elif choice == 17:
            print('--Study time report selected--')
            print()
            sessions.study_sessions_report()

        elif choice == 18:
            print('--Weekly study report selected--')
            print()
            sessions.weekly_study_report()

        elif choice == 19:
            print('--Monthly study report selected--')
            print()
            sessions.monthly_study_report()

        elif choice == 20:
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please try again.')
        print()

if __name__ == '__main__':
    main()