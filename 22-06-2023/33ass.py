#33: Remove all occurrences of a specific item from a list.

list=["a","b","c","d","e","c","f","g","c"]
list1=list.copy()
item=input("Enter the item : ")
for i in range(len(list)):
    print(i)
    if list[i] == item :
        list1.remove(item)
print(list1)