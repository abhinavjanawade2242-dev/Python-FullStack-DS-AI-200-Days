import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": [
        "Abhinav",
        "Rahul",
        "Amit",
        "Rushi",
        "Omi",
        "Kiran",
        "Sanjay",
        "Vikas"
    ],
    "Marks": [
        85, 72, 91, 65,
        88, 78, 95, 70
    ],
    "Attendance": [
        92, 85, 96, 70,
        89, 82, 98, 75
    ]
}
df = pd.DataFrame(data)
 # 1 Student Marks
plt.bar(df["Name"],df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.savefig("Day30/student_marks.png")
plt.show()


#2 Marks v/s attendance
plt.scatter(df["Attendance"],df["Marks"])
plt.title("Attendance v/s Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.savefig("Day30/marks_attendance.png")
plt.show()


#3 Marks distribution
plt.hist(df["Marks"],bins=5)
plt.title("Marks distribution")
plt.xlabel("Marks")
plt.ylabel("No. of students")
plt.savefig("Day30/marks_distribution.png")
plt.show()


