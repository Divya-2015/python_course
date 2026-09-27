"""
1
2 3
4 5 6
7 8 9 10
"""
num = 1
rows = int(input("choose a number")) # => 5
for row in range(rows): # => 0, 1, 2, 3, 4
    for col in range(row + 1):
        print(num, end=" ")
        num = num + 1
    print()