print("=============")
print("welcome to holiday planner")
print("=============")

print("pick your holiday type")
print("1 - beach holiday")
print("2 - mountain holiday")

choice = int(input("enter 1 or 2: "))

if choice == 1:
    print("step 2: pick your beach activity")
    print("1 - swimming")
    print("2 - sandcastle building")
    print()

    beach_activity = int(input("enter 1 or 2: "))
    print()

    if beach_activity == 1:
        print("you picked : swimming")
        print("best time : morning")
        print("remember : carry sunscreen and water")
    else:
        print("you picked sandcastle : building")
        print("best time : evening")
        print("remember : carry a bucket and spade")



   

