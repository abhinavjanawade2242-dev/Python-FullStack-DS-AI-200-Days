from abc import ABC,abstractmethod


#problem 1 Abstract Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142*(self.radius**2)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
o1=Circle(5)
o2=Rectangle(3,5)
print("Area of circle:",o1.area())
print("Area of Rectangle:",o2.area())        


#problem 2 Abstract Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start():
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
class Bus(Vehicle):
    def start(self):
        print("Bus started")
car=Car()
bike=Bike()
bus=Bus()
car.start()
bike.start()
bus.start()


#problem 3 Multiple inheritance
class Father:
    def father_skill(self):
        print("Innovative")
class Mother:
    def mother_skill(self):
        print("Creative")
class Son(Father,Mother):
    pass
obj=Son()
obj.father_skill()
obj.mother_skill()


#problem 4 Composition
class Engine:
    def start(self):
        print("Engine started")
class Car(Engine):
    def __init__(self):
        self.engine=Engine()
    def car_start(self):
        self.engine.start()
        print("Car started")
obj=Car()
obj.car_start()


#problem 4 Student System
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def disp_address(self):
        print("City:",self.city)
        print("State:",self.state)
class Student(Person,Address):
    def __init__(self, name, age,studentId,city,state):
        super().__init__(name,age)
        self.studentId=studentId
        self.address=Address(city,state)
    def disp_student(self):
        self.disp_person()
        print("StudentID:",self.studentId)
        self.address.disp_address()
student=Student("Abhinav",20,"4AL24CD001","Benadi","Karnataka")
student.disp_student()