def q1(a):
    print("[with argument with return]")
    if a <= 100:
        return "free of cost"
    elif a <= 200:
        return (a - 100) * 2.25
    elif a <= 400:
        return (100) * 2.25 + (a - 200) * 4.5
    else:
        return (100) * 2.25 + (200) * 4.5 + (a - 400) * 6

def q2(a,b,c):
    if a < b and a < c and b < c:
        print("a,b,c")
    elif b < a and b < c and c < a:
        print("b,c,a")
    elif c < a and c < b and a < b:
        print("c,a,b")
    elif b < a and b < c and a < c:
        print("b,a,c")
    elif a < b and a < c and c < b:
        print("a,c,b")
    elif c < b and c < a and b < a:
        print("c,b,a")
    else:
        print("invalid")

def q3():
    a = float(input("Enter the hardness of steel:"))
    b = float(input("Enter the carbon conduct of the steel:"))
    c = float(input("Enter the tensile:"))

    print("no argument with return")
    if a > 50 and b < 0.7 and c > 5600:
        return "grade 10"
    elif a > 50 and b < 0.7 and c <= 5600:
        return "grade 9"
    elif a <= 50 and b < 0.7 and c > 5600:
        return "grade 8"
    elif a > 50 and b >= 0.7 and c > 5600:
        return "grade 7"
    elif a > 50 or b < 0.7 or c > 5600:
        return "grade 6"
    elif a <= 50 and b >= 0.7 and c <= 5600:
        return "grade 5"
    else:
        return "invalid"

def q4():
    y = int(input("Enter the year: "))
    m = int(input("Enter the month: "))
    d = int(input("Enter the day: "))

    if y > 0 and m > 0 and m <= 12 and d > 0:

        if m > 0 and m <= 12:
            if (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12):
                if d <= 31:
                    if (d < 31):
                        print(d + 1, m, y)
                    elif (d == 31):
                        print(31 - 30)
                        if (m < 12):
                            print(m + 1)
                        elif (m == 12):
                            print(31 - 30, m - 11, y + 1)

                else:
                    print("date is not valid")
            elif m == 2:
                if (y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0):
                    print("leap year")
                    if d <= 29:
                        if (d < 29):
                            print(d + 1, m, y)
                        elif (d == 29):
                            print(d - 28, m + 1, y)
                    else:
                        print("date is not valid")
                else:
                    print("non leap year")
                    if d <= 28:
                        if (d < 28):
                            print(d + 1, m, y)
                        elif (d == 28):
                            print(d - 27, m + 1, y)
                    else:
                        print("date is not valid")
            else:
                if d <= 30:
                    if (d < 30):
                        print(d + 1, m, y)
                    elif (d == 30):
                        print(d - 29, m + 1, y)
                else:
                    print("date is not valid")
        else:
            print("invaid date")
    else:
        print("invalid date")
















