# Testing Checklist

This file is used to manually test the main features of the Study Manager project.

## Tasks

* [x] Add a study task
* [x] View all tasks
* [x] View task details
* [x] View pending tasks
* [x] View completed tasks
* [x] Mark a task as completed
* [x] Edit a task
* [x] Delete a task
* [x] Search tasks
* [x] Filter tasks by subject
* [x] Filter tasks by priority
* [x] View overdue tasks
* [x] Progress report

## Study Sessions

* [x] Add a study session
* [x] View study sessions
* [x] View study session details
* [x] Edit a study session
* [x] Delete a study session
* [x] View study time report
* [x] View weekly study report
* [x] View monthly study report

## Projects

* [x] Add a project
* [x] View projects
* [x] View project details
* [x] Edit a project
* [x] Delete a project
* [x] Link a task to a project
* [x] Link a study session to a project
* [x] View project progress
* [x] View project report

## Dashboard and Reports

* [x] View dashboard
* [x] Export dashboard report

## Data Persistence

* [x] Add a task, close the program, reopen it, and check if the task is still saved
* [x] Add a session, close the program, reopen it, and check if the session is still saved
* [x] Add a project, close the program, reopen it, and check if the project is still saved

## Input Validation

* [x] Try entering letters when the program asks for a number
* [x] Try entering a number outside the allowed range
* [x] Try entering an invalid date
* [x] Try entering a valid date in dd/mm/yyyy format

## Final Test

* [x] Run the full program from `main.py`
* [x] Test all menu options
* [x] Check if no unexpected errors appear
* [x] Check if all JSON files are saved correctly

## Test Summary

Version tested: Version 10

Testing status: Completed

Result: All main features were tested successfully.

Notes:

* Tasks, study sessions, and projects were tested.
* JSON save/load worked correctly.
* Reports and dashboard features worked correctly.
* Input validation worked correctly for numbers and dates.
* No major errors were found during testing.
