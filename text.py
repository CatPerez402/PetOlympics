__author__ = "Catalina Perez"
logo = '''
   ___      __    ____  __                _       
  / _ \___ / /_  / __ \/ /_ ____ _  ___  (_)______
 / ___/ -_) __/ / /_/ / / // /  ' \/ _ \/ / __(_-<
/_/   \__/\__/  \____/_/\_, /_/_/_/ .__/_/\__/___/
                       /___/     /_/              
'''

game_sum = "Welcome to the Pet Olympics! The object of the game is simple. You will be given a pet that you\n""have " \
           "to  train. There are three olympic games your pet will compete in: math, racing, and beauty.\n""Each week " \
           "you will be given an amount of stamina to train your pet in different games. Be sure to\n""use your " \
           "stamina wisely or it can cost you the gold! "

game_rules = "There are 3 weeks in total. Every week, your pet will compete in one of the games. It's your job to\n" \
             "make sure they are properly trained. You will be given certain options to pick from each week. These\n" \
             "options include: math training, stamina training, speed training, and beauty school. You only have a\n" \
             "certain amount of stamina to train your pet. "

pet_list = "cat\ndog\nbird\nhorse"
# All art from ASCII Art Archive
pet = {
    "cat": '''  /\_/\  (
 ( ^.^ ) _)
   \"/  (
 ( | | )
(__d b__)''',
    "dog": """    __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/  """,
    "bird": '''   (
  `-`-.
  '( @ >
   _) (
  /    )
 /_,'  / 
   \  / 
===m""m===''',
    "horse": '''       ,--,
  _ ___/ /\|
 ;( )__, )
; //   '--;
  \     |
   ^    ^''',

}
math_olympic_banner = """  /  |/  /__ _/ /_/ /    / __ \/ /_ ____ _  ___  (_)______
 / /|_/ / _ `/ __/ _ \  / /_/ / / // /  ' \/ _ \/ / __(_-<
/_/  /_/\_,_/\__/_//_/  \____/_/\_, /_/_/_/ .__/_/\__/___/
                               /___/     /_/              """
race_banner = """   ___           _             ____  __                _       
  / _ \___ _____(_)__  ___ _  / __ \/ /_ ____ _  ___  (_)______
 / , _/ _ `/ __/ / _ \/ _ `/ / /_/ / / // /  ' \/ _ \/ / __(_-<
/_/|_|\_,_/\__/_/_//_/\_, /  \____/_/\_, /_/_/_/ .__/_/\__/___/
                     /___/          /___/     /_/              """
beauty_banner = """   ___                __         ____  __                _       
  / _ )___ ___ ___ __/ /___ __  / __ \/ /_ ____ _  ___  (_)______
 / _  / -_) _ `/ // / __/ // / / /_/ / / // /  ' \/ _ \/ / __(_-<
/____/\__/\_,_/\_,_/\__/\_, /  \____/_/\_, /_/_/_/ .__/_/\__/___/
                       /___/          /___/     /_/              """

# print(f"Pet stamina: {stamina}  Pet smartness: {smartness}  Pet speed: {speed}  Pet beauty: {beauty}")
#     print(pet_choice)
#     train_choice_1 = input("Math Training\nStamina Training\nSpeed Training\nBeauty Training\nChoice:").lower()
#     if stamina == 0:
#         print("Whoops! Not enough stamina! On to the first game! ")
#         first_week_train = False
#         first_week = False
#         math_olympic = True
#     elif train_choice_1 == "math training":
#         math_training()
#         smartness += 6
#         stamina -= 5
#         print("Great job! Your pet has earned 6 smartness.")
#         print(f"This brings {pet_name} to {smartness} smartness!")
#         time.sleep(5)
#     elif train_choice_1 == "stamina training":
#         stamina_training()
#         stamina += 10
#         print("Great job! Your pet has earned 10 stamina.")
#         print(f"This brings {pet_name} to {stamina} stamina!")
#         time.sleep(5)
#     elif train_choice_1 == "speed training":
#         speedy = int(input("Before we begin, how many times do you want your pet to run around the track? Choose "
#                            "between 1-5."))
#         if speedy < 1 or speedy > 5:
#             speedy = int(input("Please enter a valid number between 1-5."))
#         speed_training(speedy, pet_choice)
#         speed += speedy * 2
#         print("Great job!")
#         print(f"This brings {pet_name} to {speed} speed!")
#     elif train_choice_1 == "beauty training":
#         beauty_training()
#         beauty += 3
#         print("Nice job dressing up your pet!")
#         print(f"This bring {pet_name} to {beauty} beauty!")