word= "Python"
for i in range(1,len(word)+1):
    for j in range(i):
        print(word[j],end="")
    print()
for i in range(1,len(word)+1):
    for j in range(len(word)-i):
        print(word[j],end="")
    print() 


        