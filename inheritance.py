class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d1=Dog()
d1.eat()
d1.bark()
