import pandas as pd
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