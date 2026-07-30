# Program Name: Task Tracker Priority Checker
# Author: Steven Ren
# Description: This program collects tasks and displays a message based on priority.

print("Welcome to Task Tracker Priority Checker!")
print()

while True:
    task_name = input("Enter a task name (or type 'quit' to stop): ").strip()

    if task_name.lower() == "quit":
        break

    # The > operator checks that the task name contains at least one character.
    if len(task_name) > 0:
        priority = input(
            "Enter priority (high, medium, low): "
        ).strip().lower()

        if priority == "high":
            print("Urgent: handle this task first.")
        elif priority == "medium":
            print("Schedule this task soon.")
        elif priority == "low":
            print("Handle this task when time allows.")
        else:
            print(
                "Priority not recognized. "
                "Please enter high, medium, or low."
            )
    else:
        print("Task name cannot be empty.")

    print()

print()
print("Session ended. Goodbye!")