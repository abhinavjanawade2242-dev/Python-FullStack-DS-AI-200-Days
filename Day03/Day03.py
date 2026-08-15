# Conditional statement
# 1. if statement
# 2. if-else statement
# 3. elif statement
# :=>indicates the begining of block of Code 
# indentation=>Used to determine ehich block of code belongs to which if 

# Program 1 Adult checker using if-else 
age=int(input("Enter Age:"))
if age>=18:
    print("Adult")
else:
    print("Minor")

# Program 2 Grade Assigning based on marks
marks=int(input("Enter the marks:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Fail")

# 4) nested if statement

#Program 3 Check weather number is positive or negative
num=int(input("Enter a number:"))
if num>=0:
    print("Number is positive")
else:
    print("Number is negative")

# Program 4  check weather number is even or odd
n1=int(input("Enter a number:"))
if n1%2==0:
    print("Number is even")
else:
    print("Number is odd")

# Program 5 Largest of 3 number using conditional statement
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a," is largest")
elif b>a and b>c:
    print(b," is largest")
else:
    print(c," is largest")

# Program 6 Simple Authentication system
correct_username="Abhi"
correct_password="Abhi@2006"
username=str(input("Enter your username:"))
password=str(input("Enter your password:"))
if correct_username==username and correct_password==password:
    print("Log-in Successful")
else:
    print("Invalid username or password")

# Mini-Project Student Result System
name=str(input("Enter Name:"))
m1=int(input("Enter marks1:"))
m2=int(input("Enter marks2:"))
m3=int(input("Enter marks3:"))
m4=int(input("Enter marks4:"))
m5=int(input("Enter marks5:"))
m6=int(input("Enter marks6:"))
tot=m1+m2+m3+m4+m5+m6
avg=(tot/600)*100
print("====Student Result====")
print(f"\tName:{name}")
print(f"\tTotal:{tot}")
print(f"\tPercentage:{avg}")
if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40 and m6>=40: 
    if avg>=90:
        grade='A'
    elif avg>80:
        grade='B'
    elif avg>=70:
        grade='C'
    elif avg>=60:
        grade='D'
    elif avg>=40:
        grade="pass"
    print(f"\tGrade:{grade}")
    print(f"\tStatus:Pass")
else:
    grade="Fail"
    print(f"\tGrade:{grade}")
    print(f"\tStatus:Fail")
