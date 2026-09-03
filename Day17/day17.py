import json
#problem 1 create json string
student={"name":"Abhinav","age":20,"course":"Data Science"}
data=json.dumps(student)
print(data,type(data))


#problem 2 Write JSON file
student={"name":"Abhinav","age":20,"course":"Data Science"}
with open("Day17/student.json","w") as file:
    json.dump(student,file,indent=4)


#problem 3 Read json
with open("Day17/student.json","r") as file:
    data=json.load(file)
print(data) 


#problem 4 write multiple student
students=[
    {
        "name":"Abhinav",
        "age":20,
        "course":"Data Science"
    },
    {
        "name":"Rahul",
        "age":21,
        "course":"Computer Science"
    },
    {
        "name":"Amit",
        "age":22,
        "course":"Data Science"
    }
]
with open("Day17/students.json","w") as file:
    json.dump(students,file,indent=4)


#problem 5 search data science students in students.json
with open("Day17/students.json","r") as file:
    students=json.load(file)
for student in students:
    if student["course"]=="Data Science":
        print(student["name"])


#problem 6 calculate total student and average age from students.json
count,total_age=0,0
with open("Day17/students.json","r") as file:
    students=json.load(file)
for student in students:
    count+=1
    total_age+=int(student["age"])
print("Total students:",count)
print("Average age:",total_age/count)


#problem 7 Add new student to students.csv
with open("Day17/students.json","r") as file:
    student=json.load(file)
new_stud={"name":"Rushi","age":20,"course":"ECE"}
student.append(new_stud)
with open("Day17/students2.json","w") as file:
    json.dump(student,file,indent=4)


#problem 8 Update student age
name=input("Enter student name:")
age=input("Enter new age:")
with open("Day17/students2.json","r") as file:
    students=json.load(file)
for student in students:
    if student["name"]==name:
        student["age"]=age
with open("Day17/students2.json","w") as file:
    json.dump(students,file,indent=4)


#problem 9 nested json
student={
    "name":"Abhinav",
    "skills":{
        "programming":["Python","SQL"],
        "data_science":["Pandas","NumPy"],
        "ai":["Machine Learning","LLM"]
    }
}
print(student["skills"]["programming"][0])
print(student["skills"]["data_science"][0])
print(student["skills"]["ai"][0])