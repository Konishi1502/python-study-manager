import storage
import utils

def add_project():
    project_name = input("Add project name: ")
    project_description = input("Add project description: ")
    project_status = utils.choose_project_status()
    technologies = input("Add project technologies: ")
    github_link = input("Add project github link: ")
    project_notes = input("Add project notes: ")
    start_date = utils.get_valid_date("Add project start date (dd/mm/yyyy): ")
    project_deadline = utils.get_valid_date("Add a deadline to your project (dd/mm/yyyy): ")

    project = {
        'ID': storage.next_project_id,
        'Name': project_name,
        'Description': project_description,
        'Status': project_status,
        'Technologies': technologies,
        'Github Link': github_link,
        'Notes': project_notes,
        'Start Date': start_date,
        'Deadline': project_deadline
    }

    storage.projects.append(project)
    storage.next_project_id += 1
    storage.save_projects()

def display_single_project(project):
    for key, value in project.items():
        print(f"{key}: {value}")

def display_projects():
    if not storage.projects:
        print("You haven't added any projects yet!")

    else:
        print('=== Your projects ===')
        print()
        for index, project in enumerate(storage.projects, start=1):
            print(f"{index}. {project['Name']} - {project['Status']}")

def display_project_details():
    display_projects()
    if not storage.projects:
        return
    print()
    project_number = utils.get_number_input(
        "Select the project you want to see the details: ",
        1,
        len(storage.projects)
    )
    print()

    index = project_number - 1
    selected_project = storage.projects[index]

    display_single_project(selected_project)

def edit_project():
    display_projects()
    if not storage.projects:
        return
    print()
    project_number = utils.get_number_input(
        "Select the project you want to edit: ",
        1,
        len(storage.projects)
    )
    print()

    index = project_number - 1
    selected_project = storage.projects[index]

    display_single_project(selected_project)

    print("=== What do you want to edit? ===")
    print()
    print(f"1. Name - {selected_project['Name']}")
    print(f"2. Description - {selected_project['Description']}")
    print(f"3. Status - {selected_project['Status']}")
    print(f"4. Technologies - {selected_project['Technologies']}")
    print(f"5. Github Link - {selected_project['Github Link']}")
    print(f"6. Notes - {selected_project['Notes']}")
    print(f"7. Start Date - {selected_project['Start Date']}")
    print(f"8. Deadline - {selected_project['Deadline']}")
    print("9. Go back")

    details_number = utils.get_number_input("Enter your choice (1-9): ", 1, 9)
    print()

    if details_number == 1:
        print(f"Current project name: {selected_project['Name']}")
        edit_name = input("Enter new project name: ")
        selected_project['Name'] = edit_name
        storage.save_projects()
        print()
        print("Name updated successfully!")

    elif details_number == 2:
        print(f"Current project description: {selected_project['Description']}")
        edit_description = input("Enter new project description: ")
        selected_project['Description'] = edit_description
        storage.save_projects()
        print()
        print("Description updated successfully!")

    elif details_number == 3:
        print(f"Current project status: {selected_project['Status']}")
        selected_project['Status'] = utils.choose_project_status()
        storage.save_projects()
        print()
        print("Status updated successfully!")

    elif details_number == 4:
        print(f"Current project technologies: {selected_project['Technologies']}")
        edit_technologies = input("Enter new project technologies: ")
        selected_project['Technologies'] = edit_technologies
        storage.save_projects()
        print()
        print("Technologies updated successfully!")

    elif details_number == 5:
        print(f"Current project github link: {selected_project['Github Link']}")
        edit_github_link = input("Enter new project github link: ")
        selected_project['Github Link'] = edit_github_link
        storage.save_projects()
        print()
        print("Github link updated successfully!")

    elif details_number == 6:
        print(f"Current project notes: {selected_project['Notes']}")
        edit_notes = input("Enter new project notes: ")
        selected_project['Notes'] = edit_notes
        storage.save_projects()
        print()
        print("Notes updated successfully!")

    elif details_number == 7:
        print(f"Current project start date: {selected_project['Start Date']}")
        edit_start_date = utils.get_valid_date("Enter new project start date (dd/mm/yyyy): ")
        selected_project['Start Date'] = edit_start_date
        storage.save_projects()
        print()
        print("Start date updated successfully!")

    elif details_number == 8:
        print(f"Current project deadline: {selected_project['Deadline']}")
        edit_deadline = utils.get_valid_date("Enter new project deadline (dd/mm/yyyy): ")
        selected_project['Deadline'] = edit_deadline
        storage.save_projects()
        print()
        print("Deadline updated successfully!")

    elif details_number == 9:
        return

def delete_project():
    display_projects()
    if not storage.projects:
        return

    print()
    project_number = utils.get_number_input(
        "Select the project you want to delete: ",
        1,
        len(storage.projects)
    )
    print()

    index = project_number - 1
    selected_project = storage.projects[index]

    while True:
        confirmation = input(f"Are you sure you want to delete {selected_project['Name']}? (yes/no): ")
        if confirmation.lower() == "yes":
            storage.projects.pop(index)
            storage.save_projects()
            print()
            print("Project deleted successfully!")
            break

        elif confirmation.lower() == "no":
            print("Delete cancelled.")
            break

        else:
            print("Invalid answer. Please try again")
            print()