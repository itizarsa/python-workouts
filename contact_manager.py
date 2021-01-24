#CONTACT MANAGER

contact = {
"arsa" : 90030,
"arun" : 50090,
"sai" : 87654,
"hell" : 98654
}

print()
name=input("Enter the Name : ")

if name in contact:
    a=contact[name]
    print("Contact Number : ",a)
print()