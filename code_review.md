# Task Tracker Code Review

## Code Quality

- [x] All functions and methods have docstrings.
  - During the review, missing docstrings were identified in the subclass methods and the `task_from_dict()` factory function. Docstrings were added to describe each method's purpose.
- [x] No unused variables or commented-out code blocks remain in the final files.
- [x] Variable and function names are descriptive and follow Python naming conventions.
  - Classes use PascalCase, while functions and variables use snake_case.

## Correctness

- [x] Adding a standard task creates a `Task` object and appends it to the `tasks` list.
- [x] Adding an urgent task creates an `UrgentTask` object with high priority and appends it to the list.
- [x] Adding a recurring task creates a `RecurringTask` object and appends it to the list.
- [x] Viewing tasks displays the task name, priority where applicable, completion status, estimated time, and subclass-specific fields such as deadline or frequency.
- [x] Completing a task correctly updates `is_complete` to `True`.
- [x] Deleting a task removes it from the list and prints the deleted task's name.
- [x] Saving writes a valid `tasks.json` file containing a `type` field for every task.
- [x] Loading restores `Task`, `UrgentTask`, and `RecurringTask` objects correctly using `task_from_dict()`.

## Edge Cases

- [x] `view_tasks()` handles an empty task list by printing `No tasks found.`
- [x] Invalid priority input is rejected by `set_priority()` without changing the current priority.
- [x] Non-numeric estimated-time input is caught with a `ValueError` handler.
- [x] Out-of-range and non-numeric task numbers are handled in `complete_task()` and `delete_task()`.
- [x] A missing or invalid JSON save file is handled without crashing the program.

## Documentation

- [x] The README contains the project description, setup instructions, usage instructions, available commands, project structure, and known bugs.
- [x] The Project Structure section lists every file in the repository.
- [x] Known bugs are documented.
  - No unresolved functional bugs are currently known after running the unit tests and manually testing the save-and-load workflow.

## Project Structure Reviewed

- `README.md` - Project overview, setup, usage, structure, and known bugs.
- `task.py` - Defines `Task`, `UrgentTask`, `RecurringTask`, `task_from_dict()`, and the polymorphism demonstration.
- `task_manager.py` - Provides the command-line task manager and JSON persistence.
- `tasks.json` - Stores serialized task data, including task type information.
- `test_task.py` - Contains unit tests for the task classes and their behavior.
- `code_review.md` - Contains this structured self-review.

> Before submission, compare this list with the repository and add any additional files that are present.

## Two Improvement I Made

-During the self-review, I found that `complete_task()` rejected the last task in the list because its range check used `< len(tasks)`. I changed the condition to `<= len(tasks)`, which allows the displayed one-based task number to include the final task while still safely accessing it with `tasks[task_number - 1]`.
-Using set_priority() method in the constructor of Task to handle the invalid priority input when creating a new task.
