
def get_priority_input(default_priority="medium"):
    """Collect and return a task priority entered by the user."""

    priority = input(
        "Enter priority (high, medium, low): "
    ).strip().lower()

    if not  priority:
        priority = default_priority
    return priority
