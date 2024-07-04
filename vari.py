def q1(a,b,c):
    print("With argument with return")
    d = ((a + b) / 100) * c
    res = d + a + b
    return "The total purchase cost and GST included is :", res
def q2(n,m):
    print("With argument no return")
    s = n / 100 * m
    res = s + n
    print("shirt ruppees:", n, "GST:", m, "Total cost:", res)
    print()

def q3():
    a = float(input("Enter the Basic salary:"))
    print("no argument with return")
    b = (a / 100) * 40
    c = (a / 100) * 20
    d = (a + b + c)
    return "the hra of basic salarey:", b ,"the da of basic salarey", c ,"the gross salary=", d

def q4():
    a = int(input("salarey per day:"))
    b = int(input("salarey absence day:"))
    print("no argument no return")
    c = a * 31
    d = 31 - b
    e = d * a
    print("Acatual salary of this month:", c)
    print("Total present days of this month:", d)
    print("Total income of this month:", e)









