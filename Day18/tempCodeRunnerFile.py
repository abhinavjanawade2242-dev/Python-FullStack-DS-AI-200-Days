class student:
#     def __init__(self,name,age,course,marks):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.marks=marks
#     def calculate_average(self):
#         avg=sum(self.marks)/len(self.marks)
#         print("Average marks:",avg)
# name=input("Enter Name:")
# age=int(input("Enter age:"))
# course=input("Enter course:")
# marks=[]
# print("enter marks in 5 subject")
# for i in range(5):
#     mark=int(input("Enter mark:"))
#     marks.append(mark)
# s=student(name,age,course,marks)
# s.calculate_average()
        

# #PROBLEM 5 product class
# class product:
#     total=0
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total_price(self):
#         self.total=self.total+(self.price*self.quantity)
#         print("Name:",self.name)
#         print("Price:",self.price)
#         print("Quantity:",self.quantity)
#         print("Total=",self.total)
# name=input("Enter name:")
# price=float(input("Enter price:"))
# quantity=int(input("Enter quantity:"))
# prod1=product(name,price,quantity)
# prod1.total_price()