import numpy as np
#problem 1 Array creation
numbers=np.array([10,20,30,40,50])
print(numbers)

#problem 2 Array properties
print("Shape of the array:",numbers.shape)
print("Data type of the array:",numbers.dtype)
print("Size of the array:",numbers.size)
print("Number of dimensions of the array:",numbers.ndim)


#problem 3 mathematical operations
numbers=np.array([10,20,30,40,50])
print(numbers+10)
print(numbers*2)
print(numbers//5)


#problem 4 Statistics
marks=np.array([85,72,91,65,88])
print("Total:",np.sum(marks))
print("Average:",np.mean(marks))
print("Highest",np.max(marks))
print("Lowest:",np.min(marks))
print("Standard Deviation:",np.std(marks))


#problem 5 Boolean indexing
print(marks[marks>70])
print(marks[marks<50])


#problem 6 Create 2d array
matrix=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(matrix.shape)
print(matrix[0])
print(matrix[:,1])
print(matrix[2][1])


#problem 7 Reshaping
numbers=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
numbers=numbers.reshape(3,4)
print(numbers)


#problem 8 arrange()
print(np.arange(2,21,2))


#Challenge 
students = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [95, 84, 89],
    [65, 70, 75],
    [88, 92, 86]
])
