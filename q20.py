# Q20 - Number System Functions

# ---------- Functions ----------

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))


def reverse_number(n):
    return int(str(n)[::-1])


def is_armstrong(n):
    power = len(str(n))
    total = sum(int(d) ** power for d in str(n))
    return total == n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def is_perfect(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


# ---------- Main Menu ----------

def number_menu():
    while True:
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci Series")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Choose option (1-10): ")

        if choice == "10":
            print("Exiting program...")
            break

        elif choice == "1":
            num = int(input("Enter number: "))
            print("Factorial:", factorial(num))

        elif choice == "2":
            num = int(input("Enter number: "))
            print("Prime?" , is_prime(num))

        elif choice == "3":
            num = int(input("Enter number of terms: "))
            print("Fibonacci Series:", fibonacci(num))

        elif choice == "4":
            num = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(num))

        elif choice == "5":
            num = int(input("Enter number: "))
            print("Reversed number:", reverse_number(num))

        elif choice == "6":
            num = int(input("Enter number: "))
            print("Armstrong?" , is_armstrong(num))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            num = int(input("Enter number: "))
            print("Perfect Number?" , is_perfect(num))

        else:
            print("Invalid choice!")


# Call main function
number_menu()