#opening and reading file
file = open("Day15/notes.txt", "r")
data=file.read()
print(data)
file.close()

#problem 1 Create a file with read mode
intro=["Name:Abhinav\n","Course:Data Science\n","Goal:Python Full Stack Developer"]
with open("Day15/intro.txt","w") as file:
    file.writelines(intro)

#problem 2 read the contents of above intro.txt
with open("Day15/intro.txt","r") as abhi:
    data=abhi.read()
print(data)

#problem 3 append "Learning Python Everyday" in intro.txt
with open("Day15/intro.txt","a") as file:
    file.write("\nLearning Python Everyday")

#problem 4 Program to count number of lines
cont=["Python\n","Java\n","C++\n","Javascript\n","SQL"]
with open("Day15/lines.txt","w") as file:
    file.writelines(cont)
count=0
with open("Day15/lines.txt","r") as file:
    for line in file:
        count+=1
print(count)


#problem 5 count words
with open("Day15/words.txt", "r") as file:
    data = file.read()
words = data.split()
print("Total words:", len(words))


#problem 6 search in file
key=str(input("Enter student name:"))
found=0
with open("Day15/student.txt","r") as file:
    for line in file:
        if key in line:
            found+=1
if found==1:
    print("Student found.")
else:
    print("Student Not Found")


#program 7 Student record
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")
with open("Day15/students.txt", "a") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Course: " + course + "\n")
    file.write("--------------------\n")
print("Student record saved successfully.")


# Problem 8 - Read Student Records
print("===== STUDENTS =====")
try:
    with open("Day15/students.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Student file does not exist.")


# Problem 9 - File Statistics
try:
    with open("Day15/words.txt", "r") as file:
        data = file.read()
    lines = data.splitlines()
    words = data.split()
    characters = len(data)
    print("===== FILE STATISTICS =====")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)
except FileNotFoundError:
    print("File does not exist.")