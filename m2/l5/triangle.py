"""
*
* *
* * *
* * * *
"""

rows = int(input("choose a number")) # => 5
for row in range(rows): # => 0, 1, 2, 3, 4
    for col in range(row + 1):
        print("*", end=" ")
    print()