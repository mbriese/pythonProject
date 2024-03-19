# This program takes user age as input and converts age to number of months
from datetime import datetime

ageInput: str = input("What is your age in years? ")
months = int(ageInput) * 12
ageString = "your age of {} is {} in months".format(ageInput, months)
print(ageString)
print(f"your age {ageInput} is equal to {months} months")

# months to days calculation
days = int(ageInput) * 365
print(f"You have been alive {days} days")

# days to minutes calculation
# days conversion to minutes is days * 24 hrs * 60 min
minutes = int(days) * 24 * 60
# minutes conversion to seconds is minutes * 60 sec
seconds = int(minutes) * 60
print(f"You have been alive {minutes} minutes or {seconds} seconds")
