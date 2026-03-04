farenhite = int(input('Enter a celsius a number'))

celsius = ( farenhite - 32) * 5/9
print("Temperature is :", celsius)
if(celsius>50):
  print("Temperature is very Hot")
elif(celsius>40):
  print("Temperature is Hot")
elif(celsius>30):
  print("Temperature is Good")
elif(celsius>20):
  print("Temperature is very Cold")
else:
    print("Its rainy today")