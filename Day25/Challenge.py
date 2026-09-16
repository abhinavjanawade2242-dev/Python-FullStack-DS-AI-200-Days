import pandas as pd
data = {
    "Name": [" Abhinav ", "Rahul", "Amit", "Rahul", "Rushi"],
    "Age": [20, 21, None, 21, 22],
    "Marks": [85, 72, 91, 72, None],
    "City": ["Mangalore", "Bangalore", "Mysore", "Bangalore", None]
}
df = pd.DataFrame(data)

print(df,end="\n")

df["Name"]=df["Name"].str.strip()

df["Age"]=df["Age"].fillna(df["Age"].mean())

df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

df["City"]=df["City"].fillna("Unknown")

df=df.drop_duplicates()
df=df.sort_values("Marks",ascending=0)
print(df)

print("Total students:",df["Name"].count())
print("Average marks:",df["Marks"].mean())
print("Highest marks:",df["Marks"].max())
print("Lowest marks:",df["Marks"].min())
print("Number of unique cities:",df["City"].nunique())