#program to calculate product of digits of a number

number=int(input("Enter Number "))
product=1
i=0

while i<number:
    last_num=number%10
    product=product*last_num
    number=number//10

print("The Product of digits are", product)