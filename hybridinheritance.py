class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Woof")
class Cat(Animal):
    def meow(self):
        print("Meow")
class Puppy(Dog,Cat):
    def cry(self):
        print("Crying")
p1=Puppy()
p1.eat()
p1.bark()
p1.meow()
