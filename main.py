import random
import time
inventory = dict(sun_suit = False)
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad and you need to check in. There is a security guard. ",
    departure_earth = "you depart",
    arrival_spaceport = "You have landed on a spaceport and you are going to the sun. \n\
The last thing you have to get is somewhere at the spaceport.\n\
You have to get a sun suit. \n\
There is a shoppingmall, a pilot walking around and you have a suitcase with you. "
)
def randomChance(chance):
    return random.random() < (chance / 100)
print(stories["intro"]) # begin het spel, print het begin verhaal text
name_correct = False
first_time_asking = True
while not name_correct:
    if first_time_asking:
        speler_data["name"] = input("\"Hey! What's your name?\" ")
    else:
        speler_data["name"] = input("\"Can you say that again?\" ")
    first_time_asking = False
    name_correct = input(f"So, {speler_data['name']}? y/n: ") == "y"
print(stories["departure_earth"])
print("travelling: ",end="",flush=True)
for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n" or ""),flush=True)
print(stories["arrival_spaceport"])
if input("Do you want to check your suitcase first? y/n: ") == "y":
    if randomChance(50):
        print("You had your sun suit with all along.")
        inventory["sun_suit"] = True
    else:
        print("You forgot your sun suit.")
if not inventory["sun_suit"]:
    if input("Do you want to ask the pilot where to buy a sun suit, or, go to the store to buy one? pilot/store: ") == "pilot":
        print(stories["approach_pilot"])
        if randomChance(33):
            print()
            inventory["sun_suit"] = True
        else:
            print(stories["pilot_has_no_extra_sunsuit"])
    if not inventory["sun_suit"]: #check if pilot gave you a sun suit, if not, go to the store.
        # buy a sun suit

