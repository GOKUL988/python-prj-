def q1(n):
    li=[]
    print("[With argument with return]")
    i = 1
    c = 0
    while c < n:
        if i % 2 == 0:
            li.append(i)
            c = c + 1
        i = i + 1
    return li

def q2():
    li=[]
    n = int(input("how many pronic number do you want: "))
    print("No argument with return")
    c = 0
    i = 1
    print()
    print("The first", n, "pronic number is")
    while c < n:
        j = i * (i + 1)
        li.append(j)
        c = c + 1
        i = i + 1
    return li

def q3(n):
    print("with argument no return")
    t = n
    a = 0
    b = 1

    while t > b:
        c = b
        b = a + b
        a = c
    if b == t:
        print(t, "is a fibonacci number")
    else:
        print(t, "not a fibonacci number")

def q4():
    n = int(input("how many prime number do you want in 1 to n: "))
    print("No argument no return")
    t = n
    i = 1
    ct = 0
    while ct < n:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c = c + 1

        if c == 2:
            ct = ct + 1
            f = i
        i = i + 1
    print(t, "nth prime number",f)



