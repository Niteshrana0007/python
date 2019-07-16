#def factorial(x):
#    if x==1:
#        return 1
#    return x * factorial(x-1)
#result = factorial(3)
#print(result)



def factorial(x):
    if x==1:
        return 1
    result = factorial(x-1)
    return x * result
result =factorial(3)
print(result)
