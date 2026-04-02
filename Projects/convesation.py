from utils import *
player_name = input("What is your name?    ")

set_background("pond")

s1 = create_sprite("cardinal2", -200, 0)
s2 = create_sprite("fish", 200, 0)

s1.color("white")
s2.color("dark red")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("In a pond?!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()


s1.clear()
s2.write("Nope!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
s1.write("We need to find them!")
window.update()
time.sleep(1)

s1.clear()
s2.write("Thats too much work")
window.update()
time.sleep(1)

s2.clear()
s1.write("That's so selfish!")
window.update()
time.sleep(1)

s1.clear()
s2.write("It could be dangerous!")
window.update()
time.sleep(1)

s2.clear()
s1.write("That's exactly why we have to find them!")
window.update()
time.sleep(1)

s1.clear()
s2.write("Ok, I guess so")
window.update()
time.sleep(1)
set_background("moon")

window.update()
turtle.exitonclick()