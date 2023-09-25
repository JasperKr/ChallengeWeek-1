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
time.sleep(3)
name_correct = False
first_time_asking = True
while not name_correct:
    if first_time_asking:
        speler_data["name"] = input("\"Hey! You have to check in first! What's your name?\" ")
    else:
        speler_data["name"] = input("\"Can you say that again?\" ")
    first_time_asking = False
    name_correct = input(f"So, {speler_data['name']}? y/n: ") == "y"
print(stories["departure_earth"],end="\n\n")
print("travelling: ",end="",flush=True)
for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)
print(stories["arrival_spaceport"],end="\n\n")
time.sleep(5)
if input("Do you want to check your suitcase first? y/n: ") == "y":
    time.sleep(2)
    if randomChance(25):
        print("You had your sun suit with you all along.",end="\n\n")
        inventory["sun_suit"] = True
    else:
        print("You forgot your sun suit.",end="\n\n")
time.sleep(2)
if not inventory["sun_suit"]:
    if input("Do you want to ask the pilot where to buy a sun suit, or, go to the store to buy one? pilot/store: ") == "pilot":
        print(stories["approach_pilot"])
        time.sleep(1)
        if randomChance(33):
            print()
            time.sleep(2)
            inventory["sun_suit"] = True
        else:
            print(stories["pilot_has_no_extra_sunsuit"])
            time.sleep(2)
    if not inventory["sun_suit"]: #check if pilot gave you a sun suit, if not, go to the store.
        # buy a sun suit
        print(stories["buy_a_sunsuit"])
        time.sleep(2)
print(stories["go_to_gate_A"])