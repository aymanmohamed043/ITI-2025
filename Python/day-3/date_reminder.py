# 3) Datetime Reminder Script
# - Ask user for a date (YYYY-MM-DD).
# - Calculate how many days remain until that date.
# - If it is in the past, print "This date has already passed."
# - Otherwise, save the reminder into "reminders.txt" in format:
#     "{date} -> {days_left} days left"
# - Append multiple reminders without overwriting.

from datetime import datetime
from time_decorator import log_time

@log_time
def reminder_script():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            print(f"Target date is: {target_date}")
            break
        except ValueError:
            print("Invalid date format. Try again.")

    today = datetime.today().date()
    print(f"Today's date is: {today}")  
    days_left = (target_date - today).days

    if days_left < 0:
        print("This date has already passed.")
    else:
        with open("output_files/reminders.txt", "a") as f:
            f.write(f"{date_str} -> {days_left} days left\n")
        print(f"Reminder saved: {days_left} days left.")

if __name__ == "__main__":
    reminder_script()
