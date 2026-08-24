# Problem 1 create greet function and call it 3 times
def greet():
    print("Hello,Welcome to Python!")
for i in range(3):
    greet()

#problem 2 greet function with name
def greet(name):
    print("Hello",name)
greet("Abhinav")

#problem 3 Addition function
def add(a,b):
    return a+b
result=add(10,20)
print("Addition:",result)

#problem 4 calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
print(add(10,20))
print(sub(20,10))
print(div(20,4))
print(mul(2,4))

#problem 5 check even or odd
def check_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
check_even(10)

#problem 6 LArgest of 3 using function
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
result=largest(10,50,30)
print("Largest:",result)

#problem 7 Student Average
def avg_marks(marks):
    return sum(marks)//len(marks)
marks=[80,70,85,90,69,78]
result=avg_marks(marks)
print(result)

#problem 8 student result
def stud_result(name,marks):
    print(f"-----Student Result-----")
    print(f"Name:{name}")
    print(f"Total:{sum(marks)}")
    print(f"Average:{sum(marks)//len(marks)}")
    print(f"Percentage:{(sum(marks)/600)*100}")
    print(f"Highest Marks:{max(marks)}")
    print(f"Lowest Marks:{min(marks)}")
marks=[90,80,89,87,89,93]
stud_result("Abhinav",marks)

#problem 9 Grade calculator
def grade_calculator(percentage):
    if percentage>=90:
        print("A")
    elif percentage>=80 and percentage<90:
        print("B")
    elif percentage>=70 and percentage<80:
        print("C")
    elif percentage>=60 and percentage<70:
        print("D")
    elif percentage>=40 and percentage<60:
        print("E")
    else:
        print("F")
grade_calculator(85)

#problem 10 dictionary+python student report
student={"name":"Abhinav","age":20,"marks":[80,85,90,75,88,90]}
def stud_report(student):
    print("-----Student Report-----")
    print(f"Name:{student["name"]}")
    print(f"Age:{student["age"]}")
    print(f"Total:{sum(student["marks"])}")
    print(f"Average:{sum(student["marks"])//len(student["marks"])}")
    print(f"Highest:{max(student["marks"])}")
    print(f"Lowest:{min(student["marks"])}")
stud_report(student)