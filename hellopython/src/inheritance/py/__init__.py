class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()







class area: 
    
    def circle(self,pi,r):  
        self.circle=pi*r*r
        print("area of circle",self.circle)  
  
class rect(area):  
    def rectangle(self,l,b):  
        self.rectangle=l*b
        print("area of rectangle",self.rectangle)  

class square(rect):  
   
    def squ(self,s,s1):  
        self.squ=s*s1
        print("area of square",self.squ)  
v= square()  
v.rectangle(5,6)  
v.circle(3.14,5)  
v.squ(5,5)