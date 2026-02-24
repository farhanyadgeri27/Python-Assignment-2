# Q14 - Factorial

num = int(input("Enter number: "))

if num < 0:
    print("Factorial not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial:", fact)