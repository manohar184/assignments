num=4
n=1

for i in range(1,num+1):
    res=""
    for j in range(1,i+1):
        res=str(n)+res
        n+=1
    print(res)    

       