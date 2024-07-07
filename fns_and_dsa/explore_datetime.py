from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date("%Y-%m-%d %H:%M:%S")
    formatted_date = current_date
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add:"))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_data = future_date = future_date("%Y-%m-%d")
    print(f"Future Date (after {days_to_add}days): {"formatted_future_date"}")

