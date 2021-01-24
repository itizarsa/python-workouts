# program to calculate sum of digits of a number

number=int(input("Enter Number "))

sum=0
i=0

while i<number:
    last_num=number%10
    sum=sum+last_num
    number=number//10



print("The sum of digits of a number", sum)