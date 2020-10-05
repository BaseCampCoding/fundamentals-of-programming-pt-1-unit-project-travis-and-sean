import random
number = random.randint(1, 20)
player_name = input("What is your name? \n")
print(player_name + ", I am guessing a number between 1 and 20: ")
lives = 5

while lives > 0:
    player_number = input("What is your number? ")
    lives -= 1
    if player_number < number:
        print("Your guess is too low")
    elif player_number    
