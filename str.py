def q1(n):
    print("With argument with return")
    li=[]
    li1=[]
    c = 0
    vow = "aeiouAEIOU"
    for i in n:
        if i in vow:
            c = c + 1
    li.append(c)
    s = 0
    con = "bcdfghklmnpqrstvwxyzjBCDFGHJKLMNPQRSTVWXYZ"
    for j in n:
        if j in con:
            s = s + 1
    li1.append(s)
    return "vowels = ", li, "consonants", li1

def q2():
    n = input("Enter the string:")
    print("[no Argument with return]")
    vo = "aeiou"
    a = n.lower()
    ns = ""
    for i in vo:
        if i in a:
            ns = ns + i + ""
    if ns == vo:
        return "its contains all vowels "
    else:
        return "its not contains all vowels"

def q3(n):
    print("[With argument no return ]")
    f = 0
    x = len(n)
    if x % 2 == 0:
        mid = x // 2
        s = 0
        s1 = mid
        while s < s1 and s1 < x:
            if n[s] == n[s1]:
                s = s + 1
                s1 = s1 + 1
            else:
                f = 1
            break
        if f == 0:
            print("the word is symmetrial")
        else:
            print("the word is not symmetrial")
    else:
        print("its odd sting")


def q4():
    n = input("Enter the string:")
    print("no argument no return")
    c = 0
    s = "1234567890"
    for i in n:
        if i in s:
            c = c + 1

    if c >= 1:
        print("its have numerical number")
    else:
        print("its not have numerical number")