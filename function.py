def simple():
    print ("My first function")
simple()
# Using a Function in Another Function
def plus_five(x):
    return x + 5

def m_by_3(x):
    return plus_five(x) * 3
#Another Way to Define a Function
def multiplication_by_2(x):
    result = x ** 2
    print (x, "Raised to the power of 2:")
    return result
    
multiplication_by_2(5)
