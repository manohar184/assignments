#21: Calculate the sum and average of the digits present in a string.

string=input("Enter the string : ")
count=0
sum=0
for i in range(len(string)):
    if string[i].isnumeric():
        sum+=int(string[i])
        count+=1

if count > 0:
    average=sum/count
    print("The average num of string is : ",average)
else:
      print("No intigers are present in the string")          