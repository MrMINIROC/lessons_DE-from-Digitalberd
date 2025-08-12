# практика
from traceback import print_tb


class Human:
    _name: str
    _location: str

    def __init__(self,name='Ivan'):
        self._name = name
        self._location = 'Moscow'

    def get_name(self):
        return self._name

    def get_location(self):
        return self._name + ':' + self._location

    def set_location(self, location):
        self._location=location

one_man=Human()
print(one_man.get_location())

class Children(Human):
    __age = 5

    def __init__(self, name='kid iva'):
        super().__init__(name)


    def set_age(self,age):
        self.__age=age

    def get_age(self):
        return self._name + ":" + str(self.__age)


class Bus:
    __humans: list()

    def __init__(self, humans:list):
        self.__humans = humans

    def add_kid(self, childrens:list):
        self.__humans = self.__humans + childrens

    def remove_kid(self, children:list):
        for one in children:
            if one in self.__humans:
                self.__humans.remove(one)

    def print_all_kids(self):
        for one_child in self.__humans:
            print(one_child.get_location())


    def go_to_home(self,n_loc):
        for one in self.__humans:
            one.set_location(n_loc)




one_kid=Children()
print(one_kid.get_location())
print(one_kid.get_age())

first_kid=Children('Gay')
second_kid=Children('Petya')
third_kid=Children('Vasya')

one_bus= Bus([first_kid, second_kid])
one_bus.print_all_kids()

print('______________________')
one_bus.add_kid([third_kid])
one_bus.print_all_kids()

print('___________________________')
one_bus.remove_kid([second_kid])
one_bus.print_all_kids()

print('_________________________')
one_bus.go_to_home('Home')
one_bus.print_all_kids()


#############################

list1=[1,2,3,4, 'hi!', 5,6,7]

def list_devision(local_list: list):
    l_res=list()
    for one_element in list1:
        try:
            l_res.append(100/(one_element-2))
        except ZeroDivisionError:
            print('Ne deli na 0')
        except Exception as e:
            print(e)
        finally:
            print(one_element)
    return l_res

print(list_devision(list1))

# DZ
class Human:
    sex: int
    age:int
    name:str

    def __init__(self,name="Ivan"):
        self.sex=1
        self.age=20
        self.name=name

    def get_info(self):
        return self.name


class polk:
    humans: list()

    def __init__(self,humans: list()):
        self.humans=humans

    def add_to_polk(self, voenniy: list()):
        self.humans= self.humans + voenniy

    def remove_to_polk(self, voenniy:list()):
        for one in self.humans:
            if one in self.humans:
                self.humans.remove(one)

    def who_in_polk(self):
        for one in self.humans:
            print( one.get_info())

bob=Human()
print(bob.get_info())

first=Human('Oleg')
second=Human('Ne oleg')

polk=polk([first,second])

polk.who_in_polk()

polk.remove_to_polk([first])
polk.who_in_polk()


try:
    print(10/0)
except ZeroDivisionError:
    print('Oshibka')
finally:
    print('10/0')