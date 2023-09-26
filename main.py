import random
import time
inventory = dict(moon_suit = False, nice_person = False)
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad. There is a security guard. ",
    departure_earth = "you depart",
    arrival_spaceport = "You have landed on a spaceport and you are going to the moon. \n\
The last thing you have to get is somewhere at the spaceport.\n\
You may have forgotten your moon suit at home, but you're not sure.  \n\
After looking around you can see a shoppingmall and what looks to be a pilot.\n\
You only have your suitcase.",
    approach_pilot_question = "Do you know where to buy a moon suit? I lost mine.",
    approach_pilot_with_moonsuit = "\"I have a spare moon suit that you can borrow. \"",
    pilot_has_no_extra_moonsuit = "\"you can buy a moon suit at the shoppingmall. Be sure that you have the good shop. \"",
    go_to_store = "You go to the shoppingmall.",
    at_the_stores = "When you are at the shoppingmall, you can choose from 3 stores: Albert Hein, H&M and the Gilgal. \
Which one do you want to go to?",
    Albert_Hein = "Did you also forget your orange juice?",
    H_M = "Nice suit for a fancy dress party.",
    Gilgal = "BIER!!!",
    go_to_gate = "You have everything you need, so you head over to gate ",
    you_help_someone = "You walk to the person who fell and you help him. He thanks you for your help. ",
    you_do_not_help_someone = "You ignore him and you keep on walking.",

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

# ask the player if they want to check their suitcase for a moon suit (15% chance it is there)
if input("Do you want to check your suitcase first? y/n: ") == "y":
    time.sleep(2)
    if random_chance(15):
        print("You had your moon suit with you all along.",end="\n\n")
        inventory["moon_suit"] = True # keep track of if the player has a moon suit
    else:
        print("You forgot your moon suit.",end="\n\n")

time.sleep(2)

if not inventory["moon_suit"]: # if the player didn't find a moon suit in their suitcase

    # ask the player if they want to ask the pilot where to buy a moon suit
    if input("Do you want to ask the pilot where to buy a moon suit, or, go to the store to buy one? pilot/store: ") == "pilot":

        print(stories["approach_pilot_question"]) # pilot storyline
        time.sleep(1)

        if random_chance(33):
            # tell the player the pilot has a moon suit for them and add it to their inventory.
            print(stories["approach_pilot_with_moonsuit"])
            time.sleep(2)
            inventory["moon_suit"] = True
        else:
            # tell the player where to buy a moon suit.
            print(stories["pilot_has_no_extra_moonsuit"])
            time.sleep(2)
    if not inventory["moon_suit"]: #check if pilot gave you a moon suit, if not, go to the store.
        # buy a moon suit
        print(stories["go_to_store"])
        time.sleep(2)
        amount_visited = 0 # keep track of the stores the player has visited
        stores_visited = dict(Albert_Hein=False,H_M=False,Gilgal=False)
        # if the player hasn't found a moon suit yet.
        while not inventory["moon_suit"]:
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
                    # 33% chance per store to have a moon suit, or, you checked two stores before this so it doesn't lock up the game.
                    if random_chance(33) or amount_visited >= 3:
                        print("They had one more moon suit")
                        inventory["moon_suit"] = True
                    else:
                        print("The store doesn't have any moon suits")
                else:
                    print("You already went there!")
            else:
                print("You can't find that store!")

# the player goes to a gate
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")

# does the player help someone
someone_falls = input("You see someone fall on your way to the gate, but you're in a hurry. Will you still help them? y/n: ")
time.sleep(3)
if someone_falls == "y":
    print(stories["you_help_someone"])
    time.sleep(3)
    inventory["nice_person"] = True
elif someone_falls == "n":
    print(stories["you_do_not_help_someone"])
    time.sleep(3)

# the player leaves the spaceport.
print(f"You arrive at gate {gate}.",end="\n\n")
time.sleep(1)
print("Before entering you have to show your passport to the customs.")
time.sleep(2)
print(f"\"Thank you, have a nice flight {speler_data['name']}!\"")

