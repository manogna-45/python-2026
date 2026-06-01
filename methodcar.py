class Car:
    def __init__(self,name):
        self.name = name #attribute
    def start(self):
        print(self.name, "car has started")
car1 = Car("BMW")
car1.start()
