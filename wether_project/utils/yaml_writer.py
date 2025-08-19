import yaml
from cities import *

def write_yaml():
    with open(r"cities.yaml", 'w') as file:
        city_yaml=yaml.dump(citys.get_city(),file)
