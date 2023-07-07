#25: Remove empty strings from a list of strings.

list=["abc","","def","","ghi"]
list1=[]
for i in list:
    if len(i) > 0:
        list1.append(i)
print(list1)        