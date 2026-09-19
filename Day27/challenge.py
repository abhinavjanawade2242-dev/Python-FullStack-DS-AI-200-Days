import pandas as pd
#Create student Academic database
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Abhinav", "Rahul", "Amit", "Rushi", "Omi"],
    "Department": [
        "Data Science",
        "Computer Science",
        "Data Science",
        "Computer Science",
        "Data Science"
    ]
})
marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105, 106],
    "Python": [85, 72, 91, 88, 78],
    "Math": [90, 75, 88, 92, 80]
})
print("-----Student Academic Database-----\n")
print("Student Details:\n",students,"\n")
lj=pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)
rj=pd.merge(
    students,
    marks,
    on="Student_ID",
    how="right"
)
oj=pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)
print("Left Join:\n",lj,"\n")
print("Right Join:\n",rj,"\n")
print("Outer Join:\n",oj,"\n")
print("Students with Missing Marks:\n",lj[lj["Python"].isnull()])
print("Missing student information:\n",rj[rj["Name"].isnull()])