import bmi_function
import calculator_function
import temp_function

print("Select Program")
print("1. BMI Calculator")
print("2. Simple Calculator")
print("3. Temperature Converter")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    bmi_function.bmi()
elif choice == 2:
    calculator_function.calculator()
elif choice == 3:
    temp_function.temperature()
else:
    print("Invalid number")