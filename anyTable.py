print('enter any number ')
number = int(input())
n = 1
while True :
    print(number,'*',n,'=',number*n)
    n = n + 1
    if n >= 11:
        break
print('end')
