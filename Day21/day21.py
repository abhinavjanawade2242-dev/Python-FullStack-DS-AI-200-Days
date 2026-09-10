# problem 1 Square of number using list comphrension
numbers=[1,2,3,4,5,6,7,8,9,10]
result=[n*n for n in numbers]
print(result)

#problem 2 Using list comphrension extract only even numbers
even_num=[n for n in numbers if n%2==0]
print(even_num)


#problem 3 only name of students
students=[
    {"name":"Abhinav","marks":84},
    {"name":"Rahul","marks":72},
    {"name":"Amit","marks":91}
    ]
result=[student["name"] for student in students]
print(result)


#problem 4 top students
students=[
    {"name":"Abhinav","marks":84},
    {"name":"Rahul","marks":72},
    {"name":"Amit","marks":91},
    {"name":"Rushi","marks":78}
    ]
result=[student["name"] for student in students if student["marks"]>80]
print(result)


#problem 5 sort students by highest marks using lambda
students.sort(key=lambda student:student["marks"],reverse=True)
print(students)


#problem 6 map()
numbers=[2,4,6,8,10]
result=map(lambda x:x*3,numbers)
print(list(result))


#problem 7 filter()
numbers=[5,12,17,20,25,30]
result=filter(lambda x:x>15,numbers)
print(list(result))


#problem 8 zip()
names=["Abhinav","Rahul","Amit"]
marks=[85,72,91]
result=zip(names,marks)
print(list(result))


#problem 9 enumerate()
subjects=["Python","DBMS","Math","AI"]
for index,name in enumerate(subjects,start=1):
    print(index,name)


#Challenge Student Data Analyzer
students = [
    {"name": "Abhinav", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Rushi", "marks": 65},
    {"name": "Omi", "marks": 88}
]
print("----Student Data Analyzer----")
names=[student["name"] for student in students]
for name in names:
    print(name)
print("\nTop Students:")
top_stud=[student["name"] for student in students if student["marks"]>80]
for stud in top_stud:
    print(stud)
print()
hm,lm,sum,count=0,100,0,0
for student in students:
    count+=1
    sum=sum+student["marks"]
    if student["marks"]>hm:
        hm=student["marks"]
    elif student["marks"]<lm:
        lm=student["marks"]
print("Highest Marks:",hm)
print("Lowest Marks:",lm)
print("Average Marks:",sum/count)