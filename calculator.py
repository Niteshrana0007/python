def add(a,b):
    print(a,'+',b,'=',a+b)
def sub(a,b):
    print(a,'-',b,'=',a-b)
def multi(a,b):
    print(a,'*',b,'=',a*b)
def div(a,b):
    print(a,'/',b,'=',a/b)
    
while (True):
    print('1. add')
    print('2. sub')
    print('3. multi')
    print('4. div')
    print('5. exit')
    choice = int(input('enter any choice 1/2/3/4/5 : '))
    
    if choice == 1:
        add(int(input('enter 1st num ')),int(input('enter 2nd num ')))
        
        
    elif choice  == 2:
        sub(int(input('enter 1st num ')),int(input('enter 2nd num ')))
        

    elif choice == 3:
        multi(int(input('enter 1st num ')),int(input('enter 2nd num ')))
        

    elif choice == 4:
        div(int(input('enter 1st num ')),int(input('enter 2nd num ')))
        

    elif choice == 5:
        print('thanks for using calculator.')
        break
    else:
        print('invalid choice')
        break
        
