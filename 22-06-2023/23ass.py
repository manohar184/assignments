#23: Reverse a given string.
string=input("Enter the string : ")
result=""
for i in range (len(string)):
    result=string[i] + result
print(result)    
  
