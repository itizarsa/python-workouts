# program to find sum of all natural numbers between 1 to n

s=1
e=int(input("Enter the Ending Value "))

sum=0

for i in range(s,e+1):
    sum=i+sum

print("The Sum of all Natural Numbers Between 1 to ", e, "is", sum)