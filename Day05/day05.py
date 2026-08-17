#Looping statements
# 1. while Loop 
# 2. for loop 
#Problem 1 Print 1 to 10 using while loop
count=1
while count<=10:
    print(count)
    count+=1

#problem 2 print 10 to 1 using while loop
count=10
while count>=1:
    print(count)
    count-=1

#Problem 3 print 0 to 10 using for loop
for i in range(11):
    print(i)

#problem 4 print 1 to 10 using for loop
for i in range(1,11):
    print(i)

#problem 5 print all even number between 0 to 11 using for
for i in range(0,11,2):
    print(i)

#problem 6 print 10 to 1 using for loop
for i in range(10,0,-1):
    print(i)

#problem 7 sum of first 10 integers
sum=0
for i in range(1,11):
    sum+=i
print("Sum of first 10 integers is:",sum)

#problem 8 Multiplication table generator
num=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num}*{i}={i*num}")

#problem 9 Demonstration of break
for i in range(10):
    if i==6:
        break
    print(i)

#problem 10 demonstration of continue
for i in range(10):
    if i==6:
        continue
    print(i)

#problem 11 Demonstration of nested loop
for i in range(1,4):
    for j in range(1,4):
        print(f"for i={i} and j={j}")

#problem 12 Sum of first N numbers
num=int(input("Enter the value of N:"))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
print(f"Sum of first {num} numbers is {sum}")

#problem 13 Count number of even number between 1 to N
n=int(input("Enter the value of N:"))
count=0
for i in range(2,n+1,2):
    count+=1
print(f"Total number of even numbers between 2 to {n} is {count}")

#problem 14 Program to find the factorial of number N
n=int(input("Enter the value of N:"))
fact=1
for i in range(2,n+1):
    fact*=i
print(f"Factorial of {n} is {fact}")

#problem 15 Program to reverse a number
reverse=0
num=int(input("Enter a number:"))
while num!=0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print("Number after reversing is ",reverse)

#problem 16 Number guessing game
secret,guess,count=26,0,0
while guess!=secret:
    guess=int(input("Guess the number I kept in mind:"))
    count+=1
    if guess==secret:
        break
    print("Try again!!")
print(f"You guessed it correct in {count} attempts")
