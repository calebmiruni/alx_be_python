task = input("Enter a task description: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is this task time-sensitive? (yes or no): ").lower()
match priority:
    case "high":
        priority_message = "This task has high priority."
    case "medium":
        priority_message = "This task has medium priority."
    case "low":
        priority_message = "This task has low priority."
    case _:
        priority_message = "Unknown priority."
if time_bound == "yes":
    time_sensitive_message = "That requires immediate attention today!"
else:
    time_sensitive_message = "You can complete this task at your convenience."
print(f"Task: {task}")
print(f"Priority: {priority_message}")
print(time_sensitive_message)
