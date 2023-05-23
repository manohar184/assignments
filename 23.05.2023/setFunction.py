a= "ABBCDEFFGHILJK"
b=[]
for item in a:
    b.append(item)
c=set(b)
d=list(c)   
d=sorted(d)
for item in d:
    print(item,end="")
print()    

