# program to print multiplication table of any number

t=int(input("Enter Table Number "))
l=int(input("Enter Table Length "))

for i in range(1,l+1):
 print(i, "*", t, "=", i*t)