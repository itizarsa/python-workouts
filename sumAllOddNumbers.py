#program to find sum of all odd numbers between 1 to n.

s=1
e=int(input("Enter the Ending Value "))

sum=0

for i in range(s,e+1):
 if i%2==0:
     b=i

 else:
     sum=i+sum
 
print("The Sum of all odd numbers between 1 to ", e, "is", sum)