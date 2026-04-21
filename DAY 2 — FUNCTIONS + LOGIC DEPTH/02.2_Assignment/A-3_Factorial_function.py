#A-3:Factorial function
def factorial(x):
    if x<=0:
        return None
    
    result=1
    for i in  range(1,x+1):
        result*=i

    return result
print(factorial(5))