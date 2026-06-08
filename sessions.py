import storage
import utils
from datetime import date, timedelta

def add_study_session():
    add_subject = input('Add subject to your session: ')
    add_topic = input('Add topic to your session: ')
    add_duration_in_minutes = utils.get_number_input(
        'Add duration in minutes: ',
        1,
        1440
    )
    add_date = utils.get_valid_date('Add session date (dd/mm/yyyy): ')
    add_notes = input('Add notes to your session: ')

    session = {
        'ID': storage.next_session_id,
        'Subject': add_subject,
        'Topic': add_topic,
        'Duration': add_duration_in_minutes,
        'Date': add_date,
        'Notes': add_notes
    }

    storage.sessions.append(session)
    storage.next_session_id += 1
    storage.save_sessions()

def display_sessions():
    if not storage.sessions:
        print("You don't have any sessions!")

    else:
        print('=== Your sessions ===')
        print()
        for index, session in enumerate(storage.sessions, start=1):
            print(f"{index}. {session['Subject']} - {session['Topic']} - {session['Duration']} minutes - {session['Date']}")

def edit_study_session():
    display_sessions()
    if not storage.sessions:
        return
    print()

    while True:
        session_number = utils.get_number_input(
            'Select the session you want to edit: ',
            1,
            len(storage.sessions)
        )
        index = session_number - 1
        selected_session = storage.sessions[index]

        print()
        print('=== What do you want to edit? ===')
        print()
        print(f'1. Subject - {selected_session["Subject"]}')
        print(f'2. Topic - {selected_session["Topic"]}')
        print(f'3. Duration - {selected_session["Duration"]}')
        print(f'4. Date - {selected_session["Date"]}')
        print(f'5. Notes - {selected_session["Notes"]}')
        print('6. Go back')
        print()

        while True:
            details_number = utils.get_number_input('Enter your choice (1-6): ', 1, 6)
            print()

            if details_number == 1:
                print(f'Current Subject: {selected_session["Subject"]}')
                edit_subject = input('New subject: ')
                selected_session["Subject"] = edit_subject
                print()
                storage.save_sessions()
                print('Subject updated successfully!')
                break

            elif details_number == 2:
                print(f'Current Topic: {selected_session["Topic"]}')
                edit_topic = input('New topic: ')
                selected_session["Topic"] = edit_topic
                print()
                storage.save_sessions()
                print('Topic updated successfully!')
                break

            elif details_number == 3:
                print(f'Current Duration: {selected_session["Duration"]}')
                edit_duration = utils.get_number_input(
                    'Add duration in minutes: ',
                    1,
                    1440
                )
                selected_session["Duration"] = edit_duration
                print()
                storage.save_sessions()
                print('Duration updated successfully!')
                break

            elif details_number == 4:
                print(f'Current Date: {selected_session["Date"]}')
                edit_date = utils.get_valid_date('New date (dd/mm/yyyy): ')
                selected_session["Date"] = edit_date
                print()
                storage.save_sessions()
                print('Date updated successfully!')
                break

            elif details_number == 5:
                print(f'Current Notes: {selected_session["Notes"]}')
                edit_notes = input('New notes: ')
                selected_session["Notes"] = edit_notes
                print()
                storage.save_sessions()
                print('Notes updated successfully!')
                break

            elif details_number == 6:
                break

            else:
                print('Invalid choice. Please try again.')
                print()

        break

def delete_study_session():
    display_sessions()
    if not storage.sessions:
        return

    print()
    session_number = utils.get_number_input(
        'Select the session you want to delete: ',
        1,
        len(storage.sessions)
    )
    index = session_number - 1

    while True:
        confirmation = input('Are you sure you want to delete this session? yes/no: ')
        if confirmation.lower() == 'yes':
            storage.sessions.pop(index)
            storage.save_sessions()
            print('Session successfully deleted!')
            break

        elif confirmation.lower() == 'no':
            print('Delete cancelled.')
            break

        else:
            print('Invalid answer. Please try again')
            print()

def study_sessions_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    total_minutes = 0
    subject_dict = {}

    for session in storage.sessions:
        total_minutes += session["Duration"]

        subject = session["Subject"]

        if subject not in subject_dict:
            subject_dict[session['Subject']] = session['Duration']
        else:
            subject_dict[session['Subject']] += session['Duration']

    print('===== Study Time Report =====')
    print()
    print(f'Total study time: {utils.format_minutes(total_minutes)}')
    print()
    print('Study time by subject:')

    for subject, minutes in subject_dict.items():
        print(f'{subject}: {utils.format_minutes(minutes)}')

def weekly_study_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    today = date.today()
    start_date = today - timedelta(days = 7)

    weekly_sessions = []

    for session in storage.sessions:
        session_date = utils.convert_text_to_date(session["Date"])

        if session_date is None:
            continue

        if start_date <= session_date <= today:
            weekly_sessions.append(session)

    if not weekly_sessions:
        print("You don't have any study sessions from the last 7 days.")
        return

    print('===== Weekly Study Report =====')
    print()

    total_minutes = 0
    subject_dict = {}

    for session in weekly_sessions:
        total_minutes += session["Duration"]

        subject = session["Subject"]

        if subject not in subject_dict:
            subject_dict[subject] = session["Duration"]
        else:
            subject_dict[subject] += session["Duration"]

    print(f'Total study time this week: {utils.format_minutes(total_minutes)}')
    print()
    print('Study time by subject:')

    for subject, minutes in subject_dict.items():
        print(f'{subject}: {utils.format_minutes(minutes)}')

def monthly_study_report():
    if not storage.sessions:
        print("You don't have any sessions!")
        return

    today = date.today()

    monthly_sessions = []

    for session in storage.sessions:
        session_date = utils.convert_text_to_date(session["Date"])

        if session_date is None:
            continue

        if session_date.month == today.month and session_date.year == today.year:
            monthly_sessions.append(session)

    if not monthly_sessions:
        print("You don't have any study sessions from this month.")
        return

    print('===== Monthly Study Report =====')
    print()

    total_minutes = 0
    subject_dict = {}

    for session in monthly_sessions:
        total_minutes += session["Duration"]

        subject = session["Subject"]

        if subject not in subject_dict:
            subject_dict[subject] = session["Duration"]
        else:
            subject_dict[subject] += session["Duration"]

    print(f'Total study time this month: {utils.format_minutes(total_minutes)}')
    print()
    print('Study time by subject:')

    for subject, minutes in subject_dict.items():
        print(f'{subject}: {utils.format_minutes(minutes)}')