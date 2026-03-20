morning_points = 0
both_points = 0
night_points = 0


answer1 = input("Do you prefer A coffee, B energy drinks, or C both")
if answer1 == "A" :
    morning_points += 1
elif answer1 == "B" :
    night_points +=1
elif answer1 == "C" :
    both_points +=1

answer2 = input("Do you like A eggs, B pasta, or C you like them equally")
if answer2 == "A" :
    morning_points += 1
elif answer2 == "B" :
    night_points +=1
elif answer2 == "C" :
    both_points +=1


answer3 = input ("Do you A wake up easily in the morning, B is it hard to get out of bed, or C you are right in the middle")
if answer3 == "A" :
    morning_points += 1
elif answer3 == "B" :
    night_points +=1
elif answer3 == "C" :
    both_points +=1

answer4 = input ("Do you like to A wake up early, B stay up late, or C both")
if answer4 == "A" :
    morning_points += 1
elif answer4 == "B" :
    night_points +=1
elif answer4 == "C" :
    both_points +=1

answer5 = input ("Are you A happy in the morning, B grumpy, or C it varies")
if answer5 == "A" :
    morning_points += 1
elif answer5 == "B" :
    night_points +=1
elif answer5 == "C" :
    both_points +=1


print(f"You're score is {morning_points} morning points, {night_points} night points, and {both_points} points where you like them equally.")

if morning_points > night_points and both_points :
    print("You enjoy the mornings.")

if night_points > morning_points and both_points :
    print("You enjoy the nights.")

if both_points > night_points and morning_points :
    print("You enjoy morning and night equally.")