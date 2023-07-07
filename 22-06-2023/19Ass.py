#19: Count all letters, digits, and special symbols from a given string.

word=input("Enter the string : ")
word=word.upper()
alfaCount=0
numCount=0
symbCount=0
for i in range(len(word)):
    if word[i].isupper():
        alfaCount+=1
    elif word[i].isnumeric():
        numCount+=1
    else:
        symbCount+=1
print("Letter count = ",alfaCount)
print("Digits count = ",numCount) 
print("pecial symbols count = ",symbCount)                   
