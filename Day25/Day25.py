import pandas as pd


#problem 1 Missing Values
data={
    "Name":["Abhinav","Rahul","Amit","Rushi"],
    "Age":[20,None,21,22],
    "Marks":[85,72,None,90]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(20)
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df,"\n")


#problem 2 Remove duplicates
data={
    "Name":["Abhinav","Rahul","Amit","Rahul"],
    "Marks":[85,72,91,72]
}
df=pd.DataFrame(data)
print(df.duplicated())
df=df.drop_duplicates()
print("\n",df)


#problem 3 String Cleaning
data={"Name":["abhinav","RAHUL","amit","Rushi"]}
df=pd.DataFrame(data)
print(df["Name"].str.upper(),"\n")


#problem 4 City Analysis
data={
    "Name":["A","B","C","D","E"],
    "City":["Mangalore","Bangalore","Mangalore","Mysore","Bangalore"]
}
df=pd.DataFrame(data)
print(df["City"].unique())
print(df["City"].nunique())
print(df["City"].value_counts())