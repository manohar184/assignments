#18: Arrange string characters such that lowercase letters should come first.
word=input("Enter the string : ")
lString=""
ustring=""
for i in range(0,len(word)):
    if word[i].islower():
        lString+=word[i]
    else:
        ustring+=word[i]
result=lString+ustring
print(result)            
