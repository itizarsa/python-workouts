####Create a file & Append values

a=int(input())
b=int(input())
c=a+b
d=open("3.txt","a")
d.write("The addition of %d and %d is %d\r\n"%(a,b,c))
d.close()


####Read the value from File & Print if it has read permission

a=open("3.txt","r")
if (a.mode=="r"):
    c=a.read()
    print(c)
a.close()


####Add Entered details to Files

d={}
a=open("student.txt","a")
print("Enter 1 to Start")
print("Enter 0 to Quit")
b=int(input("Enter Value"))
if b==1:
    i=1
    while i>0:
        student=int(input("Enter Student No. : "))
        print("Enter Marks for Student", student, end=" : ")
        marks=int(input())
        d[student]=marks
        print("Enter 1 to Start")
        print("Enter 0 to Quit")
        i=int(input("Enter Value"))
elif b>1:
    print("Enter 1 to Start")
    print("Enter 0 to Quit")
    b=int(input("Enter Value"))

else:
    print("Program Finished")

#a=open("student.txt","r")
#b=a.read()
#c=eval(b)
#for k,v in c:
#     print(k,v)
a.write("%s"%(d))
a.close()
