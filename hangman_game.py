#HANGMAN GAME

import random

words=["guvii", "waterr", "sellf", "hello"]
random_word=random.choice(words)
checking_word=[]
life=12
found_letter_count=0
#print(random_word)

print(150*"*")

print(len(random_word), "Letter Word")

while life>0:
    for i in range(len(random_word)):
        checking_word.append('-')
    while found_letter_count<len(random_word) and life>0:
        guess_word=input()
        if guess_word in random_word:
            if guess_word not in checking_word:
                for i in range(len(random_word)):
                    if random_word[i]==guess_word:
                        checking_word[i]=guess_word
                        found_letter_count= found_letter_count + 1
                    
            else:
                life= life - 1
        else:
            life=life-1

        print("You Have", life, "Chances")
        print(" ".join(checking_word))
        
    break

print(20*"*")

if life>0:
    print("You Won")
else:
    print("You Lose")

print(20*"*")
