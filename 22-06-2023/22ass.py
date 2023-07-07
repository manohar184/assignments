#22: Write a program to count occurrences of all characters within a string.
word=input("Enter the string : ")
subString=input("Enter the sub string : ")
word=word.lower()
subString=subString.lower()
print(word)
list=[]

for i in range (0,len(word)):
    if word[i:i+len(subString)]==subString:
        list.append(i)
print(len(list)) 