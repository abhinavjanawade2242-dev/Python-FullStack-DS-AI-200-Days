import pandas as pd
# Student Data Analyzer
data={
    "Name":["Abhinav","rahul","Amit","Rushi","Omi","Kiran"],
    "Department":["DS","CS","DS","CS","DS","CS"],
    "Marks":[85,72,91,65,88,78],
    "Age":[20,21,20,22,20,21]
}
df=pd.DataFrame(data)
print("------Student Department Analyzer------\n")
print("Department Statistics:\n")
result=df.groupby("Department").agg(
    Average_Marks=("Marks","mean"),
    Highest_Marks=("Marks","max"),
    Lowest_Marks=("Marks","min"),
    Number_of_students=("Marks","count")
    )
result=result.reset_index()
print(result.round(2))

overall_avg=df["Marks"].mean()
overall_highest=df["Marks"].max()
overall_lowest=df["Marks"].min()
print("\nOverall Statistics:")
print("Overall Average:",round(overall_avg,2))
print("Overall Highest:",overall_highest)
print("Overall Lowest:",overall_lowest)