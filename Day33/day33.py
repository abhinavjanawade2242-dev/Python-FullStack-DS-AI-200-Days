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