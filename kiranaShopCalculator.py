sum = 0
while(True):
    userInput = input('enter the item price or press q to quit: \n')
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"order total so far: {sum}")
    else:
        print(f"your bill total is {sum} .thanks for shopping with us")
        break
