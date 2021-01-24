#NUMBER GUESSING GAME

import random

random_guess=random.randint(0,11)
print(random_guess)
i=5
while i>0:
    your_guess=int(input("Enter the Number "))
    if random_guess==your_guess:
        break
    else:
        i-=1
    
    print("You have", i, "Chances")
if i>0:
    print("You won")
else:
    print("You Lose")