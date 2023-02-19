class Employee:    
    id = 10   
    #name = “Harish"    
    def display (self):    
        print(self.id,self.name)

  #emp = Employee ()    
  #emp1 = Employee()
 #emp.display();
 #emp1.display();




class addition:
  a=5
  b=10
  add=a+b
  def display(self):
      print(self.add)
add=addition()
add.display();


class mul:
    x=10.25
    y=12.5
    mul=x*y
    def display(self):
        print(self.mul)
mul=mul()
mul.display();    
        
        
class rectangle:
    l=10.5
    b=12
    rect=l*b        
    def display(self):
        print(self.rect)
rect=rectangle()
rect.display();       


class simpleinterest:
    p=1500
    r=5
    t=2
    simple=(p*r*t)/100
    def display(self):
        print(self.simple)
simple=simpleinterest()
simple.display();        


class leapyear:
    year=1990
    leap=(year%4==0)
    def display(self):
        print(self.leap)
leap=leapyear() 
leap.display();       


class aggregate:
 k=85
 e=78
 h=58
 ss=85
 sc=90
 agg=(k+e+h+ss+sc)/5
 def display(self):
    print(self.agg)
agg=aggregate()
agg.display();                 
    
    
        
class bike:
    def display(self,name,gears):
     print(name,gears)
b1 = bike()      
b2 = bike()
b1.display(1,"royal");
b2.display(2,"yamaha");


class student:
    def display(self,studentname,grade):
        print(studentname,grade)
stdnt1=student()
stdnt2=student()   
stdnt1.display("ajay",1);
stdnt2.display("sanjay",2);     


