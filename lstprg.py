def q1(n):
    print("[With argument with return]")
    list1 = []
    for i in range(n):
        list1.append(int(input("Enter the strings:")))
    mid = len(list1) // 2

    c = list1[mid:]
    s = list1[:mid]
    return "Add the first part to the end",c + s

def q2():
    n = int(input("Enter the range:"))
    print("[no argument with return]")
    lis = []
    for i in range(0, n + 1):
        if i % 2 == 1:
            lis.append(i)
    des = []
    for j in range(len(lis) - 1, -1, -1):
        des.append(lis[j])
    return des

def q3(n):
    print("[with argument no return]")
    lis = []
    for i in range(n):
        lis.append(int(input("Enter the age of employee:")))
    c = 0
    s = 0
    t = 0
    r = 0
    for i in lis:
        if i > 24 and i < 36:
            c = c + 1
        elif i > 35 and i < 46:
            s = s + 1
        elif i > 45 and i < 56:
            t = t + 1
        elif i > 55:
            r = r + 1
    print("First category employees=", c)
    print("Second category employees=", s)
    print("Third category employees=", t)
    print("Others employees=", r)

def q4():
    n = int(input("Enter the range of values:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter the value:")))
    print()
    a = int(input("Enter the divisor:"))
    f = 1
    for i in lis:
        f = f * i

    s = f % a
    print("Reminder for the product is", s)