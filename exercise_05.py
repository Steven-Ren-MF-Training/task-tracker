# Ask the user to enter task information
task_id = input("Enter Task ID: ")
task_name = input("Enter Task Name: ")
department = input("Enter Department: ")
estimated_hours = float(input("Enter Estimated Hours: "))

# Display the task information report
print("=========================")
print("TASK INFORMATION")
print("=========================")
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Department:", department)
print("Estimated Hours:", estimated_hours)
