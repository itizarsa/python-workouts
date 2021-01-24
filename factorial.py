# program to calculate factorial of a number

number=int(input("Enter the number "))
factorial=1

if number<0:
    Print("Factorial Value doesn't exist for Negative values")
elif number==0:
    print("Factorial value for 0 is 1")
else:
    for i in range(1, number+1):
        factorial=factorial*i

print("The factorial of the given number is", factorial)