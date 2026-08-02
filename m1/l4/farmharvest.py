
field1 = 120
field2 = 85
field3 = 150 
field4 = 95
field5 = 110
total = field1 + field2 +field3 +field4 +field5 
average = total / 5
print("The total is:", total)
print(f"The total is: {total}")
print(f"the average is: {average}")

price_per_kg = 15
earnings = 15 * total
print(f"the earnings are:{earnings}")


last_year = 8000

print(f"Better than last year? {earnings > last_year}")
print(f"Same as last year? {earnings == last_year}")

# Add 30  kgs of bonus harvest to the total
total = total + 30

