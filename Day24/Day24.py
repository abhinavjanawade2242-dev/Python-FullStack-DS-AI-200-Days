import pandas as pd
data={
    "Name":["Abhinav","Rahul","Amit","Rushi","Omi"],
    "Age":[20,21,20,22,21],
    "Marks":[85,72,91,65,88],
    "Course":["Data Science","Computer Science","Data Science","AI","Data Science"]
}
df=pd.DataFrame(data)
print(df,"\n")


#problem 1 Display only name column
print(df["Name"])


#problem 2 Display name and marks
print(df[["Name","Marks"]],"\n")


#problem 3 Display first 3 studnts
print(df.head(3),"\n")


#problem 4 Display the last 2 student
print(df.tail(2),"\n")


#problem 5 Find shape
print(df.shape,"\n")


#problem 6 Average marks
print(df["Marks"].mean(),"\n")


#problem 7 Top students
top_students=df[df["Marks"]>80]
print(top_students,"\n")


#problem 8 Sort student by marks High to low
df=df.sort_values("Marks",ascending=False)
print(df,"\n")

#problem 9 Data science student
ds_stud=df[df["Course"]=="Data Science"]
print(ds_stud,"\n")


#info()
df.info()


#describe()
print(df.describe())