import vari
import p2
def varipro(n):
    if n==1:
        print("{----------USER are selected variable programs----------}")
        print("1. A person buy shirt at Rs.X and pant and Rs.Y. What is the total purchase cost when n% GST is included.")
        print("2. A shirt cost is ‘n’ and GST is ‘m’%. Calculate GST amount and total cost of the shirt.")
        print("3. Read basic salary of an employee, his DA is 40% of basic salary and HRA is 20% of basic salary. Find his gross salary.")
        print("4. A person salary is Rs.’x’ per day, he is fined Rs.’y’ on his absence. Calculate his monthly income when he is present for ‘m’ days and absent for ‘n’ days.")
        a= int(input("Enter the choosable option:"))
        p2.qes(a)

def selpro(n):
    if n==2:
        print("{----------USER are selected selection programs----------}")
        print("1. The cost price of an item is x and selling price of an item is y. Find profit amount or loss amount of the item.")
        print("2. Read name and age of a person and display whether he is eligible for applying driving license.")
        print("3. Create a menu to calculate area of circle or perimeter of the circle.")
        print("4. Read 3 angles of the triangle and check whether it is valid or not (valid when sum of 3 angles is 180 degree)")
        a=int(input("Enter the choosable option:"))
        p2.qes1(a)


def logpro(n):
    if n==3:
        print("{----------USER are selected logical programs----------}")
        print("1. Calculate EB cost for given unit of utilization. Slab rates are as follows.")
        print("2. Read 3 different numbers in 3 variables and display them in ascending order.")
        print("3. A certain grade of steel is graded according to the following conditions")
        print("4. Find the next date from the given date")
        a = int(input("Enter the choosable option:"))
        p2.qes2(a)

def looprg(n):
    if n==4:
        print("{----------USER are selected looping programs----------}")
        print("1. Display squares of first n natural numbers.")
        print("2. Display powers of 2 upto n terms")
        print("3. Display first n multiples of a given number.")
        print("4. Display the following sequence for the given limit")
        a=int(input("Enter the choosable option:"))
        p2.qes3(a)

def whlp(n):
    if n==5:
        print("{----------USER are selected While loop programs----------}")
        print("1.. Display first n even numbers")
        print("2. Display first n pronic numbers")
        print("3. Check the given number is a Fibonacci number.")
        print("4. Find nth prime number")
        a=int(input("Enter the choosable option:"))
        p2.qes5(a)

def str(n):
    if n==6:
        print("{----------USER are selected string programs----------}")
        print("1. Find number of consonants and vowels in the given string.")
        print("2. Check the given string contains all vowels in it")
        print("3. Check whether the string is Symmetrical or not when string length is even")
        print("4. Check the given string contains any numerical character.")
        a = int(input("Enter the choosable option:"))
        p2.qes6(a)

def lstpro(n):
    if n==7:
        print("{----------USER are selected string programs----------}")
        print("1. Split the given list into 2 part and add the first part to the end")
        print("2. Display first n odd numbers in descending order.")
        print("3. Read ages of n employees and check how many employees in each category.")
        print("4. .Read a divisor n and find remainder for the product of given list elements.")
        a = int(input("Enter the choosable option:"))
        p2.qes7(a)





