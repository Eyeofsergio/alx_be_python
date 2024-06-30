# Enter single task
task = input("Enter your task: ")

#Enter the tast priorty
priority = input("Priority (high/medium/low): ")

#Enter in the time bound
time_bound = input("Is it time-bound? (yes/no): ")

#Enter the task based on priority and time sensitivity
match priority:
    case "high": 
        reminder = f"{task} is a high priorty task."
        if time_bound == "yes" :
            reminder += "It requires immediate attention today!"
        else:
            reminder += "Ensure to complete it as soon as possible."

    case "medium":
        reminder = f"{task} is a medium priority task. "
        if time_bound == "yes":
            reminder += "It should be completed today."
        else: 
            reminder += "Try to finish it soon." 
    
    case "low":
        reminder = f"{task} is a low pririty task."
        if time_bound == "yes":
            reminder += "It is time-bound, so try to complete it today."
        else:
            reminder += "Consider completing it when you have free time."

    case _:
        reminder = "Invalid priority entered. Please eter high, medium, or low."

print(f"Daily Reminder: {reminder}")