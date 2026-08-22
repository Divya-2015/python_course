import keyword


person_name = input("what is your name?")
goal_name = input("what is your personal goal?")
target_month = input("what is your target month?")
daily_minutes = 20


print("\nname:", person_name)
print("goal:", goal_name)
print("target month:",target_month)
print("daily practice:", daily_minutes, "minutes")


print("\nmy personal goal plan\n")


print("goal status:", end="")
print("not started")

print("progress reminder:",end="-")
print("practice every day!!")

print(
    "\n",
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "mintes every single day."
)

print("\npython keywordsare...\n")
print(keyword.kwlist)


