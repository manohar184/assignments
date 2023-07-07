#20: Find all occurrences of a substring in a given string by ignoring the case.
word=input("Enter the string : ")
subString=input("Enter the sub string : ")
word=word.lower()
subString=subString.lower()
print(word)
list=[]

for i in range (0,len(word)):
    if word[i:i+len(subString)]==subString:
        list.append(i)
print(list)        
