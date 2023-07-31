#!/usr/bin/python3
import random

def comp_rock_paper_scissors():
    rand_selection = random.randint(0, 2)
    choices = ['rock', 'paper', 'scissors']

    return choices[rand_selection]

def print_win(user_input, comp_input):
    print("YAY, You win! {} beats {}".format(user_input, comp_input))

def print_lose(user_input, comp_input):
    print("Sorry, you lose. {} beats {}".format(comp_input, user_input))

comp_input = comp_rock_paper_scissors()
input = str(input("Do you choose: Rock, Paper or Scissors?: "))
user_input = input.lower()
print("Your choice:{} | Computer:{}".format(user_input, comp_input))

if user_input == comp_input:
    print("It's a DRAW! You both said {}".format(user_input))
else:
    if user_input == 'rock':
        if comp_input == 'paper':
            print_win(user_input, comp_input)
        else:
            print_lose(user_input, comp_input)

    elif user_input == 'paper':
        if comp_input == 'rock':
            print_win(user_input, comp_input)
        else:
            print_lose(user_input, comp_input)

    elif user_input == 'scissors':
        if comp_input == 'rock':
            print_lose(user_input, comp_input)
        else:
            print_win(user_input, comp_input)

    else:
        print("Wrong input, please try again. Enter either 'rock', 'paper', or 'scissors' ")
