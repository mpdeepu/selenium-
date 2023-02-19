def my_function(fname,sno):
  print(fname)
  print(sno)
my_function("Emil",1)
my_function("Tobias",2)
my_function("Linus",4)



def org(department,role):
  print(department)
  print(role)
    org("quality","inspection")
org("purchase","procurement")
org("store","inward")
org("sales","marketing")





#return statements
def add_one(x):
     # No return statement at all
     result = x+5
     return result
output = add_one(5)
print(output)
