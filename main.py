import random
import time
inventory = dict(sun_suit = False)
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad. There is a security guard. ",
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
    Albert_Hein = "Did you also forget your orange juice?",
    H_M = "Nice suit for a fancy dress party.",
    Gilgal = "BIER!!!",
    go_to_gate = "You have everything you need, so you head over to gate ",
    you_help_someone = "You walk to the person who fell and you help him. He thanks you for your help. ",
    you_do_not_help_someone = "You ignore him and you move on walking.",

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
print(stories["intro"]) # begin of the game, print the starting text
time.sleep(3)

name_correct = False  # wether the name you supplied is correct
first_time_asking = True # is this the first time the security gaurd is asking you

while not name_correct: # while your name is not correctly input, keep asking
    if first_time_asking:
        speler_data["name"] = input("\"Hey! You have to check in first! What's your name?\" ")
    else:
        speler_data["name"] = input("\"Can you say that again?\" ")
    first_time_asking = False
    name_correct = input(f"So, {speler_data['name']}? y/n: ") == "y"

print(stories["departure_earth"],end="\n\n") # print text to leave earth and add two new lines
print("travelling",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)
print(stories["arrival_spaceport"],end="\n\n")
time.sleep(5)

# ask the player if they want to check their suitcase for a sun suit (15% chance it is there)
if input("Do you want to check your suitcase first? y/n: ") == "y":
    time.sleep(2)
    if random_chance(15):
        print("You had your sun suit with you all along.",end="\n\n")
        inventory["sun_suit"] = True # keep track of if the player has a sun suit
    else:
        print("You forgot your sun suit.",end="\n\n")

time.sleep(2)

if not inventory["sun_suit"]: # if the player didn't find a sun suit in their suitcase

    # ask the player if they want to ask the pilot where to buy a sun suit
    if input("Do you want to ask the pilot where to buy a sun suit, or, go to the store to buy one? pilot/store: ") == "pilot":

        print(stories["approach_pilot_question"]) # pilot storyline
        time.sleep(1)

        if random_chance(33):
            # tell the player the pilot has a sun suit for them and add it to their inventory.
            print(stories["approach_pilot_with_sunsuit"])
            time.sleep(2)
            inventory["sun_suit"] = True
        else:
            # tell the player where to buy a sun suit.
            print(stories["pilot_has_no_extra_sunsuit"])
            time.sleep(2)
    if not inventory["sun_suit"]: #check if pilot gave you a sun suit, if not, go to the store.
        # buy a sun suit
        print(stories["go_to_store"])
        time.sleep(2)
        amount_visited = 0 # keep track of the stores the player has visited
        stores_visited = dict(Albert_Hein=False,H_M=False,Gilgal=False)
        # if the player hasn't found a sunsuit yet.
        while not inventory["sun_suit"]:
            user_store_input = input("you have come to the shoppingmall. To which store do you want to go: Albert Hein, H&M, Gilgal? ").title()
            # the user input, Albert Hein, H&M, Gilgal or something invalid
            store_selection = ""

            # replace the text with the names that match the dictionary
            if user_store_input == "Albert Hein":
                store_selection = "Albert_Hein"
            elif user_store_input == "H&M":
                store_selection = "H_M"
            elif user_store_input == "Gilgal":
                store_selection = "Gilgal"
            
            # if that store exists
            if store_selection in stores_visited:
                # if the player hasn't gone to that store before
                if not stores_visited[store_selection]:
                    # storey
                    time.sleep(1)
                    print("You head over to "+user_store_input+"\n")
                    time.sleep(1)
                    print(stories[store_selection])
                    time.sleep(2)
                    stores_visited[store_selection] = True
                    amount_visited += 1
                    # 33% chance per store to have a sun suit, or, you checked two stores before this so it doesn't lock up the game.
                    if random_chance(33) or amount_visited >= 3:
                        print("They had one more sunsuit")
                        inventory["sun_suit"] = True
                    else:
                        print("The store doesn't have any sunsuits")
                else:
                    print("You already went there!")
            else:
                print("You can't find that store!")

# the player goes to a gate
print(stories["go_to_gate"]+random_from_list(["A", "B", "C", "E", "D", "F"])+".")

someone_falls = input("You see someone fall on your way to the gate, but you have haste. Will you help them? y/n: ")
if someone_falls == "y":
    print(stories["you_help_someone"])
elif someone_falls == "n":
    print(stories["you_do_not_help_someone"])
