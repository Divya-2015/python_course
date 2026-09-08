"""
OUTPUT:
You have 4 chores to finish today!

Did you finish Make your bed? (yes/no): yes
Great job!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): no
Finish it first!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): no
Finish it first!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): yes
Great job!
Chores remaining: 2

Did you finish Take out the trash? (yes/no): yes
Great job!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): yes
Great job!
Chores remaining: 0

All chores are complete!
"""

# List of chores to complete
chores = ["Make your bed", "Feed the pet", "Take out the trash", "Wash the dishes"]
# chores[3] => 0, 1, 2, 3

remaining = len(chores)
index = 0

print(remaining, "chores to finish today!\n")
while remaining > 0:
    answer = input(f"did you finish your chore: {chores[index]}? (yes/no): ")

    if answer == "yes":
        index = index + 1
        remaining = remaining - 1
        print("well done")
    else:
        print("please finish it today")

    print(remaining, "chores to finish today!\n")
print("all chores are completed")