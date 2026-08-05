import json

TASK_FILE = 'tasks.json'

tasks = []
END_MESSAGE = "End session, goodbye!"

def save_tasks():
    """Save the updated tasks list to JSON file"""
    try:
        with open(TASK_FILE, "w") as file_data:
            json.dump(tasks, file_data, indent=4)
            print("tasks saved!")
    except FileNotFoundError:
            print("No saved file found. Starting with an empty task list.")


def load_tasks():
    """load tasks list to initialize"""
    global tasks
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)

        print(f"Loaded {len(tasks)} task(s).")

    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")

    except json.JSONDecodeError:
        tasks = []
        print("The save file is corrupted. Starting with an empty task list.")

def add_task(name, priority, estimated_time):
    """Create a task dictionary and add it to the global task list."""
    task = {
        "name": name,
        "priority": priority,
        "is_complete": False,
        "estimated_time": estimated_time,
    }

    tasks.append(task)
    print(f"Task added: {name}")


def view_tasks():
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return
    index = 1
    for task in tasks:
        if task['is_complete']:
            status = "Completed"
        else :
            status = "Pending"
        print(
            f"{index}. {task['name']} | "
            f"Priority: {task['priority']} | "
            f"Status: {status} | "
            f"Est. Time: {task['estimated_time']} mins"
        )
        index +=1


def complete_task(index):
    """Mark the task at the specified zero-based index as complete."""
    if 0 <= index < len(tasks):
        tasks[index]["is_complete"] = True
        print(f"Task marked complete: {tasks[index]['name']}")
    else:
        print("Invalid task number.")


def delete_task(index):

    """Delete the task at the specified zero-based index."""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task deleted: {deleted_task['name']}")
    else:
        print("Invalid task number.")


def run_manager():
    """Run the Task Manager until the user chooses to quit."""
    print("Welcome to the Task Manager!")

    '''Initialization'''
    load_tasks()

    while True:
        print("\nOptions: add | view | complete | delete | save | quit")
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

        elif option == "view":
            view_tasks()

        elif option == "complete":
            view_tasks()

            if tasks:
                try:
                    task_number = int(
                        input("Enter task number to mark complete: ")
                    )
                    complete_task(task_number - 1)
                except ValueError:
                    print("Task number must be a whole number.")

        elif option == "delete":
            view_tasks()

            if tasks:
                try:
                    task_number = int(
                        input("Enter task number to delete: ")
                    )
                    delete_task(task_number - 1)
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
