import pandas as pd
#Given
data={
    "Name":["Abhinav","rahul","Amit","Rushi","Omi","Kiran"],
    "Department":["DS","CS","DS","CS","DS","CS"],
    "Marks":[85,72,91,65,88,78],
    "Age":[20,21,20,22,20,21]
}
df=pd.DataFrame(data)


#problem 1 Find average marks of each department
result=df.groupby("Department")["Marks"].mean()
print("\nAverage Marks by dept:\n",result)


#problem 2 Find the highest marks in each department
result=df.groupby("Department")["Marks"].max()
print("\nMax marks by dept:\n",result)


#problem 3 Find the lowest marks in each department
result=df.groupby("Department")["Marks"].min()
print("\nMin marks by dept:\n",result)


#problem 4 Count no. of students in each department
result=df.groupby("Department")["Department"].count()
print("\nNo. of students by dept:\n",result)


#problem 5 Find the total marks of each department
result=df.groupby("Department")["Marks"].sum()
print("\nTotal marks by department:\n",result)


#problem 6 Use of agg()
result=df.groupby("Department")["Marks"].agg(["mean","max","min","count"])
print("\n",result)


#problem 7 Find average of both Marks and Age
result=df.groupby("Department")[["Marks","Age"]].mean()
print("\n",result)