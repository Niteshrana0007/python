import json

data_info = open("data.json",'r')
data = json.load(data_info)

data_new_info = open("data_new.json",'w')
json.dump(data,data_new_info)

print(data)
