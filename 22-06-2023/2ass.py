# 2. Write a program to print multiplication table of a given number.

n= int(input("Enter table number:"))

for i in range(1,10+1):
    print(str(n)+"X"+str(i)+"="+str(n*i))
    