import pandas as pd

data = {
    "Name": [
        "Abhinav",
        " Rahul ",
        "Amit",
        "Rushi",
        "Omi",
        "Kiran",
        "Sanjay",
        "Vikas",
        "Abhinav",
        None
    ],

    "Age": [
        20,
        21,
        20,
        None,
        20,
        21,
        23,
        150,
        20,
        22
    ],

    "Department": [
        "Data Science",
        "Computer Science",
        "data science",
        "Computer Science",
        "Data Science",
        None,
        "Data Science",
        "Computer Science",
        "Data Science",
        "Computer Science"
    ],

    "Marks": [
        85,
        72,
        91,
        65,
        None,
        78,
        95,
        300,
        85,
        75
    ],

    "Attendance": [
        92,
        85,
        96,
        70,
        89,
        None,
        98,
        75,
        92,
        80
    ]
}

df = pd.DataFrame(data)

print(df)