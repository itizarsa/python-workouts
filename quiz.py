#QUIZ GAME

quiz1="What is OS ?"
quiz2="What is python"
quiz3="Is python case-sensitive ?"
quiz4="How do you declare variable in python"
quiz5="When python was released ?"

choice1=["1 -> Operation Setup", "2 -> Operating System", "3 -> Opening Show", "4 -> Open Source"]
choice2=["1 -> Game", "2 -> Snake", "3 -> Programming Language", "4 -> OS"]
choice3=["1 -> Yes", "2 -> No", "3 -> Doesn't Matter", "4 -> None of the Above"]
choice4=["1 -> var a=2", "2 -> var 2", "3 -> a=2", "4 -> None of the above"]
choice5=["1 -> 2005", "2 -> 1991", "3 -> 1990", "4 -> 2011"]

ans1=choice1[1]
ans2=choice2[2]
ans3=choice3[0]
ans4=choice4[2]
ans5=choice5[1]

points=0

print(60*"-")
print()
print("Welcome to Quiz Game")
print()

print(quiz1)
print(choice1)
q1=input("Enter the choice : ")
if q1=="2":
    print("Correct Answer")
    points+=1
else:
    print("Wrong Answer. The Correct Answer is", ans1)
print()


print(quiz2)
print(choice2)
q2=input("Enter the choice : ")
if q2=="3":
    print("Correct answer")
    points+=1
else:
    print("Wrong Answer. The Correct Answer is", ans2)
print()


print(quiz3)
print(choice3)
q3=input("Enter the choice : ")
if q3=="1":
    print("Correct answer")
    points+=1
else:
    print("Wrong Answer. The Correct Answer is", ans3)
print()


print(quiz4)
print(choice4)
q4=input("Enter the choice : ")
if q4=="3":
    print("Correct answer")
    points+=1
else:
    print("Wrong Answer. The Correct Answer is", ans4)
print()


print(quiz5)
print(choice5)
q5=input("Enter the choice : ")
if q5=="2":
    print("Correct answer")
    points+=1
else:
    print("Wrong Answer. The Correct Answer is", ans5)
print()

print("Your Points are", points)
print()
print(60*"-")