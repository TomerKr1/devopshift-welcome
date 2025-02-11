from pprint import pprint
import httpx
import json

respone=httpx.get('https://jsonplaceholder.typicode.com/users')

print (respone)

content=respone.json()

pprint(content[0])
# data=json.loads(content)

# print("NAME IS",data[0]["name"])

# for users in data:
#     print(users["name"])