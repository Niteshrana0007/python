def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# change the values of num1 and num2 for a different result
num1 = 10
num2 = 9

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
