# for-else method for checking prime
''''num = 5
for i in range(2,num):
    if num%i==0:
        print('not a prime number')         #not accurate method
        break
else:
    print('prime number')'''


# using while loop
'''n = int(input('enter any number '))
i = 2
flag = 0
while (1<n):
    if n%i==0:
        flag = 1
        break
    else:
        i+=1
if(flag==0):
    print('prime number')
else:
    print('not a prime number')'''


# using if loop
'''number = int(input('enter number '))
n = 1
while True :
    n = n + 1
    if n == number:
        print('Is a  prime number')
    if number%n == 0:
        print('not a prime number')
        break'''


# using for loop
'''number = int(input('enter any number: '))
for n in range(2,number+1):
    if number%n == 0:
        if number == n:
            print('Is a prime number ')
        else:
            print('not a prime number ')
            break'''
        
