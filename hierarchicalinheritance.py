class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Woof")
class Cat(Animal):
    def meow(self):
        print("Meow")
    
d1=Dog()
c1=Cat()
d1.bark()
c1.meow()
