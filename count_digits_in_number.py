# count the digite in a given number 
k = int(input("enter any number: "))
count = 0
while (k > 0):
    count = count + 1
    k = k//10
print(count,"digits no.")    
