# Q4 - Age Calculator

from datetime import date

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
birth_month = int(input("Enter your birth month: "))
current_month = date.today().month
birth_day = int(input("Enter your birth day: "))
current_day = date.today().day

age = current_year - birth_year

if current_month < birth_month:
    age -= 1
elif current_month == birth_month and current_day < birth_day:
    age -= 1

print("You are", age, "years old.")
print("In months:", age * 12)
print("In days (approx):", age * 365)
print("In hours (approx):", age * 365 * 24)