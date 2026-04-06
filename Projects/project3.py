from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-100
y1 =120
x2 =-100
y2 =70
x3 =-100
y3 =20
x4 =-100
y4 =-30


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("summer.gif")
t1 = create_sprite("turtle2",x1,y1)
t2 = create_sprite("turtle2",x2,y2)
t3 = create_sprite("turtle2",x3,y3)
t4 = create_sprite("turtle2",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    #Turtle 1 has the best chances
    x1 +=random.randint(8,14)
    x2 +=random.randint(7,14)
    x3 +=random.randint(7,13)
    x4 +=random.randint(7,13)
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("turtle 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("turtle 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("turtle 3 wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    s5.write("turtle 4 wins!")


turtle.exitonclick()