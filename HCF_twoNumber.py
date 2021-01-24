# program to find HCF (GCD) of two numbers

number_one=int(input("Enter the 1st Number "))
number_two=int(input("Enter the 2nd Number "))

if number_one > number_two:
    smaller=number_two
else:
    smaller=number_one

for i in range(1, smaller+1):
    if (number_one%i==0) and (number_two%i==0):
        hcf=i

print("The HCF of the two numbers are", hcf)