class Car:
    def __init__(self,brand):
        self.brand = brand

brand_name = input("Enter car brand: ")

c1 = Car(brand_name)
print(c1.brand)