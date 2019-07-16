size = 10
for n in range(size):
    for i in range(n):
        print('*',end='')
    for j in range(2*(size - 1)):
        print("",end='')
    for k in range(n):
        print("*",end='')
    print("")



'''output:
**
****
******
********
**********
************
**************
****************
******************'''
