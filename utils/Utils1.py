class Human:
    age: int
    name: str

    def __init__(self, name='Igor'):
        self.name=name
        self.age=30

    def say_hello(self):
        print(f"{self.name} say hello!")
