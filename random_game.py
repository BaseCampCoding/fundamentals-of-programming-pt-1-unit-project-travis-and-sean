import random
number = random.randint(1, 20)
player_name = input(" What is your name? ")
number_of_guesses = 0
print(player_name + " I am Guessing a number between 1 and 20:")
 
while number_of_guesses < 5:
    player_number = input("What is your number? ")
    number_of_guesses += 1
    if player_number < number:
        print("Your guess is too low")
    elif player_number 
