#29: Turn every item of a list into its square.

list=["a","b",2,"c",4,"d",5]
newList=[]
for char in list:
    if str(char).isnumeric():
        newList.append(char **2)
    else:
        newList.append(char)

print(newList)            
