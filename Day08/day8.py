#list
marks=[80,90,95]
print(marks)

#Mixed data
data=["Abhi",20,93.6,True]
print(data)

#Indexing
# if list has N elements
# forward indexing=> 0 to N-1
# Negative indexing=> -1 to N
print(marks[1])
print(marks[-1])

#append()
marks.append(40)
print(marks)

#insert()
marks.insert(1,90)
print(marks)

#remove()
marks.remove(90)
print(marks)

#pop()
marks.pop(3)
print(marks)

# len()
print(len(marks))

# in 
print(95 in marks)

# Looping through list 
for mark in marks:
    print(mark)

# calculate total of list 
total=0
for i in marks:
    total+=i
print("Total of Marks=",total)

#max()
print(max(marks))

#min()
print(min(marks))

#sort()
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# Reverse() 
marks.reverse()
print(marks)

#Problem 1 Marks of student
marks=[78,85,92,67,74]
print(marks)
print(f"Total={sum(marks)} \nAverage={(sum(marks)/len(marks))} \nHighest={max(marks)} \nLowest={min(marks)}")

#problem 2 count even and odd
number=[10,15,20,23,30,35,40]
ec,oc=0,0
for i in number:
    if i%2==0:
        ec+=1
    else:
        oc+=1
print("Even numbers:",ec,"\nOdd numbers:",oc)

#problem 3 Find a student
students=["Abhi","Rushi","Sanskar","Yash","Ranjeet"]
find=str(input("Enter Name to be finded:"))
if find in students:
    print("Student found")
else:
    print("Student not found")

#problem 4 Read and display name and marks of 5 students
students=[]
marks=[]
for i in range(0,5):
    print(f"Enter Details of Student{i+1}")
    name=str(input("Enter name:"))
    mark=int(input("Enter mark:"))
    students.append(name)
    marks.append(mark)
for i in range(5):
    print(f"{students[i]}-{marks[i]}")