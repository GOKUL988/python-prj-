def q1(n):
    print("With Argument no return")
    for i in range(1, n + 1):
        print(i, "**2", "=", i * i)

def q2():
    print("no argument no return")
    n = int(input("Enter the number:"))
    for i in range(1, n + 1):
        print(2 ** i, end=" ")

def q3(g,n):
    li=[]
    print("With argument with return")
    for i in range (1,n+1):
        li.append(g*i)
    return li

def q4():
    li=[]
    li1=[]
    print("no argument with return")
    n = int(input("given a number:"))
    s = int(input("Enter the range: "))
    for i in range(1, n + 1):
        if (i % 2 == 0):
            li.append(-i * s)
        elif (i % 2 == 1):
            li1.append(i * s)

    return li,li1

