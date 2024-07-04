def q1(a,b):
    print("[With argument with return]")
    if a < b:
        return "it is profit"
    elif a > b:
        return " it is loss"
    else:
        return "not profit not loss"

def q2(a,b):
    print("[With argument no return]")
    if b > 18 and b>=18:
        print(a, "is eligeble for driving license")
    else:
        print(a, "is not eligible for driving license")

def q3():
    ch = int(input("Enter the 1 to area of circle or 2 2 to perimeter of a circle:"))
    print("[no argument with return]")
    if ch == 1:
        d = float(input("Enter the Diameter:"))
        r = d / 2
        return "Area of cicle value is", 3.14 * (r ** 2)
    elif ch == 2:
        d = float(input("enter the Diameter:"))
        r = d / 2
        return "Perimeter of circle is", 2 * 3.14 * r

    else:
        return "Invaid number choose 1 or 2"

def q4():
    a = int(input("enter the 1st angle:"))
    b = int(input("enter the 2nd angle"))
    c = int(input("enter the 3rd angle"))
    print("[No argument no return]")

    if (a + b + c == 180):
        print("it is valid 180 triangle")
    else:
        print("it is not valid 180 triangle")


