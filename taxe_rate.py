num = float(input("Enter salary: "))

if num <= 5000:
    tex = num * 0.02
elif num <= 10000:
    tex = num * 0.03
elif num <= 15000:
    tex = num * 0.04
elif num <= 20000:
    tex = num * 0.05
else:
    tex = num * 0.10

print(f"Your tax is: {tex}")
