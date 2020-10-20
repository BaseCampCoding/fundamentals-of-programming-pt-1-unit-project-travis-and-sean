import turtle
import time

wn = turtle.Screen()
wn.title("Game of Chance!")
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("circle")
player.color("green")



def player_animate():
    if player.shape() == "circle":
        player.shape("square")
    elif player.shape() == "square":
       player.shape("circle")
    wn.ontimer(player_animate, 500)
    
    

while True:
     player_animate()




wn.mainloop()