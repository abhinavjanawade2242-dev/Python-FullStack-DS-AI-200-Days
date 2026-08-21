#Problem 1 print 3*3 grid
for i in range(3):
    for j in range(3):
        print("* ",end="")
    print()

# Problem 2 print number in rows
for i in range(3):
    for j in range(3):
        print(f"{j+1}",end=" ")
        j+=1
    print()
    i+=1

# problem 3 increasing star pattern
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()

#problem 4 increasing number pattern
for i in range(5):
    for j in range(i):
        print(f"{j+1}",end=" ")
    print()

#problem 5 multiplication table from 1 to 5
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()

