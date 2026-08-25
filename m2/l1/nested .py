print("1 - car" )
print("2 - bike")
choice = int(input("pick your vehicle: "))
if choice == 1:
    print("you have picked car")
    print("1 - suv")
    print("2 - sedan")
    cat = int(input("pick your vehicle type"))
    if cat == 1:
        print("you haved picked suv")
    else:
        print("you have picked sedan")

else:
    print("you have picked bike")
    print("1 - mountain")
    print("2 - sports")
    cat = int(input("pick your vehicle type"))
    if cat == 1:
        print("you haved picked mountain")
    else:
        print("you have picked sports")