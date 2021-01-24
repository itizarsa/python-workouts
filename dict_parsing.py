#DICT & LIST PROBLEMS (DICT_PARSING)

####Sort the list 

l1 = [3, 1, 4, 2, 5]
l1.sort()
print(l1)


####print the squares of all the number in the list 

l2 = [3, 1, 4, 2, 5]
for i in l2:
    print(i*i)


####print all the elements in the list 

l3 = [
    (105, "d"),
    (21, "z"),
    (0, "v")
]

for x in l3:
    for y in x:
        print(y,end=" ")


####print the hex codes of all colors
####print the hex value of green
####Print all the value in the list

l = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]

print()
print("Hex Codes of all Colours : ")

for i in l:
    print(i["value"])

print()
print("Hex Codes of green Colour : ")
for i in l:
    if i["color"]=="green":
        print(i["value"])

print()
print("All Values in list : ")
for x in l:
    for y in x:
        a=y
        print(x[y], end="  ")


####Print the languages that are inferior to Python

py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}

v1=py["inferior"]
for y in v1:
    print(y)


####Print my Bill

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}

x,y=0,0

for a in my_purchase:
    for b in prices:
        if a==b:
            x=my_purchase[a]*prices[b]
            y+=x
            print("The price of", my_purchase[a], a, "is", x)
print("The total bill is", y)


####print the items
####print the roles

junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}

for x in junk:
    for y in junk[x]:
        for z in junk[x][y]:
            print()
            if z=="role":
                print(z, "of", y, "is", junk[x][y][z])
                
            
            elif z=="items":
                print(z, "of", y, "is")
                for i in junk[x][y][z]:
                    print(i, end=" ")
                print()
                print()