grandmas= 0
alien = 0
cost = 0

from utils import *
# My backdrop
# Section 1 - setup
# TODO - set a background using set_background()
set_background("summer")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
#This is the Introduction that explains the game

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -100,100)
print(f"Welcome to alien clicker!")
print(f"Press (q) to get aliens")
print(f"Press (space key) to get grandmas")
m1.hideturtle()




# Section 2 - controls
# When you press q it makes an alines that gives you 6 dollars and it spawns in a random location
def get_alien():
    global alien, cost
    alien += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("alien",x,y)
    cost +=6
    print("alien:{alien}")

window.onkeypress(get_alien, "q")
# When you press space key it makes an sodacans for decoration and it spawns in a random location
def get_grandmas():
    global alien, grandmas, cost
    if cost >= grandmas:
        cost -= 15
        grandmas += 1
        
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("sodacan",x,y)
        print("Grandmas:{grandmas}")

# TODO - define an action. ex: def my_control()
window.onkeypress(get_grandmas, "space")
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):

    
    # TODO - put any automatic actions here

# displays the amount of sodacans, aliens, and amount of money

    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"alien: {alien} \n Money: ${cost} \n sodacans: {grandmas}", font= ("Arial", 16, "normal"))

    time.sleep(0.01)
    window.update()