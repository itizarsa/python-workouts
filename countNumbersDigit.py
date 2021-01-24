#program to count number of digits in a number

n=int(input("Enter Number "))

c=0
i=0

while i<n:
 a=n%10
 n=n//10
 c=c+1

print(c)

