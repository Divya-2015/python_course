"""
OUTPUT:

Welcome to the Lemonade Stand!
Price per cup is 10

Enter number of cups you want: 4

===== RECEIPT =====
Price Per Cup : 10
Cups Sold     : 4
Total Cost    : 40
===================
"""

price = 10

print("Welcome to the Lemonade Stand!")
print(f"Price per cup is {price}")

# User Input
cups = int(input("Enter number of cups you want: "))
def calc_total(cups, price):
    total = cups * price
    return total
total = calc_total(cups, price)
print(total)