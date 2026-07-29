# Bonus Exercise Student Report


# Ask the user to enter student and assignment information
student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")
course = input("Enter Course: ")
assignment_name = input("Enter Assignment Name: ")
assignment_deadline = input("Enter Assignment Deadline: ")
estimated_time = float(input("Enter Estimated Time in Hours: "))
assignment_submitted = input("Enter Assignment Submitted Status (True/False): ")

# Display the student task tracker report
print("====================================")
print("STUDENT TASK TRACKER")
print("====================================")
print(f"Student ID :{student_id}")
print(f"Student Name :{student_name}")
print(f"Course :{course}")
print(f"Assignment Name :{assignment_name}")
print(f"Assignment Deadline :{assignment_deadline}")
print(f"Estimated Time :{estimated_time}")
print(f"Assignment Submitted :{assignment_submitted}")
print("====================================")
