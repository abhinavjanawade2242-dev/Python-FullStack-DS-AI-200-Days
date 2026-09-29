import matplotlib.pyplot as plt
# 1 Create a line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 130, 180]
plt.plot(months,sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()


# 2 Create Student bar chart
students = ["Abhinav", "Rahul", "Amit", "Rushi", "Omi"]
marks = [85, 72, 91, 65, 88]
plt.bar(students,marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.figure(figsize=(10,5))
plt.show()


# 3 Study hours vs marks
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 75, 85]
plt.scatter(hours,marks)
plt.title("Hours v/s marks")
plt.xlabel("Hour")
plt.ylabel("Marks")
plt.grid()
plt.show()


# 4 Marks distribution using bins
marks = [
    45, 50, 52, 55, 60,
    62, 65, 68, 70, 72,
    75, 78, 80, 82, 85, 90
]
plt.hist(marks,bins=5)
plt.title("Marks distribution")
plt.xlabel("Marks")
plt.ylabel("No. of students")
plt.show()