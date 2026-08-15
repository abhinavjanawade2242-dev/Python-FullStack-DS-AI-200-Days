# PRINT STATEMENTS
print("Hello World")
name="Abhi"
age=20
print("Name:",name,"Age:",age)
print(f"Name:{name} Age:{age}")
print("Avoid",end=" ")
print("New Line")
print("Abhi","Rushi","Omi",sep="|")

# OPERATORS IN PYTHON
# 1)int-Integer type
# 2)float-Floating point
# 3)bool-Returns True or False
# 4)str-Used to store string format

#input()
sec=input("Enter Your Class:")
secc=int(input("Enter Your Class:"))
print(sec,"\t",secc)

#type conversion
age="20"
age=int(age)
print(type(age))

# Similar type conversion are
# 1. float()
# 2. str()
# 3. bool()
# 4. list()
# 5. tuple()

# Operators in Python
# +,-,*,/
# Note: //-Floor and **-power

# PROBLEM-1 PERSONAL INFORMATION
name=str(input("Enter your name:"))
age=int(input("Enter age:"))
city=str(input("Enter city:"))
college=str(input("Enter college:"))
course=str(input("Enter course:"))
print(f"Name:{name} \nAge:{age} \nCity:{city} \nCollege:{college} \nCourse:{course}")

# PROBLEM-2 BASIC ARITH ON TWO NUMBER
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
print(f"Addition:{n1+n2} \nSubstraction:{n1-n2} \nMultiplication:{n1*n2} \nDivision:{n1/n2}")

#PROBLEM-3 AREA AND PERIMETER OF RECTANGLE
length=int(input("Enter length of rectangle:"))
width=int(input("Enter width of rectangle:"))
print(f"Area:{length*width} \nPerimeter:{2*(length+width)}")

#PROBLEM-4 MARKS CALCULATOR
name=str(input("Enter your name:"))
m1=int(input("Enter your marks in subjct1:"))
m2=int(input("Enter your marks in subjct2:"))
m3=int(input("Enter your marks in subjct3:"))
m4=int(input("Enter your marks in subjct4:"))
m5=int(input("Enter your marks in subjct5:"))
m6=int(input("Enter your marks in subjct6:"))
total=m1+m2+m3+m4+m5+m6
avg=total/6
print(f"Total:{total} \nAverage:{avg}")