#problem 1 Create employee class
class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
emp1=employee("Abhi",20,65000)
emp2=employee("Rahul",21,50000)
emp1.display()
emp2.display()


#problem 2 rectangle class
class rectangle:
    def area(self,l,b):
        print("Area:",l*b)
    def perimeter(self,l,b):
        print("Perimeter:",2*(l+b))
l=int(input("Enter length:"))
b=int(input("Enter width:"))
r=rectangle()
r.area(l,b)
r.perimeter(l,b)


#problem3 Bank account
class bankAccount:
    balance=0
    def deposit(self):
        amt=int(input("Enter Amount to be deposited:"))
        balance+=amt
    def withdraw(self):
        amt=int(input("Enter amount to be withdrawn:"))
        balance-=amt
    def disp_balance(self):
        print("balance:",self.balance)
b=bankAccount()
print("1)Deposit \n2)Withdraw \n3)Balance enquiry")
ch=int(input("Enter your choice:"))
for ch in range(1,4):
    if ch==1:
        b.deposit()
    elif ch==2:
        b.withdraw()
    elif ch==3:
        b.disp_balance()