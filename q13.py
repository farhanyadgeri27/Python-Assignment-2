# Q13 - Sum and Average

numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    numbers.append(float(input("Enter number: ")))

print("Sum:", sum(numbers))
print("Average:", sum(numbers)/n)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))