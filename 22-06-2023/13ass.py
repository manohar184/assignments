#13: Reverse a given integer number.
n= int(input("Enter the n : "))
n=str(n)
m=""
for i in range(len(n)):
    m=n[-i]+m
print(m)    