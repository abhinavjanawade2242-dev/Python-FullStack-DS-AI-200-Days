#Problem 1 Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog=Dog()
dog.eat()
dog.bark()


#Problem 2 Vehicle
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Car(Vehicle):
    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
class Bike(Vehicle):
    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
car=Car("Kia",200)
bike=Bike("Duke390",187)
car.display()
bike.display()


#problem 3 Polymorphism
class Dog:
    def sound(self):
        print("Bark")
class Cow:
    def sound(self):
        print("mow")
class Cat:
    def sound(self):
        print("meow")
Animals=[Dog(),Cat(),Cow()]
for animal in Animals:
    animal.sound()


#problem 4 Bank Account Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Balance:", self.__balance)
account=BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)
account.display_balance()


#problem 5 Student inheritance
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class DSstudent(Student):
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nCourse:Data Science")
class CSstudent(Student):
    def display(self):
        print(f"Name:{self.name} \nAge:{self.age} \nCourse:Computer Science")
s1=DSstudent("Abhinav",20)
s2=CSstudent("Ravi",21)
s1.display()
s2.display()


#challenge University management
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age,studentID):
        super().__init__(name, age)
        self.studentID=studentID
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject
    def disp_teach(self):
        print(f"Name:{self.name} \nAge:{self.age} \nSubject:{self.subject}")
class DSstudent(Student):
    def __init__(self, name, age, studentID):
        super().__init__(name, age, studentID)
    def disp_stud(self):
        print(f"Name:{self.age} \nAge:{self.age} \nStudentID:{self.studentID} \nCourse:Data Science")
class CSstudent(Student):
    def __init__(self, name, age, studentID):
        super().__init__(name, age, studentID)
    def disp_stud(self):
        print(f"Name:{self.age} \nAge:{self.age} \nStudentID:{self.studentID} \nCourse:Computer Science")
p1=Teacher("Aslam",45,"Computer Networks")
p2=DSstudent("Abhinav",20,"4AL24CD001")
p3=CSstudent("Ravikant",21,"4AL24CS106")
p1.disp_teach()
p2.disp_stud()
p3.disp_stud()