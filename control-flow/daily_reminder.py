task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:

    case "high":
       text1=str(task)+"' is a high priority task"
    case "medium":
       text1=str(task)+"' is a medium priority task" 
    case "low":
       print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
       


if time_bound=="yes" and priority!="low": 
    print(f"Reminder: '{text1} that requires immediate attention today!")    
elif time_bound=="no" and priority!="low":
    print(f"Note: '{text1}. Consider completing it when you have free time.")    
      