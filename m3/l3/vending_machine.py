"""
OUTPUT:
Snack Price: 25
Enter the amount paid: 32
Change Returned: 7
Thank you!
"""

# Snack Vending Machine

# Function to calculate change
def calculate_change(paid, price):
    change = paid - price
    return change

# Main program
price = 25
print("snack price :" , price )
amount = int(input("enter the money"))
change = calculate_change(amount, price)
print(change)