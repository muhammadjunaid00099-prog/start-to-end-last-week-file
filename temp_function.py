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

# temperature()