import requests
import json

# POST

headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {'type': '1', 'car_num': "66버5968", 'time': '2022-04-18 10:40'}
res = requests.post('http://15.165.153.54:3000/python', data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)
