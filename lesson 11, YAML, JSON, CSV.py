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

#DZ

class Humans:
    humans_info=[
        {"Name":"Bob",
         "age":25
        },
        {"Name":"Ivan",
         "age":42
        }
    ]
    def __init__(self,name):
        self.humans_info=[
        {"Name":"Bob",
         "age":25
        },
        {"Name":"Ivan",
         "age":42
        }]
        self.name=name

    def get_info(self):
        return self.humans_info

    def sava_yaml(self):
        with open(self.name, 'w') as file:
            dz = yaml.dump(self.humans_info, file)

    def read_yaml(self):
        with open(self.name, 'r') as file:
            dz = yaml.load(file, Loader=yaml.FullLoader)
            print(dz)


Russia=Humans('dz_test.yaml')
print(Russia.get_info())
Russia.sava_yaml()
Russia.read_yaml()

class jsonchik:
    listichik=[]

    def __init__(self,name):
        self.listichik=[{
            'Gay': 'yes',
            'Natural': 'no'
        },
            {'No gay': 'yes',
             'No natural': 'no'}]
        self.name=name

        self.json_object = json.dumps(self.listichik, indent=1)

    def save_json(self):
         with open(self.name, 'w') as outfile:
            outfile.write(self.json_object)

    def read_json(self):
        with open(self.name, 'r') as openfile:
            json_object = jsson.load(openfile)
            print(json_object)

Testim=jsonchik('testim.json')
Testim.save_json()
Testim.read_json()


