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
# bmi()