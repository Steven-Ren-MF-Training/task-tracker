# Project Structure

## WEEK1:
* `task_tracker_refactor/greet_user.py`: Displays the welcome message to the user.
* `task_tracker_refactor/get_task_input.py`: Collects the task name from user input.
* `task_tracker_refactor/get_priority_input.py`: Collects the task priority from user input.
* `task_tracker_refactor/check_priority.py`: Returns the appropriate priority message based on the input value.
* `task_tracker_refactor/run_tracker.py`: Combines all functions and controls the program using a `while` loop.




## Week 2 Progress
### Day 1:
* `task_manager_day6/task_manager.py`: A task manager allows user add/delete/complete/view the task list.
### Day 2:
* `task_manager_day6/task_manager.py`: A task manager allows user add/delete/complete/view the task list.
* `task_manager_day6/tasks,json` : A json file used to save the task list.

Adding file persistence allows the Task Manager 
to save tasks between program sessions instead of losing all task data when the program closes. 
Without catching FileNotFoundError, the program would crash the first time it runs 
if tasks.json does not exist. Error handling supports the QA mindset because it considers invalid inputs and unexpected situations before they cause failures. 
It helps make the program more reliable and improves the user experience.

### Day 3:
* `task.py` : Task class which encapsulates the task with method and attribute.
* `task_manager_day6/task_manager.py`: Update the task_manager_day6/task_manager.py using task object

The Task Manager was refactored so that each task is now represented by a Task object instead of a plain dictionary. 
Encapsulation protects the priority and completion status by storing them as private attributes and controlling access through getters, setters, and methods. 
The to_dict() method is needed because custom Task objects cannot be written directly to JSON. 
The from_dict() class method converts the saved JSON dictionary data back into Task objects when the program starts.

### Day 4:
* `task.py` : Implementation of Inheritance/polymorpysim to edit RecurringTask and UrgentTask Subtask
* `task_manager_day6/task_manager.py`: Update the task_manager_day6/task_manager.py and implement add urgent task and add recurring task feature

### Day 5:
* `test_task.py` : Added unit tests using Python's built-in unittest module to test Task, UrgentTask, and RecurringTask functionality.
* `code_review.py` : Documenting the review of Code and improvement
* Reorganized the project file structure by moving the final task_manager.py / tasks.json from the task_manager_day6 folder to the project root directory.
* Updated file paths and imports so the final project structure is cleaner and easier to run.
* Ran all required unit tests and verified that the Task Manager behaves correctly before release.

## Project Structure:
* README.md — Project documentation.
* task.py — Defines the Task, UrgentTask, and RecurringTask classes.
* task_manager.py — Main CLI Task Manager application.
* test_task.py — Unit tests written using Python's built-in unittest module.
* test_results.txt — Stores the final unit test results.
* code_review.md — Contains the self-review and release readiness checklist.
* bug_report.md — Documents known bugs and issues.
* data_model.md — Documents the Task Manager data model.
* tasks.json — Stores task data using JSON persistence.


