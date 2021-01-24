import random


def register():

    credentials={}
    storage =  open("bank.txt","a+")
    storage.seek(0)
    get_value = storage.read()
    data = [ ]

    if len(get_value) == 0:

        name=input("Enter the Name : ")
        while (not(name.isalpha())):
            print("Enter Only Alphabets")
            name=input("Enter the Name : ")
        data.append(name)
    

        email=input("Enter Email : ")
        while (not(email.endswith("@gmail.com"))):
            print("Enter Valid Email")
            email=input("Enter Email : ")
        data.append(email)

        contact_no=input("Enter Contact Number : ")
        while (not(contact_no.isdigit() or len(contact_no)==10)):
            print("Enter Only Number")
            contact_no=input("Enter Contact Number : ")
        data.append(contact_no)

        print("Maximu length of Password is 8 & Minimum length of 4")
        password=input("Enter Password : ")
        while (not(len(password)>=4 and len(password)<=8)):
            print("Maximu length of Password is 8 & Minimum length of 4")
            password=input("Enter Password : ")
        data.append(password)

        print("Minimum Amount 10000 & Maximum Amount 50000  |  Enter Only Numbers")
        transaction=[]
        initial_amount=input("Enter the Initial Deposit Amount : ")
        while not(initial_amount.isdigit() and (int(initial_amount)>=10000 and int(initial_amount)<=50000)):
            print("Minimum Amount 10000 & Maximum Amount 50000 |  Enter Only Numbers")
            amount=input("Enter the  Initial Deposit Amount : ")
        transaction.append(initial_amount)
        data.append(transaction)


        while True:
            unique_id=random.randint(99,1000)
            if unique_id not in credentials:
                print("Your Unique ID is : ", unique_id)
                break

        credentials[unique_id]=data
        storage.write("%s"%(credentials))
    
        print("Registered Succesfully")

    else:
        get_eval=eval(get_value)

        name=input("Enter the Name : ")
        while (not(name.isalpha())):
            print("Enter Only Alphabets")
            name=input("Enter the Name : ")
        data.append(name)
    

        email=input("Enter Email : ")
        while (not(email.endswith("@gmail.com"))):
            print("Enter Valid Email")
            email=input("Enter Email : ")
        data.append(email)

        contact_no=input("Enter Contact Number : ")
        while (not(contact_no.isdigit() or len(contact_no)==10)):
            print("Enter Only Number")
            contact_no=input("Enter Contact Number : ")
        data.append(contact_no)

        print("Maximu length of Password is 8 & Minimum length of 4")
        password=input("Enter Password : ")
        while (not(len(password)>=4 and len(password)<=8)):
            print("Maximu length of Password is 8 & Minimum length of 4")
            password=input("Enter Password : ")
        data.append(password)

        print("Minimum Amount 10000 & Maximum Amount 50000  |  Enter Only Numbers")
        transaction=[]
        initial_amount=input("Enter the Initial Deposit Amount : ")
        while not(initial_amount.isdigit() and (int(initial_amount)>=10000 and int(initial_amount)<=50000)):
            print("Minimum Amount 10000 & Maximum Amount 50000 |  Enter Only Numbers")
            initial_amount=input("Enter the  Initial Deposit Amount : ")
        initial_amount=int(initial_amount)
        transaction.append(initial_amount)
        data.append(transaction)


        while True:
            unique_id=random.randint(99,1000)
            if unique_id not in get_eval:
                print("Your Unique ID is : ", unique_id)
                break

        storage.seek(0)
        get_eval2 = eval(storage.read())
        get_eval2.update({unique_id:data})
        credentials=get_eval2
    
    storage = open("bank.txt","w+")
    storage.seek(0)
    storage.write("%s"%(credentials))
    storage.close()      

def login():

    storage=open("bank.txt","r")
    data=storage.read()
    data1=eval(data)
    while True:
        unique_id=input("Enter Unique ID : ")
        

        while not unique_id.isdigit():
            print("Enter Only Numbers ")
            unique_id=input("Enter Unique ID : ")
            
        unique_id1=int(unique_id)
        
        if unique_id1 in data1:
            
            password=input("Enter Password : ") 
            key=data1[unique_id1][3]
            while not(password==key):
                print("Enter Correct Password")
                password=input("Enter Password : ")
            break
        else:
            print("Enter Correct Details | Only Numbers")
        
    

    print("Login Succesfully")
    return unique_id1

def check_balance(a):

    storage=open("bank.txt","r")
    data=storage.read()
    data1=eval(data)

    x=data1[a][-1]
    print("Balance",x[-1])

def deposit(a):

    storage=open("bank.txt","a+")
    storage.seek(0)
    data=storage.read()
    data1=eval(data)

    x=data1[a][-1]
    y=x[-1]
    y=int(y)
    
    while True:
        z=input("Enter the Amount to Deposit : ")
        if z.isdigit():
            z=int(z)
            if z>=5000 and z<=50000:
                y=y+z
                print("The deposit of", z, "is Succesful")
                break
            else:
                print("Minimum 5000 & Maximum 50000 are Allowed")
        else:
            print("Enter only Numbers")
    x.append(y)
    storage = open("bank.txt","w+")
    storage.seek(0)
    storage.write("%s"%(data1))
    storage.close() 


def withdraw(a):
    storage=open("bank.txt","a+")
    storage.seek(0)
    data=storage.read()
    data1=eval(data)

    x=data1[a][-1]
    y=x[-1]
    y=int(y)

    while True:
        z=input("Enter the Amount to Withdraw : ")
        if z.isdigit():
            z=int(z)
            if y-z>=10000 and z<=50000:
                y=y-z
                print("The withdrawal of", z, "is Succesful")
                break
            else:
                print("Minimum Balance 10000 is required")
        else:
            print("Enter only Numbers")
    x.append(y)
    storage = open("bank.txt","w+")
    storage.seek(0)
    storage.write("%s"%(data1))
    storage.close() 

def account_details(a):
    storage=open("bank.txt","r")
    data=storage.read()
    data1=eval(data)

    id1=a
    name=data1[a][0]
    email=data1[a][1]
    contact=data1[a][2]

    print("Unique ID : ",id1)
    print("Name : ",name)
    print("Email : ",email)
    print("Contact No : ",contact)




print(150*"*")
print()
print("Welcome to Bank")
print()



while True:
    print(" '1' Register\n '2' Login\n '3' Quit")
    option=input("Enter the Operation : ")
    option.upper()

    while not(option== "1" or option=="REGISTER" or option=="2" or option=="LOGIN" or option=="3" or option=="QUIT"):
        print("Enter the Correct Operation")
        option=input("Enter the Operation : ")
        option.upper()
    
    if option=="1" or option=="REGISTER":
        register()
        

    elif option=="2" or option=="LOGIN":
        a = login()
        while True:
            print(" '1' Check Balance\n '2' Deposit\n '3' Withdraw\n '4' Account Details\n '5' Quit")
            operation=input("Enter the Operation : ")
            operation.upper()


            if operation=="1" or operation=="CHECKBALANCE" or operation=="CHECK BALANCE":
                check_balance(a)
                


            elif operation=="2" or operation=="DEPOSIT":
                deposit(a)
                


            elif operation=="3" or operation=="WITHDRAW":
                withdraw(a)
        

            elif operation=="4" or operation=="ACCOUNT DETAILS" or operation=="ACCOUNTDETAILS":
                account_details(a)


            elif operation=="5" or operation=="QUIT":
                print("Logout Succesfully")
                break

            else:
                print("Enter Correct Option")



    elif option=="3" or option=="QUIT":
        print("Thanks for Your Interest")
        exit()
