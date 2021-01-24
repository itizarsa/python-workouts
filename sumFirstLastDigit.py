# program to find sum of first and last digit of a number

number=int(input("Enter the Number "))
find_number=[]

i=0
position=0

while i<number:
    last_num=number%10
    number=number//10
    find_number.append(last_num)
    position=position+1

sum=(find_number[position-1])+(find_number[0])
print("The Sum of First and Last digit of a number is", sum )

