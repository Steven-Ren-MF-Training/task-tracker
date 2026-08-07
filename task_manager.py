import json
from task import Task,UrgentTask,RecurringTask,task_from_dict

TASK_FILE = 'tasks.json'

tasks = []
END_MESSAGE = "End session, goodbye!"

def save_tasks():
    """Save the updated tasks list to JSON file"""
    try:
        with open(TASK_FILE, "w") as file_data:
            tasks_dict = [task.to_dict() for task in tasks]
            json.dump(tasks_dict, file_data, indent=4)
            print("tasks saved!")
    except FileNotFoundError:
            print("No saved file found. Starting with an empty task list.")


def load_tasks():
    """load tasks list to initialize"""
    global tasks
    try:
        with open(TASK_FILE, "r") as file:
            task_data = json.load(file)
            tasks = [task_from_dict(item) for item in task_data]
        print(f"Loaded {len(tasks)} task(s).")

    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")

    except json.JSONDecodeError:
        tasks = []
        print("The save file is corrupted. Starting with an empty task list.")

def add_task(name, priority, estimated_time):
    """Create a task object and add it to the global task list."""
    task = Task(name=name,priority=priority,estimated_time=estimated_time)
    tasks.append(task)
    print(f"Task added: {name}")

def view_tasks():
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def complete_task(task_number):
    """Mark the task at the specified zero-based index as complete."""
    if 0 < task_number <= len(tasks):
        tasks[task_number-1].mark_complete()
    else:
        print("Invalid task number.")


def delete_task(task_number):

    """Delete the task at the specified zero-based index."""
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number-1)
        print(f"Task deleted: {deleted_task.get_name()}")
    else:
        print("Invalid task number.")


def add_urgent_task():
    """Collect input and add an urgent task to the task list."""
    name = input("Task name: ").strip()

    try:
        estimated_time = int(
            input("Estimated time in minutes: ")
        )
    except ValueError:
        print("Estimated time must be a whole number.")
        return

    deadline = input(
        "Deadline (e.g. 2024-12-01): "
    ).strip()

    task = UrgentTask(
        name=name,
        estimated_time=estimated_time,
        deadline=deadline,
    )

    tasks.append(task)
    print(f"Urgent task added: {name}")


def add_recurring_task():
    """Collect input and add a recurring task to the task list."""
    name = input("Task name: ").strip()

    priority = input(
        "Priority (high, medium, low): "
    ).strip().lower()

    try:
        estimated_time = int(
            input("Estimated time in minutes: ")
        )
    except ValueError:
        print("Estimated time must be a whole number.")
        return

    frequency = input(
        "Frequency (e.g. daily, weekly): "
    ).strip()

    task = RecurringTask(
        name=name,
        priority=priority,
        estimated_time=estimated_time,
        frequency=frequency,
    )

    tasks.append(task)
    print(f"Recurring task added: {name}")


def run_manager():
    """Run the Task Manager until the user chooses to quit."""
    print("Welcome to the Task Manager!")

    '''Initialization'''
    load_tasks()

    while True:
        print("\nOptions: add | view | complete | delete | save | add-recurring | add-urgent | quit")
        option = input("Choose an option: ").strip().lower()

        if option == "add":
            name = input("Task name: ").strip()
            priority = input(
                "Priority (high, medium, low): "
            ).strip().lower()

            try:
                estimated_time = int(
                    input("Estimated time in minutes: ")
                )
                add_task(name, priority, estimated_time)
            except ValueError:
                print("Estimated time must be a whole number.")
        elif option == "add-urgent":
            add_urgent_task()

        elif option == "add-recurring":
            add_recurring_task()

        elif option == "view":
            view_tasks()

        elif option == "complete":
            view_tasks()

            if tasks:
                try:
                    task_number = int(
                        input("Enter task number to mark complete: ")
                    )
                    complete_task(task_number)
                except ValueError:
                    print("Task number must be a whole number.")

        elif option == "delete":
            view_tasks()

            if tasks:
                try:
                    task_number = int(
                        input("Enter task number to delete: ")
                    )
                    delete_task(task_number)
                except ValueError:
                    print("Task number must be a whole number.")
        elif option == "save":
            save_tasks()

        elif option == "quit":
            save_tasks()
            print(END_MESSAGE)
            break

        else:
            print(
                "Invalid option. Please choose add, view, "
                "complete, delete, or quit."
            )



run_manager()
