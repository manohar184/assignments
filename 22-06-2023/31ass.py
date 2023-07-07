#31: Add new item to list after a specified item.

list=["a","b","c","d","e","f","g"]
sItem=input("Enter the Item : ")
item=input("Enter the new Item : ")
index=0
for i in range (len(list)-1):
    if list[i] == sItem:
        index=i+1
list[index]=item
print(list)        