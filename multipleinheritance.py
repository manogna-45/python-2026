class Father:
    def skills1(self):
        print("Driving")
class Mother:
    def skills2(self):
        print("Dancing")
        
class Child(Father,Mother):
    pass
c1=Child()
c1.skills1()
c1.skills2()