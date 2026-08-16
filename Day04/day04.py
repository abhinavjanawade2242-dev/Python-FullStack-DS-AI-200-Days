#Problem 1 Check weather a number is +ve,-ve or 0
num=int(input("Enter a number:"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is 0")

#Problem 2 Grade calculator considering validity of marks
name=str(input("Enter Name:"))
m1=int(input("Enter marks1:"))
m2=int(input("Enter marks2:"))
m3=int(input("Enter marks3:"))
m4=int(input("Enter marks4:"))
m5=int(input("Enter marks5:"))
m6=int(input("Enter marks6:"))
if (m1>=0 and m1<=100) and (m2>=0 and m2<=100) and (m3>=0 and m3<=100) and (m4>=0 and m4<=100) and (m5>=0 and m5<=100) and (m6>=0 and m6<=100):
    tot=m1+m2+m3+m4+m5+m6
    avg=(tot/600)*100
    print("====Student Result====")
    print(f"\tName:{name}")
    print(f"\tTotal:{tot}")
    print(f"\tPercentage:{avg}")
    if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40 and m6>=40: 
        if avg>=90:
            grade='A'
        elif avg>=80:
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
else:
    print("Invalid marks")

#Problem 3 Student Eligibility Checker
name=str(input("Enter Name:"))
age=int(input("Enter age:"))
marks=int(input("Enter marks:"))
attend=int(input("Enter Attendance"))
if age>=18 and marks>=60 and attend>=75:
    stat="Eligible"
else:
    stat="Not Eligible"
print("====Eligibility Report====")
print("\tName:",name)
print("\tAge:",age)
print("\tMarks:",marks)
print("\tAttendance:",attend)
print("\tStatus",stat)

