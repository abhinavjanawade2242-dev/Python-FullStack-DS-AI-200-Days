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