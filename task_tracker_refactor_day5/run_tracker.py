END_MESSAGE = 'Session ended. Goodbye!'

from task_tracker_refactor_day5.greet_user import greet_user
from  task_tracker_refactor_day5.check_priority import check_priority
from task_tracker_refactor_day5.get_task_input import get_task_input
from task_tracker_refactor_day5.get_priority_input import get_priority_input

def run_tracker():
    greet_user()
    while True:
        task_name = get_task_input()
        if task_name.lower() == "quit":
            break
        if not task_name:
            print("Task name cannot be empty.")
            print()
            continue
        priority = get_priority_input()
        print(f"Task: {task_name}")
        print(check_priority(priority))

    print(f"{END_MESSAGE}")

run_tracker()