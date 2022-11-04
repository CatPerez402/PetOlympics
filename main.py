# Catalina Perez
# This is a pet olympics game. You will train your pet to compete in several games. There are 3
# olympic games :math, racing, and beauty. The olympic games occur at the end of each week when
# your pet runs out of stamina.

from text import *
import time
import random


# Math Training
# Player asks pet math questions and pet answers them
def math_training():
    print("You have chosen: Math Training!\nHere you get to ask your pet math questions!\nEach question gives your "
          "pet 2 smartness!")
    time.sleep(5)
    framing_details()
    for _ in range(3):
        math_quiz()


# Stamina Training
# Player will be asked to walk and feed their pet
# They will do this by typing what the prompt asks of them
# Very repetitive
def stamina_training():
    print("You have chosen: Stamina Training!\n Here you will be told to input certain tasks in order to raise your "
          "pet's stamina!\nThis whole training will give your pet 10 stamina!")
    time.sleep(5)
    framing_details()
    for _ in range(3):
        run = input("Type 'run' to make pet run!").lower()
        if run != "run":
            print("That's one way to spell it!")
        else:
            print("Running...")
        time.sleep(2)
        jump = input("Type 'jump' to make pet do jumping jacks").lower()
        if jump != "jump":
            print("That's one way to spell it!")
        else:
            print("Jumping jacks...")
        time.sleep(2)
        yoga = input("Type 'yoga' to make pet do yoga").lower()
        if yoga != "yoga":
            print("That's one way to spell it!")
        else:
            print("Yoga...")
        time.sleep(2)


def speed_training(track_runs, pet_run):
    print("You have chosen: Speed Training!\nHere your pet will run around the track as many times as you said!")
    time.sleep(3)
    for _ in range(track_runs):
        print("3...2...1...GO!")
        print(pet_run)
        print("Wow! So fast!")
        print(f"Time: {random.randint(10, 20)} seconds")
        time.sleep(10)


def beauty_training():
    print("You have chosen: Beauty Training! Here you will be required to answer beauty questions!")


def framing_details():
    print("+" * 100, "|" * 2, sep=' ', end='\n')  # Framing details for game, multiple +
    print("+" * 100, "|" * 2, sep=' ', end='\n')  # *100 prints the + 100 times on the line


# Math Quiz is used to train your pet.
# Calculator for Math Quiz


def add(n1, n2):
    return n1 + n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def power(n1, n2):
    return n1 ** n2


def floor_divide(n1, n2):
    return n1 // n2


def modulus(n1, n2):
    return n1 % n2


# Dictionary of math operation options
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "//": floor_divide,
    "%": modulus
}


def math_quiz():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:  # This will go to the dictionary and display choices of operations
        print(symbol)
    calculations = True  # Starts our calculation while loop

    while calculations:
        operation_symbol = input("Which operation do you want to use?")
        num2 = float(input("What is the next number you want to use?: "))
        calculate = operations[operation_symbol]  # Takes the symbol of the operation and its function
        answer = calculate(num1, num2)  # Calculates the two numbers

        print(f"Pet answer: {num1} {operation_symbol} {num2} = {answer}")  # Prints out answer
        break


stamina = 5
smartness = 0
speed = 0
beauty = 0
# Intro into the game!
game = True
while game:
    print(logo)
    starting_choice = input("Start\n""About\n""How to Play\n""Choice:").lower()
    if starting_choice == "start":
        framing_details()
        pre_olympic = True
        break
    elif starting_choice == "about":  # Game summary
        print(game_sum)
        time.sleep(15)
    elif starting_choice == "how to play":  # Game rules
        print(game_rules)
        time.sleep(15)

while pre_olympic:  # Week before olympics
    print("Welcome to the Pre", "olympics!", sep="-")
    player_name = input("For starters, what is your name?")
    print("Now, let's choose your pet and its name!")
    print(pet_list)
    pet_breed = input("What pet would you like?").lower()
    pet_choice = pet[pet_breed]  # Gets image for pet (pet)
    print(pet_choice)
    pet_name = input("What is your pet's name?")
    confirm_pet = input(
        "So your name is " + player_name + " your pet is a " + pet_breed + " and their name is " + pet_name + "? Y or N"
    ).lower()  # Concatenates variables and string
    if confirm_pet == "y":
        print("Great! Let's continue to the first week!")
        first_week = True
        framing_details()
        break  # End of pre olympics
    if confirm_pet == "n":
        print("Let's try this again then!")
        time.sleep(3)
        framing_details()
        continue
while first_week:  # First Week of Olympics

    time.sleep(3)
    print(f"Welcome to the first week {player_name} and {pet_name}!\nYou have 4 things you can train: math, stamina, "
          f"speed and beauty!\nYou have 20 stamina right now. Each training takes 5 stamina. Be sure to use it "
          f"wisely!\nThe olympic game this week is in math so be sure to train your pet's math skills!")
    time.sleep(10)
    first_week_train = True
    while first_week_train:  # Training Montage
        framing_details()
        # if stamina == 0:
        #     print("Whoops! Not enough stamina! On to the first game! ")
        #     first_week_train = False
        #     first_week = False
        #     math_olympic = True
        if not stamina == 20 and not stamina < 20:
            print("Wow! Your pet has so much energy!")
        print(f"Pet stamina: {stamina}  Pet smartness: {smartness}  Pet speed: {speed}  Pet beauty: {beauty}")
        print(pet_choice)
        train_choice_1 = input("Math Training\nStamina Training\nSpeed Training\nBeauty Training\nChoice:").lower()
        if stamina == 0:
            print("Whoops! Not enough stamina! On to the first game! ")
            first_week_train = False
            first_week = False
            math_olympic = True
        elif train_choice_1 == "math training":
            math_training()
            smartness += 6
            stamina -= 5
            print("Great job! Your pet has earned 6 smartness.")
            print(f"This brings {pet_name} to {smartness} smartness!")
            time.sleep(5)
        elif train_choice_1 == "stamina training":
            stamina_training()
            stamina += 10
            print("Great job! Your pet has earned 10 stamina.")
            print(f"This brings {pet_name} to {stamina} stamina!")
            time.sleep(5)
        elif train_choice_1 == "speed training":
            speedy = int(input("Before we begin, how many times do you want your pet to run around the track? Choose "
                               "between 1-5."))
            if speedy < 1 or speedy > 5:
                speedy = int(input("Please enter a valid number between 1-5."))
            speed_training(speedy, pet_choice)
            speed += speedy * 2
            print("Great job!")
            print(f"This brings {pet_name} to {speed} speed!")
        elif train_choice_1 == "beauty training":
            pass
while math_olympic: # Not finished
    time.sleep(3)
    print("Welcome to the Math Olympics Game! Here your pet will compete against 3 other pets!")
    rudy = random.randint(6,26)
    maxie = random.randint(0,15)
    scooby = random.randint(0,30)
    quiz_pets = {rudy:"Rudy",maxie:"Maxie",scooby:"Scooby"}
    math_winner = quiz_pets.get(max(quiz_pets))
    math_mega_loser = quiz_pets.get(min(quiz_pets))
    print("Time to compete!")
    time.sleep(3)
    # will fill in text for more realism
    print("And the winner is...")
    time.sleep(3)
    print(math_winner)
    time.sleep(3)
    print("In last place is...")
    time.sleep(3)
    print(math_mega_loser)



