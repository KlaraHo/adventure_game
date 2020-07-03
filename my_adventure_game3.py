import time
import random
import sys

kids = ["daughter", "son", "kid"]
dress = ["a-line", "mermaid", "princess-line"]
color_dress = ["ivory", "offwhite", "pearlwhite", "white"]
reward = ["a giant pot filled with gold", "a small leather bag filled with silver coins"]

def print_pause(text):
    print(text)
    time.sleep(0)

def begin_text():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that the king of the kingdom nearby wants his " + random.choice(kids) + " to get married.")
    print_pause("Fortunately the groom has been chosen already.")
    print_pause("But what are you doing here then?")
    print_pause("The future bride is still looking for her perfect dress!")
    print_pause("There is also " + random.choice(reward) + " for the one bringing THE dress as a reward! Hooray!")
    print_pause("Enter 1 to go to the town tailor.")
    print_pause("Enter 2 to walk towards the house standing at the end of the flower field.")
    print_pause("What would you like to do?")
    print_pause("Please enter 1 or 2.")

def stand_up():
    print_pause("You decide to stand up.")
    print_pause("But you are too weak to stand on your own feet.")
    print_pause("While you almost pass out, you try to hold yourself onto some tailor-made clothes. And...")
    print_pause("Some of your blood ruins those wonderful dresses. The tailor himself gets you arrested.")

def ask_for_help():
    print_pause("You don't feel very well and decide to ask the tailor for help.")
    print_pause("The tailor comes to you and helps you on your feet.")
    print_pause("After a small break you are strong enough.")

def go_inside():
    print_pause("You open the fortunately unlocked door and step into the enchanting house.")
    print_pause("It is full of dust and cobwebs, but that doesn't discourage you.")
    print_pause("You really are a brave pal.")
    print_pause("As you come closer, you find old, but extremely high-quality fabric.")
    print_pause("And there you find magical sewing skills!")

def back_to_field():
    print_pause("You head back to the field.")
    print_pause("Would you like to (1) go to the town tailor or (2) walk towards the house standing at the end of the flower field?")
    print_pause("Please enter 1 or 2.")

def for_the_win():
    print_pause("You walk right into the best tailor's place in the kingdom.")
    print_pause("As you open the door, the tailor senses your perfect sewing skills.")
    print_pause("He almost bursts in joy and offers you all his material for your work.")
    print_pause("You design and sew a wonderful" + random.choice(dress) + " in the color " + random.choice(color_dress))
    print_pause("The whole kingdom loves your design and you recieve the reward.")

def tailor():
    print_pause("You walk through the flower field and head to the town.")
    print_pause("As you walk into the tailor's place, happy and smiling, you stumble and fall.")
    print_pause("Oh no, you hurt yourself!")
    print_pause("Do would want to (1) stand up or (2) ask for help?")
    y = input()
    check_input(y)
    if "sewing" in magical_skills :
        for_the_win()
        you_win()
        play_again()
    else:
        if y == "1":
            stand_up()
            game_over()
            play_again()
        elif y == "2":
            ask_for_help()
            back_to_field()

def house():
    print_pause("You walk to the tiny house and knock on the door.")
    print_pause("Nothing happens.")
    print_pause("You knock again.")
    print_pause("Nothing. You try to take a glimpse through the windows, but you can't see anything. It's too dark inside.")
    print_pause("Do you want to (1) go inside or (2) go back to the field?")
    print_pause("Please enter 1 or 2.")
    y = input()
    check_input(y)
    if y == "1":
        go_inside()
        magical_skills.append("sewing")
        back_to_field()
    elif y == "2":
        back_to_field()

def check_input(x):
    while x != "1" and x != "2":
        x = input("Please enter 1 or 2.\n")

def check_input_play_again(play):
    while play != "y" and play != "n":
        play = input("Please enter y or n.\n")

def game_over():
    print_pause("Game over.")

def you_win():
    print_pause("Congratulations, you have impressed the whole kingdom!")

def play_again():
    magical_skills = []
    print_pause("Would you like to play again? y/n")
    play = input()
    check_input_play_again(play)
    if play == "y":
        begin_text()
    elif play == "n":
        print("Thanks for playing! See you soon.")
        sys.exit()


begin_text()
magical_skills = ["something"]
while True:
    x = input()
    check_input(x)
    if x == "2":
        house()
    elif x == "1":
        tailor()
