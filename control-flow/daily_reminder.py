task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:

    case "high":
       text1="Reminder: '"+str(task)+"' is a high priority task"
    case "medium":
       text1="Reminder: '"+str(task)+"' is a medium priority task" 
    case "low":
       text1="Reminder: '"+str(task)+"' is a low priority task"


if time_bound=="yes":
    text2= "that requires immediate attention today!"    
elif time_bound=="no":
    text2= ". Consider completing it when you have free time."
 
print(text1,text2)      
      