while True:
    print("1.Add numbers ")
    print("2.exit ")
    print('enter your choice ')
    choice = int(input())

    if choice == 2:
        break

    first_num = int(input('enter first number '))
    second_num = int(input('enter second number '))

    result = first_num + second_num
    print('result is ',result)
    
