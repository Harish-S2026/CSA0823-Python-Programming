def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result =", add(a, b))

    elif operation == "-":
        print("Result =", subtract(a, b))

    elif operation == "*":
        print("Result =", multiply(a, b))

    elif operation == "/":
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result =", divide(a, b))

    else:
        print("Invalid operation")

except ValueError:
    print("Error: Please enter numbers only")