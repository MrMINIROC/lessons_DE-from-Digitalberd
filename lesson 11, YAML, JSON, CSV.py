from random import sample

import yaml
#создание yaml файла
#write
l_connections=[
    {
        "user_name": "elt_user",
        "password": "123",
        'host': '127.0.0.1'
    },
    {
        "user_name": "test",
        "password": "456"
    }
]

# создание самого файла
with open(r'connections.yaml', 'w') as file:
    documents = yaml.dump(l_connections, file)

# reeding

with open(r'connections.yaml') as file:
    connections = yaml.load(file, Loader=yaml.FullLoader)
    print(connections)
print('______________________________________________________________________')

# JSON
import json

dictionary={
    'name': 'Oleg1',
    'rollno': 56,
    'cpga': 6.7,
    'phonenumber':'8800555454'
}

#индент это вид форматирования, для красоты и удобста, можно и без него
json_object = json.dumps(dictionary, indent=1)

#writing
with open('sample.json', 'w') as outfile:
    outfile.write(json_object)

#reading

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

print('______________________________________________________________________')
#csv

import pandas as pd

c_connections=[
    {
        "user_name": "elt_user",
        "password": "123",
        'host': '127.0.0.1'
    },
    {
        "user_name": "test",
        "password": "456",
        'host': '127.0.0.1'
    }
]

df1=pd.DataFrame(c_connections)
print(df1)
print(type(df1))

df1.to_csv('from_pd.csv', index=False)
print('______________________________________________________________________')

df2 = pd.read_csv('from_pd.csv')
print(df2)
print(type(df1))
