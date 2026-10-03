import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas",
        "Arjun", "Neha", "Rohan", "Sneha"
    ],

    "Department": [
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science"
    ],

    "Age": [
        20, 21, 20, 22, 20, 21,
        23, 22, 20, 21, 22, 20
    ],

    "Marks": [
        85, 72, 91, 65, 88, 78,
        95, 70, 82, 68, 90, 75
    ],

    "Attendance": [
        92, 85, 96, 70, 89, 82,
        98, 75, 90, 72, 94, 80
    ],

    "Study_Hours": [
        5, 3, 6, 2, 5, 4,
        7, 3, 5, 2, 6, 4
    ]
}
df=pd.DataFrame(data)



# 1 Basic EDA
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()


# 2 Data Quality
print("Missing values:",df.isnull().sum())
missing_percentage=(
    df.isnull().sum()/len(df)
)*100
print("Missing Percentage:\n",missing_percentage)
print("Duplicated:",df.duplicated().sum())


# 3 Numerical Analysis
print("Average Marks:",df["Marks"].mean().round(2))
print("Highest Marks",df["Marks"].max())
print("Lowest Marks:",df["Marks"].min())
print("Average Attendance:",df["Attendance"].mean())
print("Average Study Hours:",df["Study_Hours"].mean().round(2))


# 4 Categorical Analysis
print("Number of students per department:",df.groupby("Department")["Name"].count())
print("Average Marks by Department:",df.groupby("Department")["Marks"].mean().round(2))
print("Avreage Attendance by Department:",df.groupby("Department")["Attendance"].mean().round(2))


# 5 Outlier
Q1=df["Marks"].quantile(0.25)
Q3=df["Marks"].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=df[
    (df["Marks"]<lower_bound) |
    (df["Marks"]>upper_bound)
]
print("Marks outlier:",outliers)

Q1=df["Attendance"].quantile(0.25)
Q3=df["Attendance"].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=df[
    (df["Attendance"]<lower_bound) |
    (df["Attendance"]>upper_bound)
]
print("Attendance outliers:",outliers)

Q1=df["Study_Hours"].quantile(0.25)
Q3=df["Study_Hours"].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=df[
    (df["Study_Hours"]<lower_bound) |
    (df["Study_Hours"]>upper_bound)
]


# 6 Visualization 
sns.histplot(
    data=df,
    x="Marks",
    bins=5,
    kde=True
)
plt.title("Marks Histogram")
plt.show()

sns.boxplot(
    data=df,
    x="Marks"
)
plt.title("Marks boxplot")
plt.show()

sns.countplot(
    data=df,
    x="Department"
)
plt.title("Department countplot")
plt.show()

sns.barplot(
    data=df,
    x="Department",
    y="Marks"
)
plt.title("Department-wise Marks barplot")
plt.show()

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks"
)
plt.title("Study Hours v/s Marks Scatterplot")
plt.show()

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks"
)
plt.title("Attendance v/s Marks scatterplot")
plt.show()

numerical_cat=["Age","Marks","Attendance","Study_Hours"]
correlation=df[numerical_cat].corr()
sns.heatmap(
    correlation,
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()