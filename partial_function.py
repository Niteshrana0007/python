from functools import partial

def greeting(name):
    print("hello,how are you",name)

greet_nitesh = partial(greeting,"nitesh")
greet_nitesh()
    
