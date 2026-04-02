# Section 1 - Your code
from utils import *
set_background("pond")

s1 = create_sprite("fish", 10, 100)
s2 = create_sprite("fish", -10, 100)
s2 = create_sprite("fish", -10, -100)
s2 = create_sprite("fish", 10, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Willem",font = ("Arial", 40, "normal"))
message1.hideturtle()

window.update()
turtle.exitonclick()