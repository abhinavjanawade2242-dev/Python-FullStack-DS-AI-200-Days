import pandas as pd
import matplotlib.pyplot as plt

# 1 Customized line chart
days=[1,2,3,4,5]
marks=[60,65,70,80,90]
plt.plot(days,marks,marker="o",linestyle="--")
plt.title("Day v/s Marks")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.grid()
plt.show()

# 2 Bar chart with values
students = ["Abhinav", "Rahul", "Amit", "Rushi", "Omi"]
marks = [85, 72, 91, 65, 88]
bars=plt.bar(students,marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
for bar in bars:
    height=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )
plt.show()


# 3 2*2 subplots
fig,axes=plt.subplots(2,2)
axes[0,0].plot(students,marks)
axes[0,0].set_title("Student Marks")
axes[0,1].bar(students,marks)
axes[0,1].set_title("Student Marks")
axes[1,0].scatter(students,marks)
axes[1,0].set_title("Student Marks")
axes[1,1].hist(marks)
axes[1,1].set_title("Marks Distribution")
plt.tight_layout()
plt.show()