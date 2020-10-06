import random



player_name = input("What is your name? \n")

game_choice = input("Which game do you want to play? \nWe have Rock Paper Scissors, Guess The Number, and Coin Flip. \n")
games = ["rock paper scissors", "guess the number", "coin flip"]
game_choice = game_choice.lower()
while game_choice not in games:
    print("Please Enter A Valid Game.")
    game_choice = input("Which game do you want to play? \n")
    if game_choice in games:
        break

lives = 5
def random_number():
    global lives
    number = random.randint(1, 20)
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
            print("CORRECT!")
            print(str(player_name) + ", you have " + str(lives) + " left!")
            
        if lives == 0:
            print("You are out of lives, the number was " + str(number))

def rock_paper_scissors():
    global lives
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
    return result

def rpsWins():
    global lives
    wins = 0
    while wins < 1 and lives > 0:  
        result = rock_paper_scissors()
        if result == "winner":
            print("You win!")
            wins += 1
        elif result == "loser":
            print("You lose")
            lives -= 1
            print(f"You have {lives} lives left.")    
        elif result == "tie":
            print("That was a tie")      



if game_choice == "guess the number":
    random_number()
elif game_choice == "rock paper scissors":
    rpsWins()