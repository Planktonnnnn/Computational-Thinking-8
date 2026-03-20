morning_points = 0
night_points = 0
both_points = 0


answer1 = input("Do you prefer A energy drinks, B coffee, or C you like both of them equally?")
if answer1 == "A":
	morning_points += 1
elif answer1 == "B":
    night_points += 1
elif answer1 == "C":
    both_points += 1


answer2 = input("Do you prefer A morning, B nights, or C both?")
if answer2 == "A":
	morning_points += 1
elif answer2 == "B":
    night_points += 1
elif answer2 == "C":
    both_points += 1
