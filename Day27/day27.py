import pandas as pd


#Reference dataframe
students=pd.DataFrame(
    {
        "student_id":[101,102,103,104],
        "Name":["Abhinav","Rahul","Amit","Rushi"],
        "Department":["DS","CS","DS","CS"]
    }
)
marks=pd.DataFrame(
    {
        "student_id":[101,102,103,105],
        "Python":[85,72,91,78],
        "Math":[90,75,88,80]
    }
)


#problem 1 merge with default join
result=pd.merge(
    students,
    marks,
    on="student_id"
)
print(result,"\n")


#problem 2 Inner join
result=pd.merge(
    students,
    marks,
    on="student_id",
    how="inner"
)
print(result,"\n")


#problem 3 Left join
result=pd.merge(
    students,
    marks,
    on="student_id",
    how="left"
)
print(result,"\n")


#problem 4 Right join
result=pd.merge(
    students,
    marks,
    on="student_id",
    how="right"
)
print(result,"\n")


#problem 5 Outer join
result=pd.merge(
    students,
    marks,
    on="student_id",
    how="outer"
)
print(result,"\n")


#problem 6 concat()
new_students=pd.DataFrame(
    {
        "student_id":[106,107],
        "Name":["Omi","Kiran"],
        "Department":["DS","CS"]
    }
)
result=pd.concat([students,new_students])
print(result)