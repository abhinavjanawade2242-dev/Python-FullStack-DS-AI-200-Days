# problem 1 Tuple 
marks=(10,20,30,40,50)
print(marks[0])
print(marks[len(marks)-1])
print(len(marks))

#problem 2 use of count()
number=(10,20,30,10,40,40,10,50,10)
print(number.count(10))

#problem 3 tuple unpacking
student=("Abhinav",20,"Data Science")
name,age,branch=student
print(name)
print(age)
print(branch)

#problem 4 Remove duplicats from the List
numbers=[10,20,10,30,20,40,10,10,50]
dup_removed=set(numbers)
print(dup_removed)

#problem 5 Find unique number of students
students=["Abhi","Rushi","Omi","Abhi","Rushi","Amit"]
print(f"Unique students:{len(set(students))}")

#problem 6 Find the common students from classA and classB
classA={"Abhi","Rushi","Yash","Omi"}
classB={"Abhi","Ranjeet","Yash"}
print(classA.intersection(classB)) #classA & classB

#problem 7 All  students of classA and classB
print(classA.union(classB)) #classA | classB

#problem 8 Find students who are in classA but not in classB
print(classA-classB)

#problem 9 Duplicate Detector
nums=[]
for i in range(10):
    print(f"Enter number {i+1}:")
    num=int(input())
    nums.append(num)
print(f"Total numbers:{len(nums)}")
print(f"Unique numbers:{len(set(nums))}")
print(f"Duplicates found:{len(nums)-len(set(nums))}")

#problem 10
studA=["Abhi","Rushi","Omi","Rahul"]
studB=["Abhi","Omi","Amit","Kiran"]
print(f"Union:{set(studA).union(set(studB))}")
print(f"Students only in A:{set(studA)-set(studB)}")
print(f"Students only in B:{set(studB)-set(studA)}")
print(f"Total unique students:{len(set(studA).union(studB))}")