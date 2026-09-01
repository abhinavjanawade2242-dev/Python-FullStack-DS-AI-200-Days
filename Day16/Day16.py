#Reading csv file
import csv
with open("Day16/student.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


#Skipping the header
with open("Day16/student.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        print(row)


#DictReader
with open("Day16/student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


#Reading csv file
with open("Day16/student.csv","r") as file:
    reader=csv.DictReader(file)
    for student in reader:
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("Course:",student["course"])
        print("---------------------------")


#Writing csv file
with open("Day16/employees.csv","w",newline="") as file:
    abhi=csv.writer(file)
    abhi.writerow(["name","age","salary"])
    abhi.writerow(["Abhinav",20,60000.00])
    abhi.writerow(["Rushi",20,45000.00])
    abhi.writerow(["Omi",22,55000.00])


#writerows()
students=[["Abhinav",20,60000.00],["Rushi",20,45000.00],["Omi",22,55000.00]]
with open("Day16/employees2.csv","w",newline="") as file:
    abhi=csv.writer(file)
    abhi.writerow(["name","age","course"])
    abhi.writerows(students)


#DictWriter
studnts=[{"name":"Abhinav","age":20,"course":"Data Science"},{"name":"Rushi","age":20,"course":"ECE"}]
with open("Day16/students.csv","w",newline="") as file:
    fieldnames=["name","age","course"]
    abhi=csv.DictWriter(file,fieldnames=fieldnames)
    abhi.writeheader()
    abhi.writerows(studnts)


#sarching in dictionary
search_name=input("Enter student name:")
with open("Day16/student.csv","r") as file:
    abhi=csv.DictReader(file)
    found=False
    for student in abhi:
        if student["name"].lower()==search_name.lower():
            print(f"Name:{student["name"]} \nAge:{student["age"]} \nCourse:{student["course"]}")
            found=True
            break
    if not found:
        print("Student not found")


#csv+Exception handling
try:
    with open("Day16/student3.csv","r") as file:
        abhi=csv.DictReader(file)
        for student in abhi:
            print(student)
except FileNotFoundError as e:
    print("ERROR(File Not Found):",e)