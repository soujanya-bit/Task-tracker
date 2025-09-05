# Task Tracker CLI

## Overview
A simple command-line based to-do list application using Python.
Users can add tasks with a title and optional description, view tasks with their IDs, mark tasks as completed, delete tasks, and persist tasks in a `tasks.json` file.

# How to run:
1. Ensure you have python 3 installed.
2. Navigate to 'task-tracker' folder.
3. Run in terminal or cmd: python main.py

# Implemented Features:
1. Add a Task - User can add a task by providing a title and an optional description.
2. List Tasks - Display all tasks with their ID, title, description , and status (Pending/Completed).
3. Mark Task as Completed - Allow the user to update the status of a task to 'Completed' using the task ID.
4. Delete Task - Allow the user to delete a task using its ID.
5. Data Persistence - Tasks should be stored and loaded from a local tasks.json file.
6. Added support for due dates and to sort tasks by due date.

# Challenges Faced:
1. Initially used list indices instead of IDs, but implemented unique IDs using max ID + 1.
2. Fixed a few “Invalid Task ID” messages by moving error handling outside loops.
3. Added title validation to prevent empty tasks, improving user experience.
