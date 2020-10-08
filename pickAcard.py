lives = 5

def cardPickup():
    global lives
    print("I have a deck of 52 cards including the Jokers.\nI have selected a random card.")
    cardChoice = input("What card is in my hand?\n")
    cards = ["ace of spades", "ace of hearts", "ace of diamonds", "ace of clubs",  "2 of spades", "2 of hearts", "2 of diamonds", "2 of clubs", "3 of spades", "3 of hearts", "3 of diamonds", "3 of clubs", "4 of spades", "4 of hearts", "4 of diamonds", "4 of clubs", "5 of spades", "5 of hearts", "5 of diamonds", "5 of clubs", "6 of spades", "6 of hearts", "6 of diamonds", "6 of clubs", "7 of spades", "7 of hearts", "7 of diamonds", "7 of clubs", "8 of spades", "8 of hearts", "8 of diamonds", "8 of clubs", "9 of spades", "9 of hearts", "9 of diamonds", "9 of clubs", "10 of spades", "10 of hearts", "10 of diamonds", "10 of clubs", "jack of spades", "jack of hearts", "jack of diamonds", "jack of clubs", "queen of spades", "queen of hearts", "queen of diamonds", "queen of clubs", "king of spades", "king of hearts", "king of diamonds", "king of clubs", "joker"]
    while cardChoice not in cards:
        print("Thats not a card...")
    wins = 0
    while lives > 0 and wins < 1:
        drop = random.randint(1,52)

