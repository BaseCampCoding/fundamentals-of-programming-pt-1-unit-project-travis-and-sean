import random
lives = 5
def the_random_game():
    
    def random_number():
        global lives
        number = random.randint(1, 20)
        print(player_name + ", I am guessing a number between 1 and 20: ")
        while True:
            player_number = input("What is your number? ")
            if player_number.isdigit():
                player_number = int(player_number)
                break 
        while lives > 0:          
            if player_number < number:
                print("Your guess is too low")
                lives -= 1
                print("You have " + str(lives) + " lives left!")  
            elif player_number > number:
                print("Your guess is too high")
                lives -= 1
                print("You have " + str(lives) + " lives left!")
            elif player_number == number:
                print("CORRECT!")
                print(str(player_name) + ", you have " + str(lives) + " lives left!")
                break  
            if lives == 0:
                print("You are out of lives, the number was " + str(number))           
        else:
            print("Please enter a number 1-20")
            while True:
                player_number = input("What is your number? ")
                if player_number.isdigit():
<<<<<<< HEAD
                    player_number = int(player_number)
                    break
=======
                    player_number = int(player_number)     
                    if player_number < number:
                        print("Your guess is too low")
                        lives -= 1
                        print("You have " + str(lives) + " lives left!")  
                    elif player_number > number:
                        print("Your guess is too high")
                        lives -= 1
                        print("You have " + str(lives) + " lives left!")
                    elif player_number == number:
                        print("CORRECT!")
                        print(str(player_name) + ", you have " + str(lives) + " lives left!")
                        break  
                    if lives == 0:
                        print("You are out of lives, the number was " + str(number))           
>>>>>>> b8284bef4f6b9ed04ce767686137ca5792ce7528
                else:
                    print("Enter a number between 1-20")

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

    def coinFlip():
        global lives
        flip = random.randint(1,2)
        choices = ["heads", "tails"]
        wins = 0
        while lives > 0 and wins < 1:
            headsORtails = input("Heads or Tails? \n")
            headsORtails = headsORtails.lower()
            while headsORtails not in choices:
                print("You must choose Heads or Tails")
                headsORtails = input("Heads or Tails? \n")
            if headsORtails == "heads" and flip == 1:
                print("Correct!")
                wins += 1
            elif headsORtails == "heads" and flip == 2:
                print("It was Tails!")
                lives -= 1
                print(f"You have {lives} lives left!")
            elif headsORtails == "tails" and flip == 2:
                print("Correct!")
                wins += 1
            elif headsORtails == "tails" and flip == 1:
                print("It was Heads!")
                lives -= 1
            print(f"You have {lives} lives left!")    
                
        
    games = ["rock paper scissors", "guess the number", "coin flip"]

    player_name = input("What is your name? \n")
    while games != [] and lives > 0:
        for game in games:
            print(game)
        game_choice = input("Which game do you want to play? (Press q to quit)\n")
        game_choice = game_choice.lower()
        if game_choice == "quit" or game_choice == "q":
            print("Goodbye")
            quit() 
        while game_choice not in games:
            print("Please Enter A Valid Game.")
            game_choice = input("Which game do you want to play? \n")
        if game_choice in games:
            if game_choice == "guess the number":
                random_number()
            elif game_choice == "rock paper scissors":
                rpsWins()
            elif game_choice == "coin flip":
                coinFlip()
             
the_random_game()

