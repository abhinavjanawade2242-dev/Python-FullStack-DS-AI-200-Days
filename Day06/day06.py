# Problem 1 Find sum of digits
num=int(input("Enter a number:"))
total=0
while num!=0:
    total += (num%10)
    num=num//10
print("Sum of digits=",total)

# Problem 2 Count the number of digits
num=int(input("Enter a number:"))
count=0
while num!=0 :
    num=num//10
    count+=1
print("Total number of digits=",count)

#problem 3 Check for palindrome of number
num=int(input("Enter a number:"))
temp,rev=num,0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print(f"{temp} is a palindrome")
else:
    print("It is not palindrome")

#  Problem 4 Print all factors
num=int(input("Enter a number:"))
print("Factors:")
for i in range(1,num+1):
    if num%i==0:
        print(i)

#  Problem 5 Check it is prime number or not
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")

#problem 6 Fibonacci series
num=int(input("Enter a number:"))
a,b=0,1
print(f"Fibonacci series of first {num} numbers:")
for _ in range(num):
    print(a,end=" ")
    a,b=b,a+b
    
#problem 7 Armstrong number
num=int(input("Enter a number:"))
temp,total=num,0
while num!=0:
    rem=num%10
    total=total+(rem**3)
    num=num//10
if temp==total:
    print("It is armstrong!!")
else:
    print("It is not armstrong")

# Problem 8 Find the largest digit
num=int(input("Enter a number:"))
largest=0
while num!=0:
    if num%10>largest:
        largest=num%10
    num=num//10
print("Largest digit is ",largest)

# Problem 9 Pattern 1
num=int(input("Enter a number:"))
for i in range(num+1):
    for j in range(i):
        print(i,end="")
    print()