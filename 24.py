numbers=[10,20,10,30,20,40]
new_list=[]
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)