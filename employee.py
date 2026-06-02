class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def bonus(self):
        bonus_amount=self.salary*0.10
        print("Bonus", bonus_amount)
e1=Employee("Manogna", 500000)
e1.bonus()