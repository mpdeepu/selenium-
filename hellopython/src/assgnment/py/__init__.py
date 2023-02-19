class degree:
    def _init_(self,degree):
        self.degree = degree
    def display(self):    
        print("degree: %s" %(self.degree))
class undergraduate:
    def _init_(self,undergraduate):
        self.undergraduate = undergraduate
    def display(self):
        print("undergraduate: %s" %(self.undergraduate))
class postgraduate:
    def _init_(self,postgraduate):
        self.postgraduate = postgraduate
    def display(self):
        print("postgraduate: %s" %(self.postgraduate)) 
        
deg1 = degree("i got a degree")
deg2 = undergraduate("i am a undergraduate")
deg3 = postgraduate("i am a postgraduate")
deg1.display()
deg2.display()
deg3.display()       
        
           
           
           



class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)
emp = Employee('Mahesh', 23, 7500)
emp.display()

yee = Employee('Sanjana', 25, 8500)
yee.display()                  