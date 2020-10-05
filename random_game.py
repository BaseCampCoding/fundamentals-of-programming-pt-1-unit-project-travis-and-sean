import random
number = random.randint(1, 20)
players_name = input(" What is your name? ")
number_of_guesses = 0
print(player_name + " I am Guessing a number between 1 and 20:")
 
while number_of_guesses < 5:
























wins = 0 
losses = 0
def rock_paper_scissors():
    com = random.randint(1, 3)
    shoot = input("Rock, Paper, Scissors... SHOOT!: ")
    if com == 1 and shoot == "rock":
        result = ("tie")
        
    elif com == 1 and shoot == "paper":
        result = ("winner")
       
    elif com == 1 and shoot == "scissors":
        result = ("loser")
         
    if com == 2 and shoot == "paper":
        result = ("tie")
        
    elif com == 2 and shoot == "rock":
        result = ("loser")
           
    elif com == 2 and shoot == "scissors":
        result = ("winner")
        
    if com == 3 and shoot == "rock":
        result = ("winner")
        
    elif com == 3 and shoot == "paper":
        result = ("loser")
        
    else:
        if com == 3 and shoot == "scissors":
            result = ("tie")
    return result




