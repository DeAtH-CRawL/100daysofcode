import os
import calc_art
print(calc_art.logo)

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:  # outer loop = new calculator session (AC resets here)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Simple Calculator\n")
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number. Restarting session.")
        continue

    while True:  # inner loop = operate on current result
        operation = input("Enter operation (+, -, *, /): ")
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Session will restart.")
            break

        if operation in calculator_operations:
            result = calculator_operations[operation](num1, num2)
        else:
            result = "Error: Invalid operation."

        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Do you want to continue with {result}? (yes/no): ").strip().lower()
        if choice == "yes":
            try:
                num1 = float(result)
            except Exception:
                print("Cannot continue with non-numeric result. Session will restart.")
                break
        else:
            # 'no' acts as AC: clear screen and restart fresh session
            break
