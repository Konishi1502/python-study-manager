import storage

def progress_report():
    if not storage.tasks:
        print('You do not have any tasks yet.')
        return

    print('===== Progress report =====')
    print()

    total_tasks = len(storage.tasks)
    completed_tasks = 0
    pending_tasks = 0

    high_priority_tasks = 0
    medium_priority_tasks = 0
    low_priority_tasks = 0

    for task in storage.tasks:
        if task["Status"]:
            completed_tasks += 1
        else:
            pending_tasks += 1

    for task in storage.tasks:
        if task["Priority"] == "High":
            high_priority_tasks += 1
        elif task["Priority"] == "Medium":
            medium_priority_tasks += 1
        elif task["Priority"] == "Low":
            low_priority_tasks += 1

    progress = (completed_tasks / total_tasks) * 100

    print(f'Total tasks: {total_tasks}')
    print(f'Completed tasks: {completed_tasks}')
    print(f'Pending tasks: {pending_tasks}')

    if total_tasks > 0:
        print(f'Progress: {progress:.1f}%')
    else:
        print('Progress: 0%')

    print()
    print('Tasks by priority:')
    print(f'High: {high_priority_tasks}')
    print(f'Medium: {medium_priority_tasks}')
    print(f'Low: {low_priority_tasks}')