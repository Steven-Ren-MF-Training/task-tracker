import unittest
from task import Task, UrgentTask, RecurringTask

class TestTask(unittest.TestCase):
    """Test cases for the normal Task class."""
    def setUp(self):
        """Create a fresh Task before each test."""
        self.task = Task("Buy groceries", "high", 30)

    def test_task_creation(self):
        """Verify a Task is created with the right values."""
        self.assertEqual(self.task.name, "Buy groceries")
        self.assertEqual(self.task.get_priority(), "high")
        self.assertEqual(self.task.estimated_time, 30)
        self.assertFalse(self.task.get_is_complete())

    def test_initial_is_complete_false(self):
        """Verify a newly created task is initially incomplete."""
        self.assertFalse(self.task.get_is_complete())

    def test_mark_complete(self):
        """Verify mark_complete sets the task completion status to True."""
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())

    def test_set_priority_valid(self):
        """Verify set_priority updates priority when given a valid value."""
        self.task.set_priority("medium")
        self.assertEqual(self.task.get_priority(), "medium")

    def test_set_priority_invalid(self):
        """Verify set_priority does not change priority for invalid input."""
        self.task.set_priority("urgent")
        self.assertEqual(self.task.get_priority(), "high")

    def test_to_dict(self):
        """Verify to_dict returns all required task fields."""
        task_data = self.task.to_dict()

        self.assertEqual(task_data["name"], "Buy groceries")
        self.assertEqual(task_data["priority"], "high")
        self.assertEqual(task_data["estimated_time"], 30)
        self.assertFalse(task_data["is_complete"])

    def test_from_dict(self):
        """Verify Task.from_dict recreates a Task from dictionary data."""
        task_data = {
            "type": "Task",
            "name": "Buy groceries",
            "priority": "high",
            "estimated_time": 30,
            "is_complete": False,
        }

        recreated_task = Task.from_dict(task_data)

        self.assertEqual(recreated_task.name, "Buy groceries")
        self.assertEqual(recreated_task.get_priority(), "high")
        self.assertEqual(recreated_task.estimated_time, 30)
        self.assertFalse(recreated_task.get_is_complete())

    def test_str_output(self):
        """Verify Task string output contains its name and Pending status."""
        task_string = str(self.task)

        self.assertIn("Buy groceries", task_string)
        self.assertIn("Pending", task_string)

class TestUrgentTask(unittest.TestCase):
    def setUp(self):
        """"Create a urgent task with correct value"""
        self.urgent_task = UrgentTask(
            "Fix server outage",
            5,
            "2024-12-01",
        )

    def test_urgent_priority_is_always_high(self):
        """Verify an urgent task always has high priority."""
        self.assertEqual(self.urgent_task.get_priority(),'high')

    def test_urgent_str_contains_label(self):
        """Verify an urgent  has URGENT LABEL."""
        self.assertIn("[URGENT]", str(self.urgent_task))

    def test_urgent_str_contains_deadline(self):
        """Verify an urgent  has clear deadline."""
        self.assertIn("2024-12-01", str(self.urgent_task))

    def test_urgent_to_dict_includes_type(self):
        """Verify an urgent  has type and deadline type."""
        task_data = self.urgent_task.to_dict()

        self.assertEqual(task_data["type"], "UrgentTask")
        self.assertEqual(task_data["deadline"], "2024-12-01")


class TestRecurringTask(unittest.TestCase):
    def setUp(self):
        ''' Creates a fresh RecurringTask("Team standup", "medium", 15, "daily") before each test'''
        self.recurring_task = RecurringTask(
            "Team standup",
            "medium",
            15,
            "daily")


    def test_recurring_str_contains_label(self):
        """Verify recurring-task output contains its label."""
        self.assertIn("RECURRING:", str(self.recurring_task))

    def test_recurring_to_dict_includes_type(self):
        """Verify dictionary includes task type and frequency."""
        recurring_dict = self.recurring_task.to_dict()
        self.assertEqual("RecurringTask",str(recurring_dict["type"]))
        self.assertEqual("daily", str(recurring_dict["frequency"]))

    def test_reset(self):
        """Verify reset changes a completed recurring task to incomplete."""
        self.recurring_task.mark_complete()
        self.recurring_task.reset()

        self.assertFalse(self.recurring_task.get_is_complete())

if __name__ == "__main__":
    unittest.main()