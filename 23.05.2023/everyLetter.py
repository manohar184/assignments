word="Python"
for i in range(1,len(word)+1):
    new=""
    for j in range(i):
        new=new+(word[j])

    print(new*i)    