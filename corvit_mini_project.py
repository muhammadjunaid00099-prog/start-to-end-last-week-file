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


def bmi():
    weight = float(input("Enter your weight (kg): "))
    feet = float(input("Enter your height (feet): "))
    inches = float(input("Enter your inches: "))

    height = (feet * 12 + inches) * 0.0254
    bmi_value = weight / (height ** 2)

    print(f"Your BMI is: {bmi_value:.2f}")

    if bmi_value <= 18.5:
        print("You are underweight")
    elif bmi_value <= 25:
        print("You are normal weight")
    elif bmi_value <= 30:
        print("You are overweight")
    else:
        print("You are obese")


def temperature():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9

    print(f"Temperature in Celsius: {celsius:.2f}")

    if celsius > 50:
        print("Temperature is Very Hot")
    elif celsius > 40:
        print("Temperature is Hot")
    elif celsius > 30:
        print("Temperature is Good")
    elif celsius > 20:
        print("Temperature is Cold")
    else:
        print("Temperature is Very Cold")



print("Select Program")
print("1. Simple Calculator")
print("2. BMI Calculator")
print("3. Temperature Converter")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    calculator()
elif choice == "2":
    bmi()
elif choice == "3":
    temperature()
else:
    print("Invalid choice")