def msg(func):
    def inner(a,b):
        if b == 0 :
            print("can't divide by zero")
            return
        return func(a,b)
    return inner
@msg
def divide(a,b):
    res = a/b
    return res
a = float(input('enter number '))
b = float(input('enter number '))
c = divide(a,b)
print(c)
