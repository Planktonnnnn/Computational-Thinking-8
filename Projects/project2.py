morning_points = 0
night_points = 0
both_points = 0


answer1 = input("Do you prefer A short sleeves, B long sleeves, or C both?")
if answer1 == "A":
		morning_points += 1
elif answer1 == "B":
    night_points += 1
elif answer1 == "C":
    both_points += 1
