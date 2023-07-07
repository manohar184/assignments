#17: Append new string in the middle of a given string.

string=input("Entee the string : ")
string1= input("Enter the new string : ")
index=int(input("Enter the index : "))
second= len(string)-index
first=len(string)-second
print("New string : ",string[0:first]+string1+string[second:len(string)])
