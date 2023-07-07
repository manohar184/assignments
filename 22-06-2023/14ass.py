#14: Use a loop to display elements from a given list present at odd index positions.
list=["a","b","c","d","e","f","g","h","i","j"]
list1=[]
for i in range (0,len(list)):
    if i % 2 == 0:
        list1.append(list[i])
print(list1)        


