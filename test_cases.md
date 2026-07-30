# Task Tracker Test Cases

| Test Case ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-01 | Verify valid high priority task | Task: Buy groceries<br>Priority: high | Display "Urgent: handle this task first." |
| TC-02 | Verify valid medium priority task | Task: Complete assignment<br>Priority: medium | Display "Schedule this task soon." |
| TC-03 | Verify empty task name (edge case) | Task: *(empty)* | Display "Task name cannot be empty." and ask for another task. |
| TC-04 | Verify invalid priority | Task: Call doctor<br>Priority: whenever | Display "Priority not recognized. Please enter high, medium, or low." |
| TC-05 | Verify quit command | Task: quit | Exit the loop and display "Session ended. Goodbye!" |