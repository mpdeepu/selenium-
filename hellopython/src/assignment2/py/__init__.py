
num=int(input("enter a number :"))
for i in range(1,num+1):
    print(i,end='')
print("")
for j in range(0,num):
    print(num-j,end='')  
print("")





myname = "stilllearningpython"
addup = 0
for letters in myname:
        addup +=1
print(addup)

 


addon = 0
myname = "mahadevaprasad"
character = 'a'
for i in myname:
    if (i == 'a'):  
        addon +=1
print("number of character in myname:")
print(addon)





        
        
#def reverse(name):
  #string = " "
  #for i in name:
       # string = i+ string
        #return string
#x="mahadevaprasad"
#print(x)
#print(reverse(x))










def reverse(x):
    str=" "
    for i in x:
        str=i+str
    return str
i="KARNATAKA"
print("your name :",end="")
print(i)
print("reversed name:",end="")
print(reverse(i))

        
    



