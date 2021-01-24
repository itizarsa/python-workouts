#program to find frequency of each digit in a given integer

number=int(input("Enter the Number "))
find_freq=int(input("Enter the Digit "))

count=0
i=0

while i<number:
    last_num=number%10
    number=number//10
    if last_num==find_freq :
        count=count+1

print("The Frequency of the entered digit in the Integer is", count)