import pandas as pd

data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas",
        "Arjun", "Neha"
    ],

    "Department": [
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science"
    ],

    "Age": [
        20, 21, 20, 22,
        20, 21, 23, 22,
        20, 21
    ],

    "Marks": [
        85, 72, 91, 65,
        88, 78, 95, 70,
        82, 68
    ],

    "Attendance": [
        92, 85, 96, 70,
        89, 82, 98, 75,
        90, 72
    ],

    "Study_Hours": [
        5, 3, 6, 2,
        5, 4, 7, 3,
        5, 2
    ]
}

df = pd.DataFrame(data)

print(df)





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD DATA
# ==========================================

data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas",
        "Arjun", "Neha"
    ],

    "Department": [
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science",
        "Data Science", "Computer Science"
    ],

    "Age": [
        20, 21, 20, 22,
        20, 21, 23, 22,
        20, 21
    ],

    "Marks": [
        85, 72, 91, 65,
        88, 78, 95, 70,
        82, 68
    ],

    "Attendance": [
        92, 85, 96, 70,
        89, 82, 98, 75,
        90, 72
    ],

    "Study_Hours": [
        5, 3, 6, 2,
        5, 4, 7, 3,
        5, 2
    ]
}

df = pd.DataFrame(data)


# ==========================================
# 2. BASIC INFORMATION
# ==========================================

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== INFORMATION =====")
df.info()


# ==========================================
# 3. MISSING VALUES
# ==========================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== MISSING PERCENTAGE =====")

missing_percentage = (
    df.isnull().sum() / len(df)
) * 100

print(missing_percentage)


# ==========================================
# 4. DUPLICATES
# ==========================================

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())


# ==========================================
# 5. NUMERICAL SUMMARY
# ==========================================

print("\n===== STATISTICS =====")
print(df.describe())


# ==========================================
# 6. CATEGORICAL ANALYSIS
# ==========================================

print("\n===== DEPARTMENT COUNTS =====")
print(df["Department"].value_counts())


# ==========================================
# 7. GROUP ANALYSIS
# ==========================================

print("\n===== DEPARTMENT-WISE AVERAGE MARKS =====")

department_marks = (
    df.groupby("Department")["Marks"]
    .mean()
)

print(department_marks)


# ==========================================
# 8. OUTLIER DETECTION
# ==========================================

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Marks"] < lower_bound) |
    (df["Marks"] > upper_bound)
]

print("\n===== POSSIBLE OUTLIERS =====")
print(outliers)


# ==========================================
# 9. VISUALIZATIONS
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Marks",
    bins=5,
    kde=True
)

plt.title("Marks Distribution")
plt.show()


plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Department",
    y="Marks"
)

plt.title("Marks by Department")
plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Department"
)

plt.title("Study Hours vs Marks")
plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
    hue="Department"
)

plt.title("Attendance vs Marks")
plt.show()


# ==========================================
# 10. CORRELATION
# ==========================================

numeric_columns = [
    "Age",
    "Marks",
    "Attendance",
    "Study_Hours"
]

correlation = df[numeric_columns].corr()

print("\n===== CORRELATION =====")
print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()