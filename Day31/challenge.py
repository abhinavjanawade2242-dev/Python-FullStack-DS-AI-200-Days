import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": [
        "Abhinav", "Rahul", "Amit", "Rushi",
        "Omi", "Kiran", "Sanjay", "Vikas"
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

fig,axes=plt.subplots(2,2,figsize=(10,6))
bars=axes[0,0].bar(df["Name"],df["Marks"])
axes[0,0].set_title("Student v/s Marks")
for bar in bars:
    height=bar.get_height()
    axes[0,0].text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )
axes[0,1].scatter(df["Attendance"],df["Marks"])
axes[0,1].set_title("Attendance v/s Marks")
axes[1,0].plot(df["Name"],df["Marks"],marker="o")
axes[1,0].set_title("Student v/s Marks")
axes[1,0].grid()
axes[1,1].hist(df["Marks"],bins=5)
axes[1,1].set_title("Marks Distribution")
plt.tight_layout()
plt.savefig("Day31/Student_performance_dashboard.png",dpi=300)
plt.show()