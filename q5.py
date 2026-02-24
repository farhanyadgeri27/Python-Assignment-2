# Q5 - Bill Splitter

bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tax_percent = float(input("Enter tax percentage: "))
tip_percent = float(input("Enter tip percentage: "))

tax = bill * tax_percent / 100
tip = bill * tip_percent / 100

total = bill + tax + tip
per_person = total / people

print("Total bill including tax and tip:", total)
print("Each person should pay:", round(per_person, 2))