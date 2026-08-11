day = input("What day is it today?").lower()
weather = input("How is the weather today?")
if day == "saturday" or day == "sunday":
    print("it is the weekend have fun")
elif day == "friday":
    print("last day of the week")
else:
    print("a regular day")


if weather == "rainy" or weather == "cloudy":
    print("carry an umbrella")
else:
    print("you do not need an umbrella today")

