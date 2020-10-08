import random
import colorama
from colorama import Fore, Style
colorama.init()

lives = 0
 
print(Fore.LIGHTCYAN_EX + "Welcome to The Game of Chance!" + Style.RESET_ALL)
player_name = input("What is your name?\n")
def the_random_game():
    global lives
    lives += 5
    def random_number():
        global lives
        number = random.randint(1, 20)
        print('\n' + player_name + ", I am guessing a number between 1 and 20: ")
        
        while True:
            player_number = input("What is your number? ")
            if player_number.isdigit():
                player_number = int(player_number)
                break
            else:
                print(Fore.LIGHTRED_EX + "\nPlease enter a number 1-20" + Style.RESET_ALL)  
        while lives > 0:
            if player_number < number:
                print("\nYour guess is too low")
                lives -= 1
                if lives == 0:
                    print(Fore.LIGHTRED_EX + "\nYou are out of lives, the number was " + str(number) + Style.RESET_ALL)
                    break 
                print(Fore.LIGHTMAGENTA_EX + "You have " + str(lives) + " lives left!" + Style.RESET_ALL)
                while True:
                    player_number = input("What is your number? ")
                    if player_number.isdigit():
                        player_number = int(player_number)  
                        break
                    else:
                        print(Fore.LIGHTRED_EX + "Please enter a number 1-20" + Style.RESET_ALL)
                
            elif player_number > number:
                print("\nYour guess is too high")
                lives -= 1
                if lives == 0:
                    print(Fore.LIGHTRED_EX + "\nYou are out of lives, the number was " + str(number) + Style.RESET_ALL)
                    break 
                print(Fore.LIGHTMAGENTA_EX + "You have " + str(lives) + " lives left!" + Style.RESET_ALL)
                while True:
                    player_number = input("What is your number? ")
                    if player_number.isdigit():
                        player_number = int(player_number)  
                        break 
                    else:
                        print(Fore.LIGHTRED_EX + "Please enter a number 1-20" + Style.RESET_ALL)  
            elif player_number == number:
                text = "\nCORRECT!\n"
                print(Fore.LIGHTGREEN_EX + text + Style.RESET_ALL) 
                print(Fore.LIGHTMAGENTA_EX + str(player_name) + ", you have " + str(lives) + " lives left!\n" + Style.RESET_ALL)
                break 

    def rock_paper_scissors():
        global lives
        com = random.randint(1, 3)
        shoot = input("\nRock, Paper, Scissors... SHOOT!: ")
        responses = ["rock", "paper", "scissors"]
        while shoot not in responses:
            print(Fore.LIGHTRED_EX + "Please enter valid option." + Style.RESET_ALL)
            shoot = input(Fore.MAGENTA + "Rock, Paper, Scissors... SHOOT!: " + Style.RESET_ALL)
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
    
    def horse_game():
        global lives
        num = random.randint(1, 4)
        player_horse = input("Pick a Horse number\nLucky[1], Speedy[2], Lightning[3], Slow Poke[4]: ")
        response = ["1", "2", "3", "4"]
        while player_horse not in response:
            print("Please pick a horse number!")
            player_horse = input("Lucky[1], Speedy[2], Lightning[3], Slow Poke[4]: ")
        ## Lucky
        if num == 1 and player_horse == "1":
            result = ("won")
        elif num == 1 and player_horse == "2":
            result = ("1lost")
        elif num == 1 and player_horse == "3":
            result = ("1lost")
        elif num == 1 and player_horse == "4":
            result = ("1lost")
        elif num == 2 and player_horse == "1":
            result = ("2lost")
        elif num == 2 and player_horse == "2":
            result = ("won")
        elif num == 2 and player_horse == "3":
            result = ("2lost")
        elif num == 2 and player_horse == "4":
            result = ("2lost")
        elif num == 3 and player_horse == "1":
            result = ("3lost")
        elif num == 3 and player_horse == "2":
            result = ("3lost")
        elif num == 3 and player_horse == "3":
            result = ("won")
        elif num == 3 and player_horse == "4":
            result = ("3lost")
        elif num == 4 and player_horse == "1":
            result = ("4lost")
        elif num == 4 and player_horse == "2":
            result = ("4lost")
        elif num == 4 and player_horse == "3":
            result = ("4lost")
        elif num == 4 and player_horse == "4":
            result = ("won")
        return result

    def horseWINS():
        global lives
        wins = 0
        while wins < 1 and lives > 0:
            result = horse_game()
            lost = ["1lost", "2lost", "3lost", "4lost"]
            while result == "won":
                wins += 1
                print(Fore.LIGHTCYAN_EX+ "Your horse won" + Style.RESET_ALL)
                print()
                break
            while result in lost:
                lives -= 1
                print("Your horse lost")
                print(Fore.LIGHTMAGENTA_EX + f"You have {lives} lives left!\n" + Style.RESET_ALL)
                break
    
    games = ["rock paper scissors", "guess the number", "coin flip", "horse race"]
    

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
            if game_choice == "quit" or game_choice == "q":
                print("Goodbye")
                quit()
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
            elif game_choice == "horse race":
                horseWINS()
                games.remove("horse race")

    responses = ['y', 'n', 'yes', 'no']
    while lives == 0 or games == []:
        if lives > 0 and games == []:
            print(Fore.LIGHTCYAN_EX + "Congratulations!" + Style.RESET_ALL + ", You have Completed The Game of Chance\n")
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

