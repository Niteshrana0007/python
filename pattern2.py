size = 10
a = int(input('>>>'))
for n in range(2*size):
    if  n>10:
        
        n = 20 - a
    for i in range(n):
        print("*",end='')
    for j in range(2*(size-n)):
        print('',end='')
    for k in range(n):
        print("*",end='')
    print('')
