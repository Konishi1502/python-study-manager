import storage
import tasks
import reports
import filters
import sessions
import utils
import projects

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
    print('9. Search tasks')
    print('10. Filter tasks')
    print('11. View overdue tasks')
    print('12. Progress report')
    print()
    print('13. Add study session')
    print('14. View study sessions')
    print('15. View study session details')
    print('16. Edit study session')
    print('17. Delete study session')
    print('18. Study time report')
    print('19. Weekly study report')
    print('20. Monthly study report')
    print()
    print('21. Add project')
    print('22. Link task to project')
    print('23. Link session to project')
    print('24. View projects')
    print('25. View project details')
    print('26. View project progress')
    print('27. Edit project')
    print('28. Delete project')
    print('29. Project report')
    print()
    print('30. Dashboard')
    print('31. Export dashboard')
    print('32. Exit')
    print()

def get_user_choice():
    choice = utils.get_number_input('Enter your choice (1-32): ', 1, 32)
    print()
    return choice

def main():
    storage.load_tasks()
    storage.load_sessions()
    storage.load_projects()

    while True:
        utils.clear_screen()
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            print('--Add study task selected--')
            print()
            tasks.add_study_task()
            utils.pause()

        elif choice == 2:
            print('--View all tasks selected--')
            print()
            tasks.display_tasks()
            utils.pause()

        elif choice == 3:
            print('--View task details selected--')
            print()
            tasks.display_task_details()
            utils.pause()

        elif choice == 4:
            print('--View pending tasks selected--')
            print()
            tasks.display_pending_tasks()
            utils.pause()

        elif choice == 5:
            print('--View completed tasks selected--')
            print()
            tasks.display_completed_tasks()
            utils.pause()

        elif choice == 6:
            print('--Mark task as completed selected--')
            print()
            tasks.mark_task_as_completed()
            utils.pause()

        elif choice == 7:
            print('--Edit task selected--')
            print()
            tasks.edit_task()
            utils.pause()

        elif choice == 8:
            print('--Delete task selected--')
            print()
            tasks.delete_task()
            utils.pause()

        elif choice == 9:
            print('--Search selected--')
            print()
            filters.search_tasks()
            utils.pause()

        elif choice == 10:
            print('--Filter selected--')
            print()
            filters.filter_tasks()
            utils.pause()

        elif choice == 11:
            print('--View overdue tasks selected--')
            print()
            filters.overdue_tasks()
            utils.pause()

        elif choice == 12:
            print('--Progress report selected--')
            print()
            reports.task_report()
            utils.pause()

        elif choice == 13:
            print('--Add study session selected--')
            print()
            sessions.add_study_session()
            utils.pause()

        elif choice == 14:
            print('--View study sessions selected--')
            print()
            sessions.display_sessions()
            utils.pause()

        elif choice == 15:
            print('--View study session details--')
            print()
            sessions.display_session_details()
            utils.pause()

        elif choice == 16:
            print('--Edit study session selected--')
            print()
            sessions.edit_study_session()
            utils.pause()

        elif choice == 17:
            print('--Delete study session selected--')
            print()
            sessions.delete_study_session()
            utils.pause()

        elif choice == 18:
            print('--Study time report selected--')
            print()
            reports.study_sessions_report()
            utils.pause()

        elif choice == 19:
            print('--Weekly study report selected--')
            print()
            reports.weekly_study_report()
            utils.pause()

        elif choice == 20:
            print('--Monthly study report selected--')
            print()
            reports.monthly_study_report()
            utils.pause()

        elif choice == 21:
            print('--Add project selected--')
            print()
            projects.add_project()
            utils.pause()

        elif choice == 22:
            print('--Link task to project selected--')
            print()
            tasks.link_task_to_project()
            utils.pause()

        elif choice == 23:
            print('--Link session to project selected--')
            print()
            sessions.link_session_to_project()
            utils.pause()

        elif choice == 24:
            print('--View project selected--')
            print()
            projects.display_projects()
            utils.pause()

        elif choice == 25:
            print('--View project details selected--')
            print()
            projects.display_project_details()
            utils.pause()

        elif choice == 26:
            print('--View project progress selected--')
            print()
            reports.project_progress_report()
            utils.pause()

        elif choice == 27:
            print('--Edit project selected--')
            print()
            projects.edit_project()
            utils.pause()

        elif choice == 28:
            print('--Delete project selected--')
            print()
            projects.delete_project()
            utils.pause()

        elif choice == 29:
            print('--Project report selected--')
            print()
            reports.project_report()
            utils.pause()

        elif choice == 30:
            print('--Dashboard selected--')
            print()
            reports.dashboard()
            utils.pause()

        elif choice == 31:
            print('--Export dashboard selected--')
            print()
            reports.export_dashboard()
            utils.pause()

        elif choice == 32:
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please try again.')
        print()

if __name__ == '__main__':
    main()