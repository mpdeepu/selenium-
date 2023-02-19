list = [50,45,35,11,12,5]
temp = 0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
           list[i],list[j] = list[j],list[i]
print(list)





list = [50,45,35,11,12,5]
temp = 0
for j in range(0,len(list)):
    for i in range(j+1,len(list)):
        if list[i] > list[j]:
           list[i],list[j] = list[j],list[i]
print(list)



