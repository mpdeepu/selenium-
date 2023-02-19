class Vehicle:        # define parent class
   def run(self):
print 'Vehicle is running'
class Bike (Vehicle): # define child class
   def run(self):
      print 'Bike is running'

c = Bike()          # instance of child
c.run()         # child calls overridden method






#overloading method

class emp:
   def hello_emp(self,e_name=None):
   If e_name is not None:
   print(“hello”,e_name)
  else:
   Print(“Hello”)
 Emp1=emp()
Emp1.hello_emp()
Emp1.hello_emp(“Kiran”)




class Overloading:
      @Overload
      @signature()
      def getmethod(self):
             print(“First method”)
      @getMethod.overload
      @signature(“int”)
      def getmethod(self,i):
             print(“Second method”, i)
obj = Overloading()
obj.getMethod()
obj.getMethod(2)





# First product method.
# Takes two argument and print their
# product
 
 
def product(a, b):
    p = a * b
    print(p)
 
# Second product method
# Takes three argument and print their
# product
 
 
def product(a, b, c):
    p = a * b*c
    print(p)
 
# Uncommenting the below line shows an error
# product(4, 5)
 
 
# This line will call the second product method
product(4, 5, 5)


