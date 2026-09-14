import numpy as np
import random


#problem 1 Column extraction
data=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ])
print(data[0])
print(data[2])
print(data[:,0])
print(data[:,1])


#problem 2 Slicing
print(data[0:2,0:2])


#problem 3 Axis
marks=np.array([
    [80,90,70],
    [60,75,85],
    [90,85,95]
])
print("Total marks of each student:",np.sum(marks,axis=1))
print("Total marks for each subject:",np.sum(marks,axis=0))
print("Average marks of each student:",(np.sum(marks,axis=1)/300)*100)
print("Average marks for each subject:",(np.sum(marks,axis=0)/300)*100)


#problem 4 Broadcasting
prices=np.array([
    [100,200,300],
    [400,500,600]
])
print(prices+10)


#problem 5 random data
np.random.seed(10)
marks=np.random.randint(1,101,10)
print("Maximum:",np.max(marks))
print("Minimum:",np.min(marks))
print("AverageP:",np.mean(marks))


#problem 6 Transpose
data=np.array([
    [1,2,3],
    [4,5,6]
])
print(data.T)


#problem 7 Matrix multiplication
A=np.array([
    [1,2],
    [3,4]
])
B=np.array([
    [5,6],
    [7,8]
])
print("A*B:\n",A*B)
print("A@B:\n",A@B)


#Challenge Employee Salary Analyzer
employees=np.array([
    [25000,2],
    [32000,3],
    [45000,5],
    [28000,2],
    [55000,7],
    [38000,4]
])
print("Average Salary:",np.mean(employees[:,0]))
print("Highest Salary:",np.max(employees[:,0]))
print("Lowest Salary:",np.min(employees[:,0]))
print("Average Experience:",np.mean(employees[:,1]))
print("Employee having salary greater than 40000:\n")
for sal in employees[:,0]:
    if sal>42000:
        print(sal)
print("Employees with experience greater than 3 years:\n")
for exp in employees[:,1]:
    if exp>3:
        print(exp)
fin_sal=employees[:,0]+2000
print("Final Salaries:",fin_sal)