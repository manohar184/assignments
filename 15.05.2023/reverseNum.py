n= int(input("enter the number :"))

for i in range(0 , n):
    for j in range (0,n-i):
        print(i+1, end=" ")
    print()