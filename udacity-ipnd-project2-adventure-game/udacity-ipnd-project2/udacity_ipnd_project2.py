import random
import time
import sys

the_dark_cave_visited = False
attackers = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
attacker = random.choice(attackers)
# player's default weapon
player_weapon = 'dagger'


# Function that prints game instructions and then pause
def print_pause(game_instructions, pause_duration):
    print(game_instructions)
    time.sleep(pause_duration)


# Decides olayer weapon and dicision to fight or not
def fight(player_weapon):
    print_pause(f"The {attacker} attacks you!", 2)
    if player_weapon == "dagger":
        print_pause(f"You feel under-prepared with a tiny {player_weapon}.", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Would you like to (1) fight or (2) run away?\n")
        if choice == '1':
            if player_weapon == "dagger":
                print_pause(f"You do your best...", 1)
                print_pause(f"a {player_weapon} nothing against {attacker}", 2)
                print_pause(f"You have been defeated!""", 2)
            elif player_weapon == "sword":
                print_pause(f"As {attacker} moves to attack, you use sword", 2)
                print_pause(f"The Sword of Ogoroth shines brightly", 3)
                print_pause(f"But {attacker} looks sword and runs away!", 3)
                print_pause(f"You save town from {attacker}. You win", 3)
        elif choice == '2':
            print_pause("You run back into the field. Luckily, unseen", 2)
            place_to_go()


# Asks the player if they would play the game again,
# if they select no program exits,
# if they select yes the game starts again
def replay_game():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n")
        if choice == 'n':
            print_pause("Thanks for playing! See you next time.", 2)
            sys.exit()
        elif choice == 'y':
            print_pause("Excellent! Restarting the game ...", 2)
            player_weapon = 'dagger'
            play_game()


# Prints and descries opening sequences in text
def opening_sequence():
    print_pause("You find yourself standing in an open field", 3)
    print_pause(f"A {attacker} is terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark dark cave.", 2)
    print_pause(f"In your hand you hold your {player_weapon}.", 2)


# Decides the place the player would like to go
def place_to_go():
    print_pause("", 1)
    print_pause("Enter 1 to knock on the door of the house.", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    print_pause("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == '1':
            the_house()
        elif choice == '2':
            the_dark_cave()


# Defines the sequence in the house
def the_house():
    print_pause("You approach the door of the house.", 2)
    print_pause(f"The door opens and out steps a {attacker}.", 2)
    print_pause(f"Eep! This is the {attacker}'s house!", 2)
    fight(player_weapon)


# Defines the sequence in the dark cave
def the_dark_cave():
    global the_dark_cave_visited
    # change player weapon
    global player_weapon
    print_pause("You peer cautiously into the the_dark_cave.", 2)
    if the_dark_cave_visited:
        print_pause("You've been here beore. It's empty now.", 2)
    elif the_dark_cave_visited is False:
        print_pause("It turns out to be only a very small the_dark_cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause(f"You throw away {player_weapon} and take the sword", 2)
        player_weapon = "sword"
    the_dark_cave_visited = True
    print_pause("You walk back out to the field.", 2)
    place_to_go()


# Game state: if state is running continue with the game
# if state is game_over, the game ends.
def play_game():
    game_state = 'running'
    while game_state == 'running':
        opening_sequence()
        place_to_go()
        replay_game()


play_game()