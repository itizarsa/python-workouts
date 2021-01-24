#program to find all factors of a number

number=int(input("Enter the number "))
factor=[]

for i in range(1, number+1):
    if number%i==0:
        factor.append(i)

print(60*"-")

print("The factors of a given number is", factor)

print(60*"-")

