import random
import time
inventory = dict(sun_suit = False)
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad and you need to check in. There is a security guard. ",
    departure_earth = "you depart",
    arrival_spaceport = "You have landed on a spaceport and you are going to the sun. \n\
The last thing you have to get is somewhere at the spaceport.\n\
You may have to get a sun suit. You may have forgotten it at home. \n\
After looking around you can see a shoppingmall and what looks to be a pilot.\n\
You only have your suitcase.",
    approach_pilot_question = "Do you know where to buy a sun suit? I lost mine.",
    approach_pilot_with_sunsuit = "\"I have a spare sun suit that you can borrow. \"",
    pilot_has_no_extra_sunsuit = "\"you can buy a sunsuit at the shoppingmall. Be sure that you have the good shop. \""
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
print("travelling",end="",flush=True)
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
        print(stories["approach_pilot_question"]) # <---
        time.sleep(1)
        if randomChance(33):
            print(stories["approach_pilot_with_sunsuit"]) # <---
            time.sleep(2)
            inventory["sun_suit"] = True
        else:
            print(stories["pilot_has_no_extra_sunsuit"])
            time.sleep(2)
    if not inventory["sun_suit"]: #check if pilot gave you a sun suit, if not, go to the store.
        # buy a sun suit
        #print(stories["go_to_store"]) # <---
        print("You go to the store.") # temporary
        time.sleep(2)
        amount_visited = 0
        stores_visited = dict(X=False,Y=False,Z=False)
        while not inventory["sun_suit"]:
            store_selection = input("What store will you go to? X/Y/Z: ").title()
            if not stores_visited[store_selection]:
                amount_visited += 1
                stores_visited[store_selection] = True
                if randomChance(25) or amount_visited >= 3:
                    print("They had one more sunsuit")
                    inventory["sun_suit"] = True
                else:
                    print("The store doesn't have any sunsuits")
            else:
                print("You already went there!")

print(stories["go_to_gate_A"]) # <---