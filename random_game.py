import random
import colorama
from colorama import Fore, Style
colorama.init()

lives = 0
text = "Welcome to The Game of Chance!"
print(Fore.LIGHTCYAN_EX + text + Style.RESET_ALL)
player_name = input("What is your name?\n")
def the_random_game():
    global lives
    lives += 5
    def random_number():
        global lives
        number = random.randint(1, 20)
        print("\n", player_name + ", I am guessing a number between 1 and 20: ")
        
        while True:
            player_number = input("What is your number? ")
            if player_number.isdigit():
                player_number = int(player_number)  
                break
            else:
                print("\nPlease enter a number 1-20")  
        while lives > 0:
            if player_number < number:
                print("\nYour guess is too low")
                lives -= 1
                if lives == 0:
                    print("\nYou are out of lives, the number was " + str(number))
                    break 
                print("You have " + str(lives) + " lives left!")
                while True:
                    player_number = input("What is your number? ")
                    if player_number.isdigit():
                        player_number = int(player_number)  
                        break
                    else:
                        print("Please enter a number 1-20")
                
            elif player_number > number:
                print("\nYour guess is too high")
                lives -= 1
                if lives == 0:
                    print("\nYou are out of lives, the number was " + str(number))
                    break 
                print("You have " + str(lives) + " lives left!")
                while True:
                    player_number = input("What is your number? ")
                    if player_number.isdigit():
                        player_number = int(player_number)  
                        break 
                    else:
                        print("Please enter a number 1-20")  
            elif player_number == number:
                text = "\nCORRECT!"
                print(Fore.LIGHTGREEN_EX + text + Style.RESET_ALL) 
                print("\n", str(player_name) + ", you have " + str(lives) + " lives left!\n")
                break 

    def rock_paper_scissors():
        global lives
        com = random.randint(1, 3)
        shoot = input("\nRock, Paper, Scissors... SHOOT!: ")
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
                text = "\nYou win!"
                text2 = "+1 life\n"
                print(Fore.LIGHTGREEN_EX + text)
                print(Fore.LIGHTGREEN_EX + text2 + Style.RESET_ALL)
                wins += 1
                lives += 1
                print(str(player_name) + ", you have " + str(lives) + " lives left!")
                print()
                
            elif result == "loser":
                text = "\nYou lose"
                lives -= 1
                print(Fore.RED + text + Style.RESET_ALL)
                print(Fore.LIGHTMAGENTA_EX + "\nYou have {lives} lives left." + Style.RESET_ALL)    

            elif result == "tie":
                print(Fore.LIGHTCYAN_EX + "\nThat was a tie" + Style.RESET_ALL)      

    def coinFlip():
        global lives
        flip = random.randint(1,2)
        choices = ["heads", "tails"]
        wins = 0
        while lives > 0 and wins < 1:
            flip = random.randint(1,2)
            headsORtails = input("\nHeads or Tails? \n")
            headsORtails = headsORtails.lower()
            while headsORtails not in choices:
                print(Fore.LIGHTRED_EX + "You must choose Heads or Tails" + Style.RESET_ALL)
                headsORtails = input("Heads or Tails? \n")
            if headsORtails == "heads" and flip == 1:
                text = "\nCorrect!"
                wins += 1
                print(Fore.LIGHTGREEN_EX + text + Style.RESET_ALL)
            elif headsORtails == "heads" and flip == 2:
                result = "\nIt was Tails!"
                print(Fore.LIGHTRED_EX + result + Style.RESET_ALL)
                lives -= 1
                print(Fore.LIGHTMAGENTA_EX + f"\nYou have {lives} lives left!" + Style.RESET_ALL)
            elif headsORtails == "tails" and flip == 2:
                text = "\nCorrect!"
                wins += 1
                print(Fore.LIGHTGREEN_EX + text + Style.RESET_ALL)
            elif headsORtails == "tails" and flip == 1:
                result = "\nIt was Heads!"
                print(Fore.LIGHTRED_EX + result + Style.RESET_ALL)
                lives -= 1
                print(Fore.LIGHTMAGENTA_EX + f"\nYou have {lives} lives left!" + Style.RESET_ALL)                
        
    games = ["rock paper scissors", "guess the number", "coin flip"]
    

    while games != [] and lives > 0:
        for game in games:
            print(Fore.LIGHTYELLOW_EX + "\n", game, "\n" + Style.RESET_ALL)

        game_choice = input("Which game do you want to play? (Press q to quit)\n")
        game_choice = game_choice.lower()
        if game_choice == "quit" or game_choice == "q":
            print("Goodbye")
            quit()
        while game_choice not in games:
            print(Fore.LIGHTRED_EX + "Please Enter A Valid Game." + Style.RESET_ALL)
            game_choice = input("Which game do you want to play? \n")
        if game_choice in games:
            if game_choice == "guess the number" or game_choice == 2:
                random_number()
                games.remove("guess the number")
            elif game_choice == "rock paper scissors" or game_choice == 1:
                rpsWins()
                games.remove("rock paper scissors")
            elif game_choice == "coin flip" or game_choice == 3:
                coinFlip()
                games.remove("coin flip")

    responses = ['y', 'n', 'yes', 'no']
    while lives == 0 or games == []:
        print(Fore.LIGHTCYAN_EX + "Congratulations!" + Style.RESET_ALL + "You have Completed The Game of Chance\n")
        replay = input("Do you want to play again? [Y/N]\n")
        replay = replay.lower()
        while replay not in responses:
            print(Fore.LIGHTRED_EX + "Please Enter A Valid Option" + Style.RESET_ALL)
            replay = input("Do you want to play again? [Y/N]\n")
        if replay == 'y' or replay == 'yes':
            lives = 0
            the_random_game()
            break
        elif replay == 'n' or replay == 'no':
            print("Goodbye.")
            quit()

the_random_game()

