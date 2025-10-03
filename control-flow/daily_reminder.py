task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:

    case "high":
       text1=str(task)+"' is a high priority task"
    case "medium":
       text1=str(task)+"' is a medium priority task" 
    case "low":
       text1=str(task)+"' is a low priority task"
       


if time_bound=="yes":
    text="Reminder:"
    text2= "that requires immediate attention today!" 
    print(f"{text} '{text1} {text2}")    
elif time_bound=="no":
    text="Note:"
    text2= ". Consider completing it when you have free time."
    print(f"{text} '{text1} {text2}")    
      