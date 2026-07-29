# Program Name: Task Tracker
# Author: Kaifeng (Steven) Ren
# Description: This script collects task information and displays a task summary.

print("Welcome to Task Tracker!")
print("Please enter your task details below.")
task_name = input("Enter task name: ")
task_priority = input("Enter priority level (high, medium, low): ")
estimated_time = int(input("Estimated time to complete (in minutes): "))
is_urgent = input("Is this task urgent? (yes/no): ")

# Placeholder: task completion status starts as False
is_complete = False

print("Task Summary")
print("------------")
print(f"Task: {task_name}")
print(f"Priority: {task_priority}")
print(f"Estimated Time: {estimated_time} minutes")
print(f"Urgent: {is_urgent}")
print(f"Completed: {is_complete}")