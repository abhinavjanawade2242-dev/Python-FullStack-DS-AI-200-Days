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
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder =account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully.")
        print("Current balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully.")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance.")
    def display_balance(self):
        print("Current balance:", self.balance)
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display_balance()


#problem 4 student class
class student:
    def __init__(self,name,age,course,marks):
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks
    def calculate_average(self):
        avg=sum(self.marks)/len(self.marks)
        print("Average marks:",avg)
name=input("Enter Name:")
age=int(input("Enter age:"))
course=input("Enter course:")
marks=[]
print("enter marks in 5 subject")
for i in range(5):
    mark=int(input("Enter mark:"))
    marks.append(mark)
s=student(name,age,course,marks)
s.calculate_average()
        

#PROBLEM 5 product class
class product:
    total=0
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        self.total=self.total+(self.price*self.quantity)
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Total=",self.total)
name=input("Enter name:")
price=float(input("Enter price:"))
quantity=int(input("Enter quantity:"))
prod1=product(name,price,quantity)
prod1.total_price()


#Daily Challenge Bank Account system
class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Amount Deposited Successfully")
    def withdraw(self,amount):
        self.balance-=amount
        print("Amount Withdrawn Successfully")
    def disp_balance(self):
        print("Balance:",self.balance)
    def disp_details(self):
        print("Name:",self.name)
        print("Account Number:",self.account_number)
        print("Balance:",self.balance)
choice=10
while choice!=6:
    print("----Bank Account System----")
    print("1.Create account \n2.Deposit \n3.Withdraw \n4.Check Balance \n5.Account Details \n6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter Account name:")
        acc_number=int(input("Enter Account number:"))
        balance=float(input("Enter Balance:"))
        ac1=BankAccount(name,acc_number,balance)
    elif choice==2:
        amount=float(input("Enter amount to be Deposited:"))
        ac1.deposit(amount)
    elif choice==3:
        amount=float(input("Enter Amount to be Withdrawn:"))
        ac1.withdraw(amount)
    elif choice==4:
        ac1.disp_balance()
    elif choice==5:
        ac1.disp_details()
    elif choice==6:
        exit(0)
    else:
        print("Enter a valid Choice")