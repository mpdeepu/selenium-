weight = int(input("print the weight"));
height = float(input("print the height"));
bmi = weight/float(height*height)
if bmi < 18.5:
    print('underweight')
elif bmi>=18.5 and bmi<25:
    print("normal")
elif bmi >=25 and bmi <=35:
    print("overweight")
else:
    print("obesity")              
    
    
    
    
fah = int(input("enter value of temparature in fahrenheit:"))
cel = (fah-32)/1.8
print("equivalent temperature in celcius:",cel)





    
    
    
    