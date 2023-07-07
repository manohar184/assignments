#26: Removal all characters from a string except integers.

string=input("Enter the string : ")
lenght= len(string)
newString=""
for i in range(len(string)):
    if string[i].isnumeric():
        newString+=string[i]
        
print(newString)