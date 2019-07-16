def func2(func):
    def inner():
        print('enter your name ')
        name = input()
        func()
        print(name)
    return inner
@func2
def fun():
    print('hello user!')
fun() 
