#4: Count the total number of digits in a number.
list=[1,"a","b","c",2,3,4,5,6,7,8,9]
count=0
for i in list:
    if str(i).isdigit():
        count+=1
print(count)        

