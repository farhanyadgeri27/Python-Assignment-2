# Q7 - Temperature Converter

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5/9)

    elif choice == "3":
        break
    else:
        print("Invalid choice!")