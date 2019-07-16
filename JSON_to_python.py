import json

# some json
x = '{"name":"john","age":30,"city":"sonepat"}'

# parse x
y = json.loads(x)

# the result is in python dictionary
print(y)
