# Q9 - Ticket Pricing

age = int(input("Enter age: "))
day = input("Enter day (weekday/weekend): ").lower()

price = 0

if age < 12:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

if day == "weekday":
    price -= 20

print("Ticket price:", price)