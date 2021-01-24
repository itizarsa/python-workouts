#CALCULATOR

def add(a,b):
    return a+b
def sub(a,b):
    return b-a
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


operation=input("Enter the Operation\n '1' -> Add\n '2' -> Sub\n '3' -> Multiply\n '4' -> Division\n")

if operation=="1":
    value1=int(input("Enter 1st Number : "))
    value2=int(input("Enter 2nd Number : "))
    print(add(value1,value2))

if operation=="2":
    value1=int(input("Enter 1st Number : "))
    value2=int(input("Enter 2nd Number : "))
    print(sub(value1,value2))

if operation=="3":
    value1=int(input("Enter 1st Number : "))
    value2=int(input("Enter 2nd Number : "))
    print(mul(value1,value2))

if operation=="4":
    value1=int(input("Enter 1st Number : "))
    value2=int(input("Enter 2nd Number : "))
    print(div(value1,value2))
