#program to enter a number and print its reverse

number=int(input("Enter Number "))
reverse=0
i=0

while i<number:
    last_num=number%10
    reverse=(reverse*10)+last_num

    number=number//10

print("The Reverse of numbers are", reverse)