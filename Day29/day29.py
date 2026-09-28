import pandas as pd
#1 Read the csv file
df=pd.read_csv("students.csv")


#2 Describe dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)


#3 avg,max and min marks
print("Average marks:",df["Marks"].mean())
print("Highest Marks:",df["Marks"].max())
print("Lowest Marks:",df["Marks"].min())


#4 group by dept.
result=df.groupby("Department")["Marks"].mean()
print(result)


#5 Display students with marks greater than 80
print(df[df["Marks"]>80])


#6 Sort students by marks in ascending order
result=df.sort_values("Marks",ascending=False)
print(result)


#7 result column creation
df["Result"]=df["Marks"].apply(
    lambda x:"Pass" if x>=40 else "Fail"
)


#save df to processed_students.csv
df.to_csv("processed_students.csv",index=False)