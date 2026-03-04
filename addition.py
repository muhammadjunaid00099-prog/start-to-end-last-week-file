def addition(a , b):
    
    sum = a + b
    subtraction = a - b
    
    print(f"The sum is : {sum}")
    print(f"The subtraction is : {subtraction}")
    
addition(76,76)
addition(89,65)

def func1(a = 5 , b =6 , c = 7):
    
    print(a,b,c)
    
func1()
func1(2,3,4)

def show_employee(name , salary = 90000):
    print(f"Both the print : {name , salary}")
    
show_employee('Ben')
show_employee("waqas",100000)


def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)