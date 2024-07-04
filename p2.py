import vari
import sel
import log
import looprg
import whilop
import str
import lstprg
def qes(a):
    if a==1:
        print(" A person buy shirt at Rs.X and pant and Rs.Y. What is the total purchase cost when n% GST is included.")
        a = float(input("Enter the shirt price  :"))
        b = float(input("Enter the pant price :"))
        c = float(input("Enter the gst percentage :"))
        ans=vari.q1(a,b,c)
        print(ans)
        print()

    elif a==2:
        print("A shirt cost is ‘n’ and GST is ‘m’%. Calculate GST amount and total cost of the shirt.")
        n = float(input("Enter the rupees of shirt:"))
        m = float(input("Enter the percentage of GST:"))
        vari.q2(n,m)

    elif a==3:
        print("Read basic salary of an employee, his DA is 40% of basic salary and HRA is 20% of basic salary. Find his gross salary.")
        ans3=vari.q3()
        print(ans3)

    elif a==4:
        print("A person salary is Rs.’x’ per day, he is fined Rs.’y’ on his absence. Calculate his monthly income when he is present for ‘m’ days and absent for ‘n’ days.")
        vari.q4()

    else:
        print("Giving wrong input please check again")
        print()

def qes1(a):
    if a==1:
        print(" The cost price of an item is x and selling price of an item is y. Find profit amount or loss amount of the item.")
        a = int(input("Enter the cost price of an item:"))
        b = int(input("Enter the selling price of an item:"))
        ans=sel.q1(a,b)
        print(ans)
        print()

    elif a==2:
        print("Read name and age of a person and display whether he is eligible for applying driving license.")
        a = input("Enter the person name:")
        b = int(input("Enter the person age: "))
        sel.q2(a,b)
        print()

    elif a==3:
        print("Create a menu to calculate area of circle or perimeter of the circle.")
        ans1=sel.q3()
        print(ans1)

    elif a==4:
        print("Read 3 angles of the triangle and check whether it is valid or not (valid when sum of 3 angles is 180 degree)")
        sel.q4()
        print()

    else:
        print("Giving wrong input please check again")
        print()

def qes2(a):
    if a==1:
        print("Calculate EB cost for given unit of utilization. Slab rates are as follows")
        a = float(input("Enter the unit: "))
        ans=log.q1(a)
        print("Calculate of eb cost of given unit:",ans)
        print()

    elif a==2:
        print(" Read 3 different numbers in 3 variables and display them in ascending order.")
        a = int(input("Enter the number:"))
        b = int(input("Enter the number:"))
        c = int(input("Enter the number:"))
        log.q2(a,b,c)
        print()

    elif a==3:
        print("A certain grade of steel is graded according to the following conditions")
        ans1=log.q3()
        print(ans1)
        print()

    elif a==4:
        print("Find the next date from the given date")
        log.q4()
        print()

    else:
        print("Giving wrong input please check again")
        print()

def qes3(a):
    if a==1:
        print("Display squares of first n natural numbers.")
        n = int(input("Enter the number:"))
        looprg.q1(n)
        print()

    elif a==2:
        print("Display powers of 2 upto n terms")
        looprg.q2()
        print()

    elif a==3:
        print("Display first n multiples of a given number")
        g = int(input("Enter the given number:"))
        n = int(input("Enter the number of range:"))
        ans2=looprg.q3(g,n)
        print(ans2)
        print()

    elif a==4:
        print("Display the following sequence for the given limit")
        ans3=looprg.q4()
        print(ans3)
        print()

    else:
        print("Giving wrong input please check again")
        print()

def qes5(a):
    if a==1:
        print(" Display first n even numbers")
        n = int(input("how many  even number do you want: "))
        ans=whilop.q1(n)
        print(ans)
        print()

    elif a==2:
        print("Display first n pronic number")
        ans2=whilop.q2()
        print(ans2)
        print()

    elif a==3:
        print("Check the given number is a Fibonacci number")
        n = int(input("Enter the number : "))
        whilop.q3(n)
        print()
    elif a==4:
        print("Find nth prime number")
        whilop.q4()
        print()

    else:
        print("Giving wrong input please check again")
        print()

def qes6(a):
    if a==1:
        print("Find number of consonants and vowels in the given string.")
        n = input("Enter the sentence to number of vowels & c0sonants:")
        ans=str.q1(n)
        print(ans)
        print()

    elif a==2:
        print("Check the given string contains all vowels in it")
        ans2=str.q2()
        print(ans2)
        print()

    elif a==3:
        print("Check whether the string is Symmetrical or not when string length")
        n = input("Enter the words:")
        str.q3(n)
        print()

    elif a==4:
        print("Check the given string contains any numerical character")
        str.q4()
        print()

    else:
        print("Giving wrong input please check again")
        print()

def qes7(a):
    if a==1:
        print("Split the given list into 2 part and add the first part to the end")
        n = int(input("Enter the range:"))
        ans=lstprg.q1(n)
        print(ans)
        print()

    elif a==2:
        print("Display first n odd numbers in descending order.")
        ans1=lstprg.q2()
        print(ans1)
        print()

    elif a==3:
        print("Read ages of n employees and check how many employees in each category")
        n = int(input("Enter the range:"))
        lstprg.q3(n)
        print()

    elif a==4:
        print("Read a divisor n and find remainder for the product of given list elements.")
        lstprg.q4()
        print()

    else:
        print("Giving wrong input please check again")
        print()

