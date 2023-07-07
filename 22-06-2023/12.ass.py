#12: Find the factorial of a given number.
n= int(input("Enter the n : "))
total=0
for i in range(1,n+1):
    sum=0
    for i in range(1,i+1):
        sum+=i
        
    total=+sum
print(total)     