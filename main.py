import p1
while True:
     print()
     print("1.to variable programs")
     print("2.to Selection programs")
     print("3.to Logical programs")
     print("4.to looping programs")
     print("5.to while loop programs")
     print("6.to string programs")
     print("7.to list programs")
     print("8.to Exit")
     print()
     n=int(input("Enter the option to choose:"))
     if n==8:
          print("<>This program as been exit<>")
          break
     p1.varipro(n)
     p1.selpro(n)
     p1.logpro(n)
     p1.looprg(n)
     p1.whlp(n)
     p1.str(n)
     p1.lstpro(n)