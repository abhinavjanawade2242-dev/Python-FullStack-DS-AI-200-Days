import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas"
    ],

    "Department": [
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science"
    ],

    "Marks": [
        85, 72, 91, 65,
        88, 78, 95, 70
    ],

    "Attendance": [
        92, 85, 96, 70,
        89, 82, 98, 75
    ],

    "Age": [
        20, 21, 20, 22,
        20, 21, 23, 22
    ]
}

df = pd.DataFrame(data)

print(df)


# 1 Scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
    hue="Department"
)
plt.title("Attendance v/s marks")
plt.grid()
plt.show()


# 2 Count plot
sns.countplot(
    data=df,
    x="Department"
)
plt.title("Number of Students per department")
plt.show()


# 3 Histogram with bins and kde
sns.histplot(
    data=df,
    y="Marks",
    bins=5,
    kde=True
)
plt.title("Marks Distribution")
plt.show()


#4 Box plot
sns.boxplot(
    data=df,
    x="Department",
    y="Marks"
)
plt.title("Marks Distribution by department")
plt.show()


# 5 correlation heatmap
correlation=df[["Marks","Attendance","Age"]]
sns.heatmap(
    correlation,
    annot=True
)
plt.title("HeatMap")
plt.show()