class Task:
    """Represent a task with encapsulated priority and completion status."""
    def __init__(self, name, priority, estimated_time):
        """Initialize a task with a name, priority, and estimated time."""
        self.name = name
        self.estimated_time = estimated_time
        self.__priority = priority
        self.__is_complete = False

    def get_priority(self):
        """Return the task priority."""
        return self.__priority

    def get_name(self):
        """return name of the task"""
        return self.name

    def set_priority(self, new_priority):
        """Update the task priority if the new value is valid."""
        valid_priorities = ("high", "medium", "low")

        if new_priority in valid_priorities:
            self.__priority = new_priority
        else:
            print("Invalid priority. Please enter high, medium, or low.")

    def get_is_complete(self):
        """Return whether the task is complete."""
        return self.__is_complete

    def mark_complete(self):
        """Mark the task as complete."""
        self.__is_complete = True
        print(f"{self.name} was marked completed")

    def to_dict(self):
        """Convert the Task object into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete,
        }

    @classmethod
    def from_dict(cls,task_data):
        '''Convert the dictionary to task object'''
        task = cls(
            task_data["name"],
            task_data["priority"],
            task_data["estimated_time"],
        )

        if task_data["is_complete"]:
            task.mark_complete()

        return task

    def __str__(self):
        """Return a readable string representation of the task."""
        status = "Done" if self.__is_complete else "Pending"

        return (
            f"{self.name} | "
            f"Priority: {self.__priority} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )