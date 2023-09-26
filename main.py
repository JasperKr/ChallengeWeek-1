import random
import time
inventory = dict(moon_suit = False, nice_person = False, bottle = False, headphones = True, souvenir = False, photo = False)
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad. There is a security guard. ",
    departure_earth = "you depart",
    arrival_spaceport = "You have arrived at a spaceport and you are going to the moon. \n\
You may have forgotten your moon suit at home, but you're not sure.  \n\
After looking around you can see a shoppingmall and what looks to be a pilot.\n\
You only have your suitcase and a pair of headphones.",
    approach_pilot_question = "Do you know where to buy a moon suit? I lost mine.",
    approach_pilot_with_moonsuit = "\"I have a spare moon suit that you can borrow. \"",
    pilot_has_no_extra_moonsuit = "\"you can buy a moon suit at the shoppingmall. Be sure that you have the good shop. \"",
    go_to_store = "You go to the shoppingmall.",
    at_the_stores = "When you are at the shoppingmall, you can choose from 3 stores: Albert Hein, H&M and the Gilgal. \
Which one do you want to go to?",
    Albert_Hein = "Did you also forget your orange juice?",
    H_M = "Nice suit for a fancy dress party.",
    Gilgal = "BIER!!!",
    buy_bottle = "Do you want to buy a bottle of Belgium wine? y/n: ",
    go_to_gate = "You have everything you need, so you head over to gate ",
    you_help_someone = "You walk to the person who fell and you help him. He thanks you for your help. ",
    you_do_not_help_someone = "You ignore him and you keep on walking.",
    arrival_spaceport_2 = "You arrived at the last spaceport before arriving at the moon. \n\
This place looks shadey. ",
    transfer_to_another_spaceship = "You have to wait another 8 hours before continuing your journey",
    ask_to_explore_the_station = "Do you want to explore the station and find out what's there or not? y/n: ",
    explore_the_station = "While exploring the station, you find a souvenirshop.",
    get_robbed = "After you've bought a souvenir, you want to return to the station. \n\
But while walking back, you see a man approaching you. \n\
After he sees you looking around, he runs towards you and ",
    nice_person_helps = "tries to rob you, he would have succeeded if not for the person you helped a while back.\n\
You lost nothing and return safely.",
    defend_with_bottle = "tries to rob you, he would have succeeded if not for that bottle you bought at Gilgal \n\
You use it to defend yourself from the attacker but barely get away, you lost the bottle.",
    get_robbed_without_help = "steals your headphones and souvenir",
    sleep_safely_at_station = "You find a safe place somewhere in the station and wake up right before the flight leaves, time to get ready."
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

go_anyways = False
if inventory["moon_suit"]:
    go_anyways = input("Do you want to go to the store anyways? y/n: ") == "y"
if not inventory["moon_suit"] or go_anyways: # if the player didn't find a moon suit in their suitcase

    # ask the player if they want to ask the pilot where to buy a moon suit
    if not go_anyways:
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
        if inventory["moon_suit"]:
            go_anyways = input("Do you want to go to the store anyways? y/n: ") == "y"
    if not inventory["moon_suit"] or go_anyways: #check if pilot gave you a moon suit, if not, go to the store.
        # buy a moon suit
        print(stories["go_to_store"])
        time.sleep(2)
        amount_visited = 0 # keep track of the stores the player has visited
        stores_visited = dict(Albert_Hein=False,H_M=False,Gilgal=False)
        stay = True
        # if the player hasn't found a moon suit yet.
        while not inventory["moon_suit"] or stay:
            if inventory["moon_suit"]:
                if input("do you want to leave, or continue shopping? leave/stay: ") == "leave":
                    stay = False
            if stay:
                user_store_input = input("To which store do you want to go: Albert Hein, H&M, Gilgal? ").title()
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
                        if store_selection == "Gilgal":
                            if input(stories["buy_bottle"]) == "y":
                                inventory["bottle"] = True
                                time.sleep(2)
                        if not inventory["moon_suit"]:
                            if random_chance(33) or amount_visited >= 3:
                                print("They had one more moon suit")
                                inventory["moon_suit"] = True
                            else:
                                print("The store doesn't have any moon suits")
                            time.sleep(2)
                    else:
                        print("You already went there!")
                        time.sleep(2)
                else:
                    print("You can't find that store!")
                    time.sleep(2)

# the player goes to a gate
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")
time.sleep(2)

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
time.sleep(2)
print("Before entering you have to show your passport to the customs.")
time.sleep(2)
print(f"\"Thank you, have a nice flight {speler_data['name']}!\"")
time.sleep(2)
print("You enter the spaceship. And you take a seat somewhere in the back.")
time.sleep(2)
if inventory["nice_person"]:
    print("You depart from the spaceship stop. While listening to some music, you also notice that the person you helped is here too.",end="\n\n")
else:
    print("You depart from the spaceship stop. While listening to some music",end="\n\n")
time.sleep(2)
print("travelling",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)
print(stories["arrival_spaceport_2"], end="\n\n")
time.sleep(5)
print(stories["transfer_to_another_spaceship"])
time.sleep(3)
if input(stories["ask_to_explore_the_station"]) == "y":
    time.sleep(2)
    print(stories["explore_the_station"])
    time.sleep(2)
    if input("Do you want to go to the shop? y/n: ") == "y":
        inventory["souvenir"] = True
    time.sleep(3)
    print()
    print(stories["get_robbed"],end="")
    time.sleep(2)
    if inventory["nice_person"]:
        print(stories["nice_person_helps"])
    elif inventory["bottle"]:
        print(stories["defend_with_bottle"])
        inventory["bottle"] = False
    else:
        print(stories["get_robbed_without_help"])
        inventory["headphones"] = False
        inventory["souvenir"] = False
    time.sleep(4)
    print(stories["sleep_safely_at_station"])
    time.sleep(2)
else:
    print(stories["stay_at_station"])
    if inventory["bottle"]:
        if input("Do you want to drink your bottle?") == "y":
            print(stories["drink_bottle"])
            inventory["bottle"] = False
        time.sleep(2)
        print(stories["pass_out_at_station"])
        inventory["headphones"] = False
        time.sleep(2)
        print(stories["headphones_stolen"])
        time.sleep(2)

print(stories["spaceship2_departs"])
if inventory["bottle"]:
    print(stories["someone_wants_drink"])
    inventory["bottle"] = False
else:
    print(stories["you_talk_to_someone"])

print(stories["landing_on_moon"])

input_photo = input("Your friend says:\"shall I take a picture of you?\" y/n: ")
if input_photo == "y":
    inventory["photo"] = True
    time.sleep(2)
    print(stories["photo_taken"])
elif input_photo == "n":
    print(inventory["photo_not_taken"])
    time.sleep(2)

print(stories["take_train_to_camping"])
time.sleep(4)
if inventory["souvenir"] == False:
    print("You go to the shop and buy a souvenir. ")
    inventory["souvenir"] = True
time.sleep(1)

souvenir_in_vault_input = input("Do you want to stash your souvenir in the vault? y/n: ")
if souvenir_in_vault_input == "y":
    souvenir_in_vault_input_bool = True
    print("Your souvenir is safe in the vault")
elif souvenir_in_vault_input == "n":
    souvenir_in_vault_input_bool = False
    print("Your souvenir is not safe in the vault. Be carefull with it.")   

