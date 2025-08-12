
#public открытый без чего либо
#protected _  просто показать тем кто смотрит что ну не надо из класса, но никак не влияет на код
#private __ никак не выходит из класса


class Human:
    name:str
    __age:int
    _password:str

    def __init__(self,v_name="Vasya"):
        self.name=v_name
        self._password="lalala"
        self.__age=30


o_vasya=Human()
print(o_vasya.name)
# ничего протектед не дает, не встречается почти
print(o_vasya._password)

#приват делается через __, не дает выходить из класса
#print(o_vasya.__age)



class Alien:
    name:str
    __age:int

    def __init__(self,v_name="Gandonio"):
        self.name=v_name
        self.__age=30

    def get_age(self): #гетер
        return self.__age

    def set_age(self,new_age:int): # сеттер
        if type(new_age)==int:
            self.__age=new_age


Gandonio=Alien()
print(Gandonio.get_age())

Gandonio.set_age(10)
print(Gandonio.get_age())
# только инт
Gandonio.set_age(10.3)
print(Gandonio.get_age())

#DZ

class Monkey:
    name:str
    __age:int

    def __init__(self,v_name="Monkey"):
        self.name=v_name
        self.__age=10

class Kid:
    __name:str
    __age:int

    def __init__(self,v_name="Dolbaeb"):
        self.__name=v_name
        self.__age=6

    def set_name(self,v_name):
        self.__name=v_name

    def get_name(self):
        return self.__name

class Shuller(Kid):
    def __init__(self,name="Shuller"):
        super().__init__(name)
        self.status='Shuller'

    def get_name(self):
        return super().get_name()

Oleg=Kid()
Oleg.set_name("Oleg")
print(Oleg.get_name())

Shuller_kid=Shuller("Kevin")
print(Shuller_kid.get_name())