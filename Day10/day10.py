# problem 1 Student dictionary
student={"Name":"Abhi","Age":20,"Course":"DS","College":"AIET"}
for key,value in student.items():
    print(f"{key}:{value}")

#problem 2 Add marks=80 in student and later update it to 90
student["marks"]=80
print(f"Marks before update:{student["marks"]}")
student["marks"]=90
print(student)

#problem 3 Dictionary search
key=input("Enter the key:")
found=0
for k,v in student.items():
    if key==k:
        found=1
        print(f"{k}:{v}")
if found==0:
    print("Key Not Found")

#problem 4 Student marks
students={"Abhi":93,"Rushi":85,"Omi":75,"Yash":80}
for name,mark in students.items():
    print(f"{name}->{mark}")

#problem 5 student with highest marks from problem 4
highest_mark=0
highest_scorer=""
for k,v in students.items():
    if v>highest_mark:
        highest_mark=v
        highest_scorer=k
print(f"Highest Marks:{highest_mark} \nName:{highest_scorer}")

#problem 6 Count pass and fail
students["Vasu"]=25
students["Rnjeet"]=78
students["Hrushi"]=30
p,f=0,0
for name,mark in students.items():
    if mark>=40:
        p+=1
    else:
        f+=1
print(f"No. of students passed={p} \nNo. of students failed={f}")

#problem 7 Track for students individual subject marks
stud={"Name":"Abhinav","marks":{"Python":90,"Java":80,"C++":95}}
for k,v in stud.items():
    print(f"{k}:{v}")

#problem 8 Student Management System
students.clear()
students={}
for i in range(5):
    print(f"---Student {i+1} Info---")
    name=input("Name:")
    age=int(input("Age:"))
    mark=int(input("Marks:"))
    students[name]={"age":age,"marks":mark}

print("\n----Student Information----")
for name,details in students.items():
    print("Name:",name)
    print("Age:",details["age"])
    print("Marks",details["marks"])
    print()
