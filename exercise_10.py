# Ask the user to enter task tracker information
task_id = int(input("Enter Task ID: "))
task_name = input("Enter Task Name: ")
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
priority = input("Enter Priority: ")
estimated_hours = float(input("Enter Estimated Hours: "))

# No if-else allowed
completed_status = input("Enter Completed Status (True/False): ")

# Display the task tracker report
print("====================================")
print("TASK TRACKER REPORT")
print("====================================")
print("Task ID :", task_id)
print("Task Name :", task_name)
print("Employee Name :", employee_name)
print("Department :", department)
print("Priority :", priority)
print("Estimated Hours :", estimated_hours)
print("Completed :", completed_status)
print("====================================")