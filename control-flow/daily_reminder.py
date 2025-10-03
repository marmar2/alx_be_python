
task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:

    case "high":
       text1="'"+str(task)+"' is a high priority task"
    case "medium":
       text1="'"+str(task)+"' is a medium priority task" 
    case "low":
       print("Note: '"+str(task)+"' is a low priority task. Consider completing it when you have free time.")
 

if time_bound=="yes" and (priority=="high" or priority=="medium"):
    text="Reminder: "
    text2= "that requires immediate attention today!" 
    print(text,text1,text2) 
elif time_bound=="no" and (priority=="high" or priority=="medium"):
    text="Note: "
    text2= ". Consider completing it when you have free time."
    print(text,text1,text2) 
     
      