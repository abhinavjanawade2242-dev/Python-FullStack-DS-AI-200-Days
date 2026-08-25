#problem 1 celsius to fahrenheit converter
def cel_to_fah(cel):
    return (cel*(9/5))+32
print(f"Temperature:{cel_to_fah(25)}F")

#problem 2 Area And perimeter of rectangle calculator
def cal_area(len,wid):
    return len*wid
def cal_peri(len,wid):
    return 2*(len+wid)
print("Area:",cal_area(10,5))
print("Perimeter:",cal_peri(10,5))

#problem 3 print even numbers
def print_even_no(*nums):
    for num in nums:
        if num%2==0:
            print(num)
print_even_no(10,20,30,23,25,71,74,58)

#problem 4 function to count number of odd and even numbers
def count(*nums):
    e,o=0,0
    for num in nums:
        if num%2==0:
            e+=1
        else:
            o+=1
    return e,o
e,o=count(10,11,12,21,31,52,24)
print(f"Even:{e} \nOdd:{o}")

#problem 5 function to find maximum number without using max() 
def cal_max(*nums):
    max=0
    for num in nums:
        if num>max:
            max=num
    return max
res=cal_max(10,50,30,90,20)
print("Maximum:",res)

#problem 6 Function to check weather a number is prime number or not
def is_prime(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count>2:
        return False
    else:
        return True
print(is_prime(3))

#problem 7 Student result
def stud_result(name,marks):
    print("----Student Result----")
    print(F"Name:{name}")
    print(f"Total:{sum(marks)}")
    print(f"Average:{sum(marks)/len(marks)}")
    print(f"Highest:{max(marks)}")
    print(f"Lowest:{min(marks)}")
marks=[80,85,90,75,88]
stud_result("Abhi",marks)

#problem 8 function to calculate sum of n numbers using *args
def cal_sum(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(cal_sum(10,20,30,40))

#problem 8 function to print student info using **kwargs
def stud_info(**details):
    print(details)
stud_info(name="Abhinav",Age=20,Course="Data Science")

#problem 9 Mini Calculator
print("----Mini Calculator----")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Exit")
choice=int(input("Choose The operation that you want to perform:"))
if choice==1:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=add(a,b)
elif choice==2:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=sub(a,b)
elif choice==3:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=mul(a,b)
elif choice==4:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=div(a,b)
elif choice==5:
    exit()
else:
    print("Invalid choice")
print("Result=",result)
