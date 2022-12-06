__author__ = "Catalina Perez"

# This is a pet olympics game. You will train your pet to compete in several games. There are 3
# olympic games :math, racing, and beauty. The olympic games occur at the end of each week when
# your pet runs out of stamina.

import random
import time
from text import *

pet_stats = {"stamina": 20, "smartness": 0, "speed": 0, "beauty": 0}


# Math Training
# Player asks pet math questions and pet answers them
def math_training():
    """
    math training for pet, uses pet as a calculator
    """
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
    """
    stamina training for pet, use types what prompt asks for
    """
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


# Speed Training
# Gives pet more speed
# No tasks required
def speed_training(track_runs):
    """
    speed training for pet, no user inputs needed
    :param track_runs:
    """
    print("You have chosen: Speed Training!\nHere your pet will run around the track as many times as you said!")
    time.sleep(3)
    for _ in range(track_runs):
        print("3...2...1...GO!")
        print("Wow! So fast!")
        print(f"Time: {random.randint(10, 20)} seconds")
        time.sleep(6)


# Beauty Training
# User inputs items and it "dresses" the pet
def beauty_training():
    """
    beauty training for pet, dress the pet
    """
    print("You have chosen: Beauty Training! Here you will be required to dress up your pet!")
    time.sleep(3)
    pet_dress_hat = input("Type what type of hat do you want on your pet: ")
    pet_dress_outfit = input("Type what outfit do you want on your pet(one word): ")
    pet_dress_collar = input("Type what color collar do you want on your pet(one word): ")
    time.sleep(3)
    print(
        f"Wow! Your pet looks really nice with their {pet_dress_hat},{pet_dress_outfit}, "
        f"and their {pet_dress_collar} collar! ")
    time.sleep(3)


def framing_details():
    """
    adds visual details to program
    """
    print("+" * 100, "|" * 2, sep=' ', end='\n')  # Framing details for game, multiple +
    print("+" * 100, "|" * 2, sep=' ', end='\n')  # *100 prints the + 100 times on the line


# Math Quiz is used to train your pet.
# Calculator for Math Quiz
def add(n1, n2):
    """
    adds two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


def divide(n1, n2):
    """
    divides two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 / n2


def multiply(n1, n2):
    """
    multiples two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 * n2


def subtract(n1, n2):
    """
    subtracts two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 - n2


def power(n1, n2):
    """
    sets first number to the power of second number
    :param n1:
    :param n2:
    :return:
    """
    return n1 ** n2


def floor_divide(n1, n2):
    """
    uses floor division of second number on first
    :param n1:
    :param n2:
    :return:
    """
    return n1 // n2


def modulus(n1, n2):
    """
    gives remainder of first number divided by second number
    :param n1:
    :param n2:
    :return:
    """
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
    """
    math quiz used for math training, acts as a calculator
    """
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
        calculations = False


def training_screen_func(choice, pet_stat):
    """
    training screen for players choice of what training their pet will do
    :param choice:
    :param pet_stat:
    :return:
    """
    if choice == "math training":
        math_training()
        for key in pet_stat:
            if key == "smartness":
                pet_stat[key] += 6
        for key in pet_stat:
            if key == "stamina":
                pet_stat[key] -= 5
        print("Great job! Your pet has earned 6 smartness.")
        time.sleep(5)
        return pet_stats
    elif choice == "stamina training":
        stamina_training()
        for key in pet_stat:
            if key == "stamina":
                pet_stat[key] += 10
        print("Great job! Your pet has earned 10 stamina.")
        time.sleep(5)
        return pet_stats
    elif choice == "speed training":
        speedy = int(input("Before we begin, how many times do you want your pet to run around the track? Choose "
                           "between 1-5."))
        if speedy < 1 or speedy > 5:
            speedy = int(input("Please enter a valid number between 1-5."))
        speed_training(speedy)
        for key in pet_stat:
            if key == "stamina":
                pet_stat[key] -= 5
        for key in pet_stat:
            if key == "speed":
                pet_stat[key] += speedy * 2
        print("Great job!")
        time.sleep(3)
        return pet_stat

    elif choice == "beauty training":  # Repeat this structure with the other if statements
        beauty_training()
        for key in pet_stat:
            if key == "stamina":
                pet_stat[key] -= 5

        for key in pet_stat:
            if key == "beauty":
                pet_stat[key] += 3
        print("Nice job dressing up your pet!")
        time.sleep(3)
        return pet_stat


def main():
    """
    The entire game program
    """
    gold_medal = 0
    bronze_medal = 0
    silver_medal = 0
    # Intro into the game!
    game = True
    while game:

        print(logo)
        starting_choice = input("Start\n""About\n""How to Play\n""Choice:").lower()
        if starting_choice == "start":
            framing_details()
            game = False
            pre_olympic = True
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
            "So your name is " + player_name + " your pet is a " + pet_breed + " and their name is " + pet_name + "? "
                                                                                                                  "Y "
                                                                                                                  "or "
                                                                                                                  "N "
        ).lower()  # Concatenates variables and string
        if confirm_pet == "y":
            print("Great! Let's continue to the first week!")
            first_week = True
            framing_details()
            pre_olympic = False  # End of pre olympics
        if confirm_pet == "n":
            print("Let's try this again then!")
            time.sleep(3)
            framing_details()
            continue
    while first_week:  # First Week of Olympics
        time.sleep(3)
        print(
            f"Welcome to the first week {player_name} and {pet_name}!\nYou have 4 things you can train: math, stamina, "
            f"speed and beauty!\nYou have 20 stamina right now. Each training takes 5 stamina. Be sure to use it "
            f"wisely!\nThe olympic game this week is in math so be sure to train your pet's math skills!")
        time.sleep(10)
        first_week_train = True
        while first_week_train:  # Training Montage
            framing_details()
            if not pet_stats["stamina"] == 20 and not pet_stats["stamina"] < 20:
                print("Wow! Your pet has so much energy!")
            print("Pet stamina: " + str(pet_stats.get("stamina")) + " Pet smartness: " + str(
                pet_stats.get("smartness")) + " Pet speed: " + str(pet_stats.get("speed")) + " Pet beauty: " + str(
                pet_stats.get("beauty")))
            print(pet_choice)
            train_choice_1 = input("Math Training\nStamina Training\nSpeed Training\nBeauty Training\nChoice:").lower()
            if pet_stats["stamina"] == 0:
                print("Whoops! Not enough stamina! On to the first game! ")
                first_week_train = False
                first_week = False
                math_olympic = True

            else:
                framing_details()
                training_screen_func(train_choice_1, pet_stats)

    while math_olympic:  # Math Olympic Game
        framing_details()
        time.sleep(3)
        print(math_olympic_banner)
        time.sleep(3)
        print("Welcome to the Math Olympics Game! Here your pet will compete against 3 other pets!")
        rudy = random.randint(5, 45)
        maxie = random.randint(10, 35)
        scooby = random.randint(15, 50)
        quiz_pets = {  # Pets the user's pet is competing against
            rudy: "Rudy",
            maxie: "Maxie",
            scooby: "Scooby",
            pet_stats["smartness"]: pet_name,
        }
        math_winner = quiz_pets.get(max(quiz_pets))
        math_mega_loser = quiz_pets.get(min(quiz_pets))
        print("Time to compete!")
        time.sleep(5)
        print("These are really smart pets!")
        time.sleep(5)
        print("Whoops seems like someone made a mistake!")
        time.sleep(5)
        print("Wow! Look how quick they are answering these questions!")
        time.sleep(5)
        print("And the winner is...")
        time.sleep(3)
        print(math_winner)
        time.sleep(3)
        print("In last place is...")
        time.sleep(3)
        print(math_mega_loser)
        print("Thank you to all the pets for participating. We will see you next week for our race!")
        second_week = True
        math_olympic = False

    while second_week:  # Start of second week
        framing_details()
        time.sleep(3)
        pet_stats["stamina"] = 20
        print("Welcome back to second week training!")
        if math_mega_loser == pet_name:
            print("Well,your pet didnt do the best in the math olympics but they could always win the other games!")
            bronze_medal += 1
        if math_winner == pet_name:
            print("Wow, your pet won! That's incredible, keep up the great work!")
            gold_medal += 1
        else:
            print("Well, at least your pet was not in last place! Let's aim to do better next time!")
            silver_medal += 1
        print(
            "The next Olympic game is racing. You should focus on training your pet's speed so they can win the race!")
        time.sleep(10)
        second_week_train = True
        second_week = False
        while second_week_train:  # Second training montage
            framing_details()
            if not pet_stats["stamina"] == 20 and not pet_stats["stamina"] < 20:
                print("Wow! Your pet has so much energy!")
            print("Pet stamina: " + str(pet_stats.get("stamina")) + " Pet smartness: " + str(
                pet_stats.get("smartness")) + " Pet speed: " + str(pet_stats.get("speed")) + " Pet beauty: " + str(
                pet_stats.get("beauty")))
            print(pet_choice)
            train_choice_1 = input("Math Training\nStamina Training\nSpeed Training\nBeauty Training\nChoice:").lower()
            if pet_stats["stamina"] == 0:
                print("Whoops! Not enough stamina! On to the second game! ")
                second_week_train = False
                second_week = False
                race_olympic = True
            else:
                framing_details()
                training_screen_func(train_choice_1, pet_stats)
    while race_olympic:  # Racing Olympic Game
        framing_details()
        time.sleep(4)
        print(race_banner)
        print("Welcome to our race! Your pet will be competing against 2 other pets.")
        time.sleep(3)
        rudy = random.randint(10, 26)
        scooby = random.randint(20, 50)
        race_pets = {  # Pets the user's pet is competing against
            rudy: "Rudy",
            scooby: "Scooby",
            pet_stats["speed"]: pet_name,
        }
        race_winner = race_pets.get(max(race_pets))
        race_mega_loser = race_pets.get(min(race_pets))
        print("It is time to race!")
        time.sleep(4)
        print("On your marks...")
        time.sleep(5)
        print("Get set...")
        time.sleep(5)
        print("GO!!")
        print(pet_choice)
        print("WOW THEY ARE SO FAST, THIS IS INSANE!")
        time.sleep(5)
        print("THEY ARE ALL NECK AND NECK FOLKS! WHO IS GOING TO WIN?!?!")
        time.sleep(5)
        print("AND THEY PASSED THE FINISH LINE!")
        time.sleep(3)
        print(
            "What's that? I am being informed that the winner is being determined because they were too close to tell!")
        time.sleep(5)
        print("The results are in!")
        time.sleep(3)
        print("The winner is....")
        time.sleep(3)
        print(race_winner)
        time.sleep(2)
        print("In last place is...")
        time.sleep(2)
        print(race_mega_loser)
        print("Thank you all for competing! We will see you all at our last game, the beauty olympic!")
        framing_details()
        third_week = True
        race_olympic = False
    while third_week:
        time.sleep(5)
        pet_stats["stamina"] = 20
        print("Welcome back to the last week of training!")
        if race_mega_loser == pet_name:
            print("Well,your pet didnt do the best in the race but they could always win the other games!")
            bronze_medal += 1
        if race_winner == pet_name:
            print("Wow, your pet won! That's incredible, keep up the great work!")
            gold_medal += 1
        else:
            print("Well, at least your pet was not in last place! Let's aim to do better next time!")
            silver_medal += 1
        print(
            "The next Olympic game is beauty. You should focus on training your pet's beauty so they can win the "
            "contest!")
        time.sleep(10)
        third_week_train = True
        third_week = False
        while third_week_train:  # Second training montage
            framing_details()
            if not pet_stats["stamina"] == 20 and not pet_stats["stamina"] < 20:
                print("Wow! Your pet has so much energy!")
            print("Pet stamina: " + str(pet_stats.get("stamina")) + " Pet smartness: " + str(
                pet_stats.get("smartness")) + " Pet speed: " + str(pet_stats.get("speed")) + " Pet beauty: " + str(
                pet_stats.get("beauty")))
            print(pet_choice)
            train_choice_1 = input("Math Training\nStamina Training\nSpeed Training\nBeauty Training\nChoice:").lower()
            if pet_stats["stamina"] == 0:
                print("Whoops! Not enough stamina! On to the third game! ")
                third_week_train = False
                third_week = False
                beauty_contest = True
            else:
                framing_details()
                training_screen_func(train_choice_1, pet_stats)
    while beauty_contest:
        framing_details()
        time.sleep(4)
        print(beauty_banner)
        print("Welcome to our final game in the Pet Olympics!")
        time.sleep(3)
        print("Every one has done so amazing!")
        print("Keep up the energy for this last game!")
        time.sleep(5)
        print("Your pet will be competing against 2 other pets! Lets see which pet will win the beauty contest! ")
        kimmy = random.randint(3, 15)
        scooby = random.randint(3, 15)
        beauty_pets = {  # Pets the user's pet is competing against
            kimmy: "Kimmy",
            scooby: "Scooby",
            pet_stats["beauty"]: pet_name,
        }
        beauty_winner = beauty_pets.get(max(beauty_pets))
        beauty_mega_loser = beauty_pets.get(min(beauty_pets))
        print(pet_choice)
        time.sleep(3)
        print("Hygiene is good....")
        time.sleep(3)
        print("Really stylish outfit choice....")
        time.sleep(3)
        print("Super cute face...")
        time.sleep(3)
        print("The results are in!")
        time.sleep(3)
        print("The winner is...")
        time.sleep(3)
        print(beauty_winner)
        time.sleep(3)
        print("In last place is...")
        time.sleep(3)
        print(beauty_mega_loser)
        time.sleep(2)
        print("Thank you all for participating! I will see you in the last week to go over some things!")
        time.sleep(4)
        framing_details()
        end_game = True
        beauty_contest = False
    while end_game:  # Final Week, just a summary of the game
        if beauty_mega_loser == pet_name:
            bronze_medal += 1
        if beauty_winner == pet_name:
            gold_medal += 1
        else:
            silver_medal += 1
        print("Hey there! Great job in the olympics!\nI hope you and your pet had alot of fun!")
        time.sleep(5)
        print("Your pet ended up winning " + str(gold_medal) + " gold medals!")
        time.sleep(3)
        print("Your pet won " + str(silver_medal) + " silver medals!")
        time.sleep(3)
        print("Your pet also won " + str(bronze_medal) + " bronze medals!")
        time.sleep(3)
        print("Hopefully Ill see you again at the next Pet Olympics! Goodbye for now!")
        time.sleep(5)
        framing_details()
        print("Summary")  # Summary of pet wins and stats
        print("Gold medals: " + str(gold_medal))
        print("Silver medals: " + str(silver_medal))
        print("Bronze medals: " + str(bronze_medal))
        print("Pet smartness: " + str(pet_stats.get("smartness")) + " Pet speed: " + str(pet_stats.get("speed")) +
              " Pet beauty: " + str(pet_stats.get("beauty")))
        time.sleep(8)
        end_game = False


main()
