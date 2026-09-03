import json

FILE_NAME = "Day17/students3.json"
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
        return students
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
def add_student():
    students = load_students()
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    if len(students) == 0:
        student_id = 1
    else:
        student_id = students[-1]["id"] + 1

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(new_student)
    save_students(students)
    print("Student added successfully.")
def view_students():
    students = load_students()
    if len(students) == 0:
        print("No students found.")
        return
    print("\n===== STUDENT LIST =====")
    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print("------------------------")
def search_student():
    students = load_students()
    name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")

            found = True
            break
    if not found:
        print("Student not found.")
def update_student():
    students = load_students()
    name = input("Enter student name to update: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found.")
            new_age = int(input("Enter new age: "))
            new_course = input("Enter new course: ")
            student["age"] = new_age
            student["course"] = new_course
            found = True
            break
    if found:
        save_students(students)
        print("Student updated successfully.")
    else:
        print("Student not found.")
def delete_student():
    students = load_students()
    name = input("Enter student name to delete: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            found = True
            break
    if found:
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Student not found.")
def student_statistics():
    students = load_students()
    if len(students) == 0:
        print("No students available.")
        return
    total_students = len(students)
    total_age = 0
    data_science = 0
    computer_science = 0
    for student in students:
        total_age += student["age"]
        if student["course"].lower() == "data science":
            data_science += 1
        elif student["course"].lower() == "computer science":
            computer_science += 1
    average_age = total_age / total_students
    print("\n===== STUDENT STATISTICS =====")
    print(f"Total Students           : {total_students}")
    print(f"Average Age              : {average_age:.2f}")
    print(f"Data Science Students    : {data_science}")
    print(f"Computer Science Students: {computer_science}")
while True:
    print("\n================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        student_statistics()
    elif choice == "7":
        print("Thank you for using Student Management System.")
        break
    else:
        print("Invalid choice. Please try again.")