from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(x):
    future_date = datetime.now().date()+ timedelta(days=x)
    return future_date


print("Current date and time:",display_current_datetime())
int(input("Enter the number of days to add to the current date: "))
print("Future date:",calculate_future_date(1))