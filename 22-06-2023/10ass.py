#10: Write a program to display all prime numbers within a range.

num= int(input("Enter the number : "))
if num == 1:
    print(num,"is not a prime number")
elif num > 1:
    count=0
    for i in range(2,num):
        if num % i == 0:
            count+=1
    print(count) 
    if count >=1:
        print(num,"is a not a prime number")
    else:
        print(num,"is prime number")    