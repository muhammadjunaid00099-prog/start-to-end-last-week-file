def calculator(value1 = 5 , value2 = 87 , operator = "+"):
   

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

calculator(49,78,'/')
calculator()