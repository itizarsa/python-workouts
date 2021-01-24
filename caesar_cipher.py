####CAESAR CIPHER

def encrypt(word,shift): 
    result = "" 
    for i in range(len(word)): 
        c = word[i] 
  
        if (c.isupper()): 
            result += chr((ord(c) + shift-65) % 26 + 65) 
        else: 
            result += chr((ord(c) + shift-97) % 26 + 97) 
    print("Encrypted word :",result)
  
#check the above function 
word = input("Enter the text to encrypt : ")
shift=int(input("Enter Shift Value : "))
encrypt(word,shift)