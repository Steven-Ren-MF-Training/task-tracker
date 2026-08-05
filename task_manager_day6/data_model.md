# Task Manager Data Model

## Section 1: Task Dictionary Structure

| Field Name | Data Type | Description | Default Value |
|---|---|---|---|
| name | string | Stores the name or description of the task. | No default; entered by the user |
| priority | string | Stores the priority level of the task. | No default; entered by the user |
| is_complete | boolean | Indicates whether the task has been completed. | False |
| estimated_time | integer | Stores the estimated time required to complete the task. | No default; entered by the user |

## Section 2: Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|---|---|---|
| Add a task | add_task() | Creates a task dictionary and appends it to the tasks list. |
| View all tasks | view_tasks() | Loops through the tasks list and displays each task's information. |
| Mark a task as complete | complete_task() and is_complete | Changes the selected task's is_complete value from False to True. |
| Delete a task | delete_task() | Removes the selected task from the tasks list. |

## Section 3: Assumptions

- Tasks are stored in memory only and are lost when the program stops.
- Estimated time is entered as a whole number.
- Priority must be high, medium, or low.
- Each task is identified by its position in the task list.