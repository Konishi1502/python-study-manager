import storage
import utils

def add_study_session():
    add_subject = input('Add subject: ')
    add_topic = input('Add topic: ')
    add_duration_in_minutes = utils.get_number_input(
        'Add duration in minutes: ',
        1,
        1440
    )
    add_date = utils.get_valid_date('Add session date (dd/mm/yyyy): ')
    add_notes = input('Add notes: ')

    session = {
        'ID': storage.next_session_id,
        'Subject': add_subject,
        'Topic': add_topic,
        'Duration': add_duration_in_minutes,
        'Session date': add_date,
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
            print(f"{index}. {session['Subject']} - {session['Topic']} - {session['Duration']} minutes - {session['Session date']}")


def study_sessions_report():
    if not storage.sessions:
        print("You don't have any sessions!")
    else:
        total_minutes = 0
        subject_dict = {
        }
        for session in storage.sessions:
            total_minutes += session['Duration']
            if session['Subject'] not in subject_dict:
                subject_dict[session['Subject']] = session['Duration']
            else:
                subject_dict[session['Subject']] += session['Duration']
        print('===== Study Time Report =====')
        if total_minutes < 60:
            print(f'Total study time: {total_minutes} minutes')
        elif total_minutes == 60:
            print(f'Total study time: {total_minutes//60}h')
        else:
            print(f'Total study time: {total_minutes//60}h {total_minutes%60}min')
        print()
        print('Study time by subject')
        for key, value in subject_dict.items():
            print(f'{key}: {value} minutes')