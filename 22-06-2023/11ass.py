#11: Display Fibonacci series up to 10 terms.
list=[0,1]
n=int(input("Enter n :"))
for i in range(1,n-1):
    l1=list[-1]+list[-2]
    list.append(l1)
print(list)        


