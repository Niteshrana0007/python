num_dict = {
    "1":1,
    "2":2,
    "3":3
}
num = "321"
result = num_dict[num[0]]
for i in range(1,len(num)):
    result = result*10 + num_dict[num[i]]

print(result)
print(type(result))
