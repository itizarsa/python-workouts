# program to find first and last digit of a number

n=int(input("Enter Number "))
a=[]

i=0
c=0

while i<n:
 x=n%10
 n=n//10
 a.append(x)
 c=c+1


print("The First Digit is ",a[c-1])
print("The Last Digit is ",a[0])
 