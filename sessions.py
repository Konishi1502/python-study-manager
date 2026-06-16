import storage
import utils

def add_study_session():
    session_subject = input('Add subject to your session: ')
    session_topic = input('Add topic to your session: ')
    session_duration = utils.get_number_input(
        'Add duration in minutes: ',
        1,
        1440
    )
    session_date = utils.get_valid_date('Add session date (dd/mm/yyyy): ')
    session_notes = input('Add notes to your session: ')

    session = {
        'ID': storage.next_session_id,
        'Subject': session_subject,
        'Topic': session_topic,
        'Duration': session_duration,
        'Date': session_date,
        'Notes': session_notes,
        'Project ID': None
    }

    storage.sessions.append(session)
    storage.next_session_id += 1
    storage.save_sessions()


def link_session_to_project():
    display_sessions()
    if not storage.sessions:
        return

    print()
    session_number = utils.get_number_input(
        'Select the session you want to link to project: ',
        1,
        len(storage.sessions)
    )

    index = session_number - 1

    project_id = utils.choose_project()
    if project_id is None:
        return

    storage.sessions[index]['Project ID'] = project_id
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
    session_number = utils.get_number_input(
        'Select the session you want to edit: ',
        1,
        len(storage.sessions)
    )
    print()

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

    details_number = utils.get_number_input('Enter your choice (1-6): ', 1, 6)
    print()

    if details_number == 1:
        print(f'Current Subject: {selected_session["Subject"]}')
        edit_subject = input('New subject: ')
        selected_session["Subject"] = edit_subject
        print()
        storage.save_sessions()
        print('Subject updated successfully!')

    elif details_number == 2:
        print(f'Current Topic: {selected_session["Topic"]}')
        edit_topic = input('New topic: ')
        selected_session["Topic"] = edit_topic
        print()
        storage.save_sessions()
        print('Topic updated successfully!')

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

    elif details_number == 4:
        print(f'Current Date: {selected_session["Date"]}')
        edit_date = utils.get_valid_date('New date (dd/mm/yyyy): ')
        selected_session["Date"] = edit_date
        print()
        storage.save_sessions()
        print('Date updated successfully!')

    elif details_number == 5:
        print(f'Current Notes: {selected_session["Notes"]}')
        edit_notes = input('New notes: ')
        selected_session["Notes"] = edit_notes
        print()
        storage.save_sessions()
        print('Notes updated successfully!')

    elif details_number == 6:
        return

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