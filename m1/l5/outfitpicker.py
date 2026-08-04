"""
Activity: Weather Outfit Picker

Instructions:
1. Ask the user to enter today's temperature.
2. If the temperature is below 20°C, suggest wearing a jacket.
3. Otherwise, suggest wearing a t-shirt.
4. Ask if it is raining.
5. If it is raining, remind the user to carry an umbrella.
6. Ask if there are puddles on the ground.
7. If there are puddles, suggest wearing boots.
8. Otherwise, suggest wearing sneakers.
9. Display a summary of the outfit choices.
"""

# Ask for today's temperature
temp = int(input("what is todays temperature? "))


# Check if it is cold and decide the outfit 
if temp < 20:
    outfit = "jacket"
else:
    outfit = "t-shirt" 


# Check if it is raining and decide on the umbrella
raining = input ("Is it raining? yes/no: ")
if raining == "yes":
    print("Carry an umbrella")
else:
    print("An umbrella is not needed today")


# Check for puddles and decide the shoes
puddles = input ("Is there puddles today? yes/no: ")
if puddles == "yes":
    shoes = "boots" 
else:
    shoes = "any shoes"



# Display the final summary
print("\n===== WEATHER OUTFIT SUMMARY =====")
print(f"Temperature: {temp}")
print(f"outfit: {outfit}")
print(f"raining: {raining}")
print(f"shoes: {shoes}")