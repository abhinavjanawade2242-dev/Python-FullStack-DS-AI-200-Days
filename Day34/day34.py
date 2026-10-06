import pandas as pd
import numpy as np
import statistics
from scipy.stats import skew, zscore

data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas",
        "Arjun", "Neha", "Rohan", "Sneha"
    ],
    "Marks": [
        85, 72, 91, 65,
        88, 78, 95, 70,
        82, 68, 90, 75
    ],
    "Attendance": [
        92, 85, 96, 70,
        89, 82, 98, 75,
        90, 72, 94, 80
    ],
    "Study_Hours": [
        5, 3, 6, 2,
        5, 4, 7, 3,
        5, 2, 6, 4
    ]
}

df = pd.DataFrame(data)

# Mean
print("Mean Marks:", df["Marks"].mean())

# Median
print("Median Marks:", df["Marks"].median())

# Mode
print("Mode Marks:", statistics.mode(df["Marks"]))

# Range
print("Range:", df["Marks"].max() - df["Marks"].min())

# Variance
print("Variance:", df["Marks"].var())

# Standard deviation
print("Standard Deviation:", df["Marks"].std())

# Quartiles
Q1 = df["Marks"].quantile(0.25)
Q2 = df["Marks"].quantile(0.50)
Q3 = df["Marks"].quantile(0.75)

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

# IQR
IQR = Q3 - Q1

print("IQR:", IQR)

# Skewness
print("Skewness:", skew(df["Marks"]))

# Correlation
print("\nCorrelation:")
print(df[["Marks", "Attendance", "Study_Hours"]].corr())

# Z-score
df["Marks_ZScore"] = zscore(df["Marks"])

print("\nZ-Scores:")
print(df[["Name", "Marks", "Marks_ZScore"]])


# 1 Basic statisctics
marks=[55,60,65,70,75,80,85,90]
print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Minimum:",min(marks))
print("Maximum:",max(marks))
print("Range:",max(marks)-min(marks))
print("Variance:",np.var(marks))
print("Standard Deviation:",np.std(marks))


# 2 Quartile analysis
marks = [45, 50, 52, 55, 60, 65, 70, 75, 80, 100]
Q1=np.percentile(marks,25)
Q2=np.percentile(marks,50)
Q3=np.percentile(marks,75)
IQR=Q3-Q1
print(f"Q1:{Q1} \nQ2:{Q2} \nQ3:{Q3} \nIQR:{IQR}")
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
print("Lower bound:",lower)
print("Upper bound:",upper)
outlier=[]
for mark in marks:
    if mark<lower or mark>upper:
        outlier.append(mark)
print("Outlier:",outlier)


# 3 Correlation
study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 50, 55, 62, 70, 78, 85]
correlation=np.corrcoef(study_hours,marks)
print(correlation)