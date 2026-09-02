#problem 1 count number of students
import csv
with open("Day16/student.csv","r") as file:
    abhi=csv.reader(file)
    next(abhi)
    count=0
    for student in abhi:
        count+=1
print(count)


#problem 2 Find data science students
with open("Day16/student.csv","r") as file:
    abhi=csv.reader(file)
    next(abhi)
    for row in abhi:
        if row[2]=="Data Science":
            print(row)
            break


#problem 3 Average age
with open("Day16/student.csv","r") as file:
    total_age,count=0,0
    abhi=csv.DictReader(file)
    for row in abhi:
        total_age+=int(row["age"])
        count+=1
average=total_age/count
print("Average age:",average)


#problem 4 Add student to student.csv
# with open("Day16/student.csv","a") as file:
#     abhi=csv.writer(file)
#     abhi.writerow(["Ranjeet",21,"ECE"])


#problem 5 search student
found=False
Search_student=input("Enter student name:")
with open("Day16/student.csv","r") as file:
    abhi=csv.DictReader(file)
    for student in abhi:
        if student["name"].lower()==Search_student.lower():
            print("Student found")
            print(f"Name:{student["name"]} \nAge:{student["age"]} \nCourse:{student["course"]}")
            found=True
            break
if not found:
    print("Student not found")


#problem 6 Student statistics
with open("Day16/student2.csv","r") as file:
    courses={}
    abhi=csv.DictReader(file)
    total_age,i,j,count=0,0,0,0
    for row in abhi:
        count+=1
        total_age+=int(row["age"])
        if row["course"].lower()=="Data Science".lower():
            i+=1
            courses["Data Science Student:"]=i
        elif row["course"]=="Computer Science":
            j+=1
            courses["Computer Science Student:"]=j
print("----Student Statistics----")
print(f"Total Students:{count} \nAverage Age:{total_age/count} \nData Science Students:{i} \nComputer Science Students:{j}")