# Python CLI Task Manager

A simple command-line task manager built in Python that allows users to manage daily tasks efficiently. This project focuses on clean logic, data persistence using JSON, and practical features like searching, filtering, and prioritisation.

## Features

* Add new tasks with:
  - Description
  - Priority (High / Medium / Low)
  - Due date

* View tasks:
  - All tasks
  - Completed tasks
  - Pending tasks

* Task management:
  - Mark tasks as complete/incomplete
  - Delete tasks

* Search & filtering:
  - Search tasks by keyword
  - Filter by completion status
  - View overdue tasks
  - View tasks due today

* Sorting:
  - Sort tasks by priority (High → Low)

* Data storage:
  - Tasks are saved in a local tasks.json file


## How It Works
{ 
   "description": "Finish assignment", "completed": false, "priority": "High", "due_date": "2026-04-10" 
}


## How to Run the Project

1. Clone the repository:

   git clone https://github.com/Leila-NM/python-projects.git

2. Navigate to the task manager folder:

   cd python-projects/task_manager

3. Run the program:

   python task_manager.py

## Example

Task Manager 
1. Add Task 
2. View All Tasks 
... 

Enter a task description: Submit report 
Enter priority (High / Medium / Low): High 
Enter task due date (YYYY-MM-DD): 2026-04-10

## Task Indicators

* ✓ → Completed
* ✗ → Pending
* Tasks are displayed with:
  * Priority
  * Due date

## Technologies Used

* Python
* JSON (for data persistence)
* Built-in libraries:
  * json
  * datetime

## What I Learned

* Working with file handling and JSON data
* Structuring a CLI-based application
* Implementing filtering, searching, and sorting logic
* Handling user input and validation
* Managing dates and time-based logic

## Future Improvements

* Edit existing tasks
* Add unique task IDs
* Convert to a full CLI tool using argparse
* Add unit tests
* Build a GUI version (Tkinter or web-based)

## Notes

This project was built as part of my learning journey in Python and software development. It demonstrates practical problem-solving and incremental feature development.
