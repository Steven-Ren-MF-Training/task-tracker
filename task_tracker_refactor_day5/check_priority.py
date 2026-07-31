def check_priority(priority):
    """
    Return a message based on the supplied priority level.
    A message describing how the task should be handled.
    """
    if priority == "high":
        return "Urgent: handle this task first."
    elif priority == "medium":
        return "Schedule this task soon."
    elif priority == "low":
        return "Handle this task when time allows."
    else:
        return (
            '''Priority not recognized. 
            Please enter high, medium, or low.'''
        )
