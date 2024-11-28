from datetime import datetime

def calculate_age_gap(date1_str, date2_str):
    # Parse the input dates
    format_str = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, format_str)
    date2 = datetime.strptime(date2_str, format_str)

    # Calculate the time difference
    delta = abs(date2 - date1)
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30

    # Display the results
    print(f"Age gap: {years} years, {months} months, {days} days")
    print(f"Total time difference: {int(delta.total_seconds())} seconds")

# Input dates
date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

calculate_age_gap(date1_str, date2_str)
