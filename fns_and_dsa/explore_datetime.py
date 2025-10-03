from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    return formated_date

def calculate_future_date(x):
    future_date = datetime.now().date()+ timedelta(days=x)
    formated_date= future_date.strftime("%Y-%m-%d")
    return formated_date


print("Current date and time:",display_current_datetime())
days_to_add = int(input("Enter the number of days to add to the current date: "))
print("Future date:",calculate_future_date(days_to_add))