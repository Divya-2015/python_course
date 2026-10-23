print("CLASSROOM POINT CALCULATOR")
team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85

total = team1 + team2 + team3 + team4 + team5
average = total / 5
print("total points :", total)
print("average per team :", average)

stars_per_point = 2
reward_stars = total * stars_per_point
print("total reward stars :", reward_stars)

boxes = reward_stars // 25
leftover = reward_stars % 25

print("full boxes packed :", leftover)
print("leftover stars :", leftover)

last_week = 500

print("better than last week :", total > last_week)
print("same as last week?:", total == last_week)
print("at least as good?:", total >= last_week)

total += 30
print("after bonus points :", total)

total -= 15
print("after missed tasks :", total)

reward_stars = total * stars_per_point
boxes = reward_stars // 25

print("final boxes packed")