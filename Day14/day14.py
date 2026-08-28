#problem 1 Try except block
try:
    num=int(input("Enter a number:"))
except:
    print("Invalid Input.Please enter a number")

#problem 2 Safe division
try:
    n1=int(input("Enter number1:"))
    n2=int(input("Enter number2:"))
    result=n1/n2
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Division by zero")

#problem 3 List index
try:
    numbers=[10,20,50,45,23]
    look=int(input("Enter index:"))
    print(numbers[look])
except:
    print("Invalid index")

#problem 4 Dictionary key
try:
    student={"name":"Abhii","age":20,"Course":"Data Science"}
    key=input("Enter a key:")
    print(student[key])
except:
    print("KeyError")

#problem 5 Safe calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Error:",e)
try:
    n1=int(input("Enter number1:"))
    n2=int(input("Enter number2:"))
    print("----Choose Opertion----")
    print("1.Addition \n2.substraction \n3.Multiplication \n4.Division")
    op=int(input("Enter operation:"))
    if op==1:
        add(n1,n2)
    elif op==2:
        sub(n1,n2)
    elif op==3:
        mul(n1,n2)
    elif op==4:
        div(n1,n2)
    raise ValueError("Inavlid Operation")
except ValueError:
    print("Invalid number1 or number2 or operation")

#problem 6 Age validator
def check_age(age):
    try:
        if age<0:
            raise ValueError("Age cannot be negative")
        elif age>100:
            raise ValueError("Age cannot be more than 100")
    except ValueError as e:
        return e
    else:
        return age
age=int(input("Enter your age:"))
age=check_age(age)
print(age)

#problem 7 Student marks validator
def marks_validator(marks):
    try:
        if marks<0 or marks>100:
            raise ValueError("Invalid Marks")
    except ValueError as e:
        return e
    else:
        return marks
marks=input("Enter marks:")
marks=marks_validator(marks)
print(marks)

