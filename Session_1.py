####RANGE METHOD


for i in range(1,20,2):
    print(i, end=" ")
print()


for i in range(2,20,2):
    print(i, end=" ")
print()


for i in range(1,20,2):
    print(i*i, end=" ")
print()


####LIST ERROR

namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist.append('pb122')
if 'pb122' in namelist:
    print("Now I know pb122!")


####VARIABLE ERROR

print("Hello!")
name = input("Enter your name: ")
print("Your name is " + name + ".")


####EXTEND METHOD ERROR

namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist.extend('theelous3')

if input("Enter your name: ") in namelist:
    print("I know you!")
else:
    print("I don't know you.")


####GET VALUES FROM DICT

abc = {
'__Myst__': 'cats',
'Arun': 'dogs',
'horusr': 'cats',
'caisa64': 'cats and dogs'
}

print()
for i , b in abc.items():
    print(i, ":", b)

print()


####FUNCTION EXPLANATION

a1=10
def abc(s):
    a2=20

    return a2
    print(a1)
    
b=abc("hi")

print(b)


####NESTED FOR LOOP

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            for l in range(3,0):
                print(l)
            print(k)
        print(j)
    print(i)