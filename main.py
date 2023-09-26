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
    pilot_has_no_extra_sunsuit = "\"you can buy a sunsuit at the shoppingmall. Be sure that you have the good shop. \"",
    go_to_store = "You go to the shoppingmall.",
    at_the_stores = "When you are at the shoppingmall, you can choose from 3 stores: Albert Hein, H&M and the Gilgal. \
Wich one do you want to choose?",
    AH = "Did you also forget your orange juice?",
    H_M = "Nice suit for a fancy dress party.",
    Gilgal = "BIER!!!",
    go_to_gate = "You have come to the gates. Now you need to take the right gate. ",
)
def random_chance(chance):
    return random.random() < (chance / 100)
def random_from_list(list):
    chance = 1/len(list)
    random_number = random.random()
    j = 0
    for i in list:
        j += chance
        if random_number > j - chance and random_number < j:
            return i
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
    if random_chance(25):
        print("You had your sun suit with you all along.",end="\n\n")
        inventory["sun_suit"] = True
    else:
        print("You forgot your sun suit.",end="\n\n")
time.sleep(2)
if not inventory["sun_suit"]:
    if input("Do you want to ask the pilot where to buy a sun suit, or, go to the store to buy one? pilot/store: ") == "pilot":
        print(stories["approach_pilot_question"]) # <---
        time.sleep(1)
        if random_chance(33):
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
        stores_visited = dict(Albert_Hein=False,H_M=False,Gilgal=False)
        while not inventory["sun_suit"]:
            store_selection = input("you have come to the shoppingmall. To wich store do you want to go: Albert Hein, H&M, Gilgal? ").title()
            if store_selection == "Albert Hein":
                stores_visited["Albert_Hein"] = True
            elif store_selection == "H&M":
                stores_visited["H_M"] = True
            elif store_selection == "Gilgal":
                stores_visited["Gilgal"] = True
        
            if not stores_visited[store_selection]:
                amount_visited += 1
                if random_chance(33) or amount_visited >= 3:
                    print("They had one more sunsuit")
                    inventory["sun_suit"] = True
                else:
                    print("The store doesn't have any sunsuits")
            else:
                print("You already went there!")

print(stories["go_to_gate"]) # <---
gate = random_from_list(["A", "B", "C", "E", "D", "F"])