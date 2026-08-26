#problem 1 Import calculator and perform addition and substraction of 2 numbers
import utilities.calculator as calculator
print(calculator.add(10,2))
print(calculator.sub(20,10))

#problem 2 Math module function importing
import math
print(math.sqrt(144))
print(math.pow(2,3))
print(math.ceil(5.6))
print(math.floor(5.6))
print(math.factorial(6))

#problem 3 random number generator between 1 to 100
import random
print(random.randint(1,100))

#problem 4 random student selector
names=["Abhi","Omi","Rushi","Yash","Ranjeet","Ravi"]
print(random.choice(names))

#problem 5 to display current date
import datetime
today=datetime.date.today()
print("Current Date:",today)
print("Year:",today.year)
print("Month",today.month)
print("Day:",today.day)

#problem 6 import stdent
import utilities.student as student
mark=[80,75,90,85,70]
print("Total:",student.calculate_total(mark))
print("Average:",student.calculate_average(mark))
print("Highest:",student.calculate_highest(mark))
print("Lowest:",student.calculate_lowest(mark))

#problem 7 random password generator of 8 characters
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
print("Generated Password:",end="")
for i in range(8):
    print(random.choice(characters),end="")
print()

#problem 8 Random question selector
questions=["What is python?","What is a variable?","What is a function?","What is a dictionary?"]
print(random.choice(questions))