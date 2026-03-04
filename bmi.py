weight = float(input("Enter your weight :"))
feet = float(input("Enter your height : "))
inches = float(input("Enter your inches :"))
height = (feet * 12 + inches) * 0.0254
bmi = weight / (height ** 2)
print(f"Your BMI is :{bmi}")
if(bmi<=18.5):
    print("Your are under weight")
elif(bmi>=20 and bmi<=25):
    print("Your are normal weight")
elif(bmi>=25 and bmi<=30):
    print("Your are over weight")
else:
    print("Your weight is obese")




