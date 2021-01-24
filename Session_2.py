####SUM OF VALUES FROM LIST BY GIVEN INDEX

l1=[]
length=int(input("Enter Length : "))

for i in range(length):
    value=int(input("Enter Values : "))
    l1.append(value)
key=int(input("Enter the Key : "))
sum=0
for i in range(key+1):
    sum=l1[i] + sum

print(sum)


####LIST SLICING

a=[1,2,3,4,5,6,7,8]

print(a[3:4])
print(a[1:2:3])
print(a[::])
print(a[:])
print(a[::4:])
print(a[1::6])
print(a[0:0:0])
print(a[5:-1:-1:7])
print(a[4:6:-1])
print(a[3:2:1:0])
print(a[:7:])
print(a[1:])
print(a[:7])
print(a[6:1:1])
print(a[0:0])
print(a(int[2.75]):3.7)


