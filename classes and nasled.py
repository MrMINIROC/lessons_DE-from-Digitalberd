# классы и наследование

class Human:
    hands: int
    foots: int
    head: int
    eyes: int
    age: int
    sex: int
    name:str


    def __init__(self,name):
        self.hands=2
        self.foots=2
        self.head=1
        self.eyes=2
        self.age=30
        self.sex=1
        self.name=name




    def krieg(self):
        if self.sex == 1:
            self.hands=self.hands/2
            self.foots=self.foots/2
            self.eyes=self.eyes/2

    def see_info(self):
        print(f"{self.name} у него осталось {self.hands}, {self.foots}, {self.head}, {self.eyes}")

#init вызывается каждый раз как мы используем класс

petya= Human('petya')
petya.krieg()
petya.see_info()




#наслед

class Woman(Human):
    def __init__(self,name):
        #super = возвращает все данные от родителя. То есть обязательно нужно для наследование супер
        super().__init__(name)
        self.sex=0

    def info(self):
        print(f"Thats is {self.name}. And sex = {self.sex}")

masha=Woman("Masha")
masha.info()
masha.see_info()

# добавление новый параметр для наслед класса
class Nonbinare(Human):
    def __init__(self,name):
        super().__init__(name)
        self.sex=42
        self.cicle=28

    def see_info(self):
        super().see_info()
        print(f"cicle is {self.cicle}")

huesos=Nonbinare("Huesos")
huesos.see_info()

print(huesos.name)



# DZ
class Human():
    name: str
    age: int
    job: str
    raca: str
    def __init__(self,name):
        self.name=name
        self.age=30
        self.job='Alcogolicker'
        self.raca='White'


class Kid(Human):
    def __init__(self,name):
        super().__init__(name)
        self.age=10
        self.job='Kids'
        self.geo='home'
    def go_to_school(self):
        self.geo='school'
    def go_to_home(self):
        self.geo='home'
    def info(self):
        print(f"He is in {self.geo}")
        print(f"That's {self.name}. And age = {self.age}. He work with {self.job}. And raca is {self.raca}")


Oleg=Kid('Oleg')
Oleg.info()


class bus:
    kids: list

    def __init__(self):
        self.kids=[]

    def add_in_bus(self,kid):
        self.kids.append(kid)
        kid=Kid(kid)
        kid.info()

    def remove_from_bus(self,kid):
        self.kids.remove(kid)

    def info(self):
        print(f"{self.kids}")



bus=bus()
bus.add_in_bus('Eric')
bus.info()
bus.add_in_bus('Gay')
bus.info()
bus.remove_from_bus('Eric')
bus.info()




















