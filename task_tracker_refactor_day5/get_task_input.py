def get_task_input():
    """Collect and return a task name entered by the user."""
    task_name = input(
        "Enter a task name (or type 'quit' to stop): "
    ).strip()

    return task_name
