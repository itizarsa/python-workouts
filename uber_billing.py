#UBER

starting=int(input("Enter the Starting Place : "))
ending=int(input("Enter the Ending Place : "))
distance = ending-starting

macro_car_list=["1","2","3","4"]
mini_car_list=[1,2,3,4]
prime_car_list=[1,2,3,4]
luxury_car_list=[1,2,3,4]

print("Enter Q to exit")

select_cat=input("Enter the Car Category :\n'1' -> Macro\n'2' -> Mini\n'3' -> Prime\n'4' -> Luxury\n")

if select_cat=="q" or select_cat=="Q":
    exit()

if select_cat=="1":
    while len(macro_car_list)>0:
        print("Enter Q to exit")
        print("Available cars : ", macro_car_list)
        choose_car=(input("Choose the Car : "))

        if choose_car=="q" or choose_car=="Q":
            exit()

        elif choose_car in macro_car_list:
            macro_car_list.remove(choose_car)
            print("Car", choose_car, "Booked")
            print("Distance Travelled : ",distance)
            print("Bill : ",distance*10)

        elif choose_car not in macro_car_list:
            print("Select Available Cars")
            print("Available cars : ", macro_car_list)
            choose_car=(input("Choose the Car : "))


    if len(macro_car_list)==0:
        print("All Cars are booked in this Category")
        print("Choose other Category")
        select_cat=input("Enter the Car Category :\n'1' -> Macro\n'2' -> Mini\n'3' -> Prime\n'4' -> Luxury\n")

elif select_cat=="2":
    while len(mini_car_list)>0:
        print("Enter Q to exit")
        print("Available cars : ", mini_car_list)
        choose_car=int(input())

        if choose_car=="q" or choose_car=="Q":
            exit()

        elif choose_car in mini_car_list:   
            mini_car_list.remove(choose_car)
            print("Car", choose_car, "Booked")
            print("Distance Travelled : ",distance)
            print("Bill : ",distance*20)

        elif choose_car not in mini_car_list:
            print("Select Available Cars")
            print("Available cars : ", mini_car_list)
            choose_car=(input("Choose the Car : "))

    if len(mini_car_list)==0:
        print("All Cars are booked in this Category")
        print("Choose other Category")
        select_cat=input("Enter the Car Category :\n'1' -> Macro\n'2' -> Mini\n'3' -> Prime\n'4' -> Luxury\n")

elif select_cat=="3":
    while len(prime_car_list)>0:
        print("Enter Q to exit")
        print("Available cars : ", prime_car_list)
        choose_car=int(input())

        if choose_car=="q" or choose_car=="Q":
            exit()

        elif choose_car in prime_car_list:    
            prime_car_list.remove(choose_car)
            print("Car", choose_car, "Booked")
            print("Distance Travelled : ",distance)
            print("Bill : ",distance*30)
        
        elif choose_car not in prime_car_list:
            print("Select Available Cars")
            print("Available cars : ", prime_car_list)
            choose_car=(input("Choose the Car : "))

    if len(prime_car_list)==0:
        print("All Cars are booked in this Category")
        print("Choose other Category")
        select_cat=input("Enter the Car Category :\n'1' -> Macro\n'2' -> Mini\n'3' -> Prime\n'4' -> Luxury\n")

elif select_cat=="4":
    while len(luxury_car_list)>0:
        print("Enter Q to exit")
        print("Available cars : ", luxury_car_list)
        choose_car=int(input())

        if choose_car=="q" or choose_car=="Q":
            exit()

        elif choose_car in luxury_car_list:
            luxury_car_list.remove(choose_car)
            print("Car", choose_car, "Booked")
            print("Distance Travelled : ",distance)
            print("Bill : ",distance*40)

        elif choose_car not in luxury_car_list:
            print("Select Available Cars")
            print("Available cars : ", luxury_car_list)
            choose_car=(input("Choose the Car : "))

    if len(luxury_car_list)==0:
        print("All Cars are booked in this Category")
        print("Choose other Category")
        select_cat=input("Enter the Car Category :\n'1' -> Macro\n'2' -> Mini\n'3' -> Prime\n'4' -> Luxury\n")

else:
    print("Invalid Option")