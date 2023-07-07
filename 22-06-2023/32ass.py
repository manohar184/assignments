#32: Replace list’s item with new value if found.
list=["a","b","c","d","e","f","g"]
item=input("Enter the item : ")
newItem=input("Enter the new item : ")
index=0
for i in range(len(list)):
    if list[i] == item :
        index= i
list[index]=newItem
print(list)        
        