def calculator():
    value1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    value2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", value1 + value2)

    elif operator == "-":
        print("Result:", value1 - value2)

    elif operator == "*":
        print("Result:", value1 * value2)

    elif operator == "/":
        if value2 != 0:
            print("Result:", value1 / value2)
        else:
            print("Cannot divide by zero")

    elif operator == "%":
        print("Result:", value1 % value2)

    else:
        print("Invalid operator")

# calculator()