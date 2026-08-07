class Task:
    """Represent a task with encapsulated priority and completion status."""
    def __init__(self, name, priority, estimated_time):
        """Initialize a task with a name, priority, and estimated time."""
        self.name = name
        self.estimated_time = estimated_time
        self._is_complete = False
        self.set_priority(priority)

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
        return self._is_complete

    def mark_complete(self):
        """Mark the task as complete."""
        self._is_complete = True
        print(f"{self.name} was marked completed")

    def to_dict(self):
        """Convert the Task object into a dictionary for JSON storage."""
        return {
            "type": "Task",
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self._is_complete,
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
        status = "Done" if self._is_complete else "Pending"

        return (
            f"{self.name} | "
            f"Priority: {self.__priority} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )

class UrgentTask(Task):
    """Represent a high-priority task with a deadline."""
    def __init__(self, name, estimated_time, deadline):
        """Initialize an urgent task with high priority and a deadline."""
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline

    def __str__(self):
        """Return a readable string with an urgent label and deadline."""
        if self.get_is_complete():
            status = "Done"
        else:
            status  = "Pending"

        return (
            f"[URGENT] {self.name} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins | "
            f"Deadline: {self.deadline}"
        )

    def to_dict(self):
        """Convert the UrgentTask object into a dictionary."""
        task_data = super().to_dict()
        task_data["type"] = "UrgentTask"
        task_data["deadline"] = self.deadline
        return task_data

class RecurringTask(Task):
    def __init__(self, name, priority, estimated_time, frequency):
        """Initialize a recurring task with a frequency."""
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency

    def __str__(self):
        """Return a readable string with a recurring label and deadline."""
        if self.get_is_complete():
            status = "Done"
        else:
            status  = "Pending"
        return (
            f"[RECURRING: {self.frequency}] {self.name} | "
            f"Priority: {self.get_priority()} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )

    def reset(self):
        """Reset the task completion status to incomplete."""
        self._is_complete = False

    def to_dict(self):
        """Convert the RecurringTask object into a dictionary."""
        task_data = super().to_dict()
        task_data["type"] = "RecurringTask"
        task_data["frequency"] = self.frequency
        return task_data


def task_from_dict(data):
    """Create and return the correct task type from dictionary data."""
    task_type = data.get("type", "Task")

    if task_type == "UrgentTask":
        task = UrgentTask(
            data["name"],
            data["estimated_time"],
            data["deadline"],
        )
    elif task_type == "RecurringTask":
        task = RecurringTask(
            data["name"],
            data["priority"],
            data["estimated_time"],
            data["frequency"],
        )
    else:
        return Task.from_dict(data)

    if data.get("is_complete", False):
        task.mark_complete()

    return task


if __name__ == "__main__":
    demo_tasks = [
        Task("Buy groceries", "low", 30),
        UrgentTask("Fix server outage", 5, "2024-12-01"),
        RecurringTask("Team standup", "medium", 15, "daily")
    ]

    print("--- Polymorphism Demo ---")
    for task in demo_tasks:
        print(task)
        print("Is a Task instance:", isinstance(task, Task))
        print()
