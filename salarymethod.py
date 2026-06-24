class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self,percent):
        increment = self.salary * percent / 100
        self.salary += increment  
        
    def show_details(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
              
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
e1 = Employee(name,salary)
hike=int(input("Enter hike percentage: "))
e1.increase_salary(hike)
e1.show_details()
