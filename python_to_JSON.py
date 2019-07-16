import json

data = {
    "name":"Nitesh",
    "marks":[1,2,3,4],
    "age":21
    }
print(json.dumps(data))          # output is string
