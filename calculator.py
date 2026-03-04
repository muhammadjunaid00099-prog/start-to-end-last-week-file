# Input
value1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
value2 = float(input("Enter second number: "))

# Calculation
if operator == "+":
    result = value1 + value2
    print(f"Result: {result}")

elif operator == "-":
    result = value1 - value2
    print(f"Result: {result}")

elif operator == "*":
    result = value1 * value2
    print(f"Result: {result}")

elif operator == "/":
    if value2 != 0:
        result = value1 / value2
        print(f"Result: {result}")
    else:
        print("Cannot divide by zero")

elif operator == "%":
    result = value1 % value2
    print(f"Result: {result}")

else:
    print("Invalid operator")
