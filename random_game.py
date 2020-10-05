import random
number = random.randint(1, 20)
player_name = input("What is your name? \n")
lives = 5

def random_number():
    print(player_name + ", I am guessing a number between 1 and 20: ")
    while lives > 0:
        player_number = int(input("What is your number? "))
        lives -= 1
        if player_number < number:
            print("Your guess is too low")
            print("You have " + str(lives) + " lives left!")
        elif player_number > number:
            print("Your guess is too high")
            print("You have " + str(lives) + " lives left!")
        elif player_number == number:
            break

        if player_number == number:
            print(str(player_name) + " have " + str(lives) + " left!")
        else:
            print("You are out of lives, the number was " + str(number))






def rock_paper_scissors():
    com = random.randint(1, 3)
    shoot = input("Rock, Paper, Scissors... SHOOT!: ")
    responses = ["rock", "paper", "scissors"]
    while shoot not in responses:
        print("Please enter valid option.")
        shoot = input("Rock, Paper, Scissors... SHOOT!: ")
    if com == 1 and shoot == "rock":
        result = ("tie")
        
    elif com == 1 and shoot == "paper":
        result = ("loser")
       
    elif com == 1 and shoot == "scissors":
        result = ("winner")
         
    if com == 2 and shoot == "paper":
        result = ("tie")
        
    elif com == 2 and shoot == "rock":
        result = ("winner")
           
    elif com == 2 and shoot == "scissors":
        result = ("loser")
        
    if com == 3 and shoot == "rock":
        result = ("loser")
        
    elif com == 3 and shoot == "paper":
        result = ("winner")
        
    else:
        if com == 3 and shoot == "scissors":
            result = ("tie")
    wins = 0
    while wins < 1 and lives > 0:  
        result = rock_paper_scissors()
        if result == "winner":
            print("You win!")
        elif result == "loser":
            print("You lose")
            lives -= 1
        elif result == "tie":
            print("That was a tie")      

rock_paper_scissors()