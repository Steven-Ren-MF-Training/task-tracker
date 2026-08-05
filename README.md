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