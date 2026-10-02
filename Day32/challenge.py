import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

    "Marks": [85, 72, 91, 65, 88, 78, 95, 70],

    "Attendance": [92, 85, 96, 70, 89, 82, 98, 75],

    "Age": [20, 21, 20, 22, 20, 21, 23, 22]
}

df = pd.DataFrame(data)


# 1 Department-wise Marks
sns.barplot(
    data=df,
    x="Department",
    y="Marks"
)
plt.title("Department-wise Marks")
plt.show()


# 2 Attendance v/s Marks
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
    hue="Department"
)
plt.title("Attendance v/s Marks")
plt.show()


# 3 Marks distribution
sns.histplot(
    data=df,
    x="Marks",
    bins=5,
    kde=True
)
plt.title("Marks Distribution")
plt.show()


# 4 Correlation Heatmap
correlation=df[["Marks","Attendance","Age"]].corr()
sns.heatmap(
    correlation,
    annot=True
)


# Bonus
fig,axes=plt.subplots(2,2,figsize=(12,8))
sns.barplot(
    data=df,
    x="Department",
    y="Marks",
    ax=axes[0,0]
)
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
    ax=axes[0,1]
)
sns.histplot(
    data=df,
    y="Marks",
    bins=5,
    kde=True
)
sns.heatmap(
    correlation,
    annot=True
)
plt.tight_layout()
plt.show()