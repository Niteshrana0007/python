def function_A(x):
    print('entered function A',x)
    function_B(x+1)
    print('exit function A',x)
def function_B(x):
    print('entered dunction B',x)
    function_C(x+1)
    print('exit function B',x)
def function_C(x):
    print('entered function C',x)
    function_D(x+1)
    print('exit function C',x)
def function_D(x):
    print('entered function D',x)

    print('exit function D',x)

print('starting execution')
function_A(1)
