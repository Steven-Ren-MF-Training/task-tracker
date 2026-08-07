# Bug Reports

## BUG-01
**Status:** Resolved

**Description:** Recurring tasks do not reset their completion status correctly.

**Steps to Reproduce:**

1. Create a `RecurringTask`.
2. Call `mark_complete()` on the recurring task.
3. Call `reset()`.
4. Check the task status using `get_is_complete()`.

**Expected Behavior:**
The recurring task should be reset and `get_is_complete()` should return `False`.

**Actual Behavior:**
The task remains completed and `get_is_complete()` returns `True` because the subclass attempts to update a different private `__is_complete` attribute.

---

## BUG-02

**Status:** Resolved

**Description:** The last task in the task list cannot be marked as complete.

**Steps to Reproduce:**

1. Run `task_manager.py`.
2. Add one or more tasks.
3. Choose the option to complete a task.
4. Enter the number of the last task in the list.

**Expected Behavior:**
The selected task should be marked as complete.

**Actual Behavior:**
The program reports that the task number is invalid because the validation condition excludes the final task number.
