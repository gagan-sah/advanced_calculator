import math
import datetime

history = []

def show_menu():
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Power")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")

def save_history(operation):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"{time_stamp} --> {operation}")

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == '9':
        print("Thank you for using Advanced Calculator 🚀")
        break

    if choice == '8':
        print("\n---- Calculation History ----")
        for item in history:
            print(item)
        continue

    try:
        if choice in ['1','2','3','4','5','6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                operation = f"{num1} + {num2} = {result}"

            elif choice == '2':
                result = num1 - num2
                operation = f"{num1} - {num2} = {result}"

            elif choice == '3':
                result = num1 * num2
                operation = f"{num1} * {num2} = {result}"

            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by Zero not allowed!")
                    continue
                result = num1 / num2
                operation = f"{num1} / {num2} = {result}"

            elif choice == '5':
                result = (num1 / 100) * num2
                operation = f"{num1}% of {num2} = {result}"

            elif choice == '6':
                result = num1 ** num2
                operation = f"{num1} ^ {num2} = {result}"

            print("Result:", result)
            save_history(operation)

        elif choice == '7':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot find square root of negative number!")
                continue
            result = math.sqrt(num)
            operation = f"√{num} = {result}"
            print("Result:", result)
            save_history(operation)

        else:
            print("Invalid choice! Try again.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")