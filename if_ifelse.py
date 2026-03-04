num = int(input("Enter a number"))
if(num > 100 or num < 0):
    print("Invalid number")
elif(num>90):
    print("Grade is A")
elif(num>80):
    print("Grade is B")
elif(num>70):
    print("Grade is C")
elif(num>60):
    print("Grade is D")
elif(num>50):
    print("Pass the student")
else:
    print("Fail the student")
    
