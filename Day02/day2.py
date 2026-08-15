# Comparrison Operator
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#  Logical Operator
print(a<20 and b<20)
print(a<20 or b<20)
print(not True)

#Operator Precedence
# 1 ()
# 2 **
# 3 * / // %
# 4 + -
# 5 comparisson 
# 6 not
# 7 and
# 8 or

#Problem 1 Updated marks report
name=str(input("Enter Name:"))
m1=int(input("Enter marks1:"))
m2=int(input("Enter marks2:"))
m3=int(input("Enter marks3:"))
m4=int(input("Enter marks4:"))
m5=int(input("Enter marks5:"))
m6=int(input("Enter marks6:"))
tot=m1+m2+m3+m4+m5+m6
print("====Student Report====")
print(f"Name:{name} \nTotal:{tot} \nAverage:{tot/6} \nPercentage:{(tot/600)*100} \nHighest:{max(m1,m2,m3,m4,m5,m6)} \nLowest:{min(m1,m2,m3,m4,m5,m6)}")

#Problem 2 Remainder of number divided by 2
x=int(input("Enter a number:"))
print(f"Remainder:{x%2}")

#Problem 3 Comparisson of 2 numbers
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print(f"First numbr is Greater:{n1>n2}")
print(f"First numbr is Smaller:{n1<n2}")
print(f"Both numbers are equal:{n1==n2}")

#problem 4 Chck adult or not
age=int(input("Enter age:"))
print(f"Adult:{age>=18}")

#problem 5` salary calculation with =>1)basic salary,2)HRA-20% of basic salary,3)DA-10% of basic salary 4)Gross salary
sal=int(input("Enter Basic Salary:"))
HRA=(20/100)*sal
DA=(10/100)*sal
print(f"Basic Salary:{sal} \nHRA:{HRA} \nDA:{DA} \nGross Salary:{sal+HRA+DA}")