#(still being developed) early version of the code that made the 'info' api 
import json, names, random
data = {}
print('[')
for i in range(99):
    data['id'] = str(i)
    data['name'] = names.get_full_name()
    data['age']  = random.randint(16,78)
    data['friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
    json_data = json.dumps(data)
    print(json_data, ',')
data['id'] = '100'
data['name'] = names.get_full_name()
data['age']  = random.randint(16,78)
data['friends'] = [names.get_full_name(),names.get_full_name(),names.get_full_name()]
json_data = json.dumps(data)
print(json_data)
print(']')


