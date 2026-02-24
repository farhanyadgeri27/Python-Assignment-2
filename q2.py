# Q2 - Simple Calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
        print("Modulus:", num1 % num2)
    else:
        print("Division and Modulus not possible (division by zero)")

    print("Power:", num1 ** num2)

except ValueError:
    print("Invalid input! Please enter numbers only.")