import random
import time
import story
import riddles
inventory = dict(moon_suit = False, nice_person = False, bottle = False, headphones = True, souvenir = False, photo = False)
speler_data = dict(name = "")
stories = story.story
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
def random_from_range(amount):
    chance = 1/amount
    random_number = random.random()
    j = 0
    for i in range(amount):
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
print("Travelling",end="",flush=True)

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
print("Travelling",end="",flush=True)

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
time.sleep(2)
friend_names = random_from_list(["Ben", "Jaap", "Klaas", "Jan", "Emily", "Rozanne", "Suzanne", "Annalies"])
if inventory["bottle"]:
    print(stories["someone_wants_drink"])
    inventory["bottle"] = False
    time.sleep(4)
else:
    print(stories["you_talk_to_someone"])
    time.sleep(3)
print("After hours of talking",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)

print(stories["landing_on_moon"])
time.sleep(3)

input_photo = ""
while input_photo != "y" and input_photo != "n":
    input_photo = input(f"Your friend says:\"Do you want to take a picture together?\" y/n: ")
    if input_photo == "y":
        inventory["photo"] = True
        time.sleep(2)
        print(stories["photo_taken"])
    elif input_photo == "n":
        print(stories["photo_not_taken"])
        time.sleep(2)

print(stories["take_train_to_camping"])
time.sleep(4)
if not inventory["souvenir"]:
    print("You go to the shop and buy a souvenir. ")
    inventory["souvenir"] = True
time.sleep(2)

souvenir_in_vault_input = ""
souvenir_in_vault = False
while souvenir_in_vault_input != "y" and souvenir_in_vault_input != "n":
    souvenir_in_vault_input = input("Do you want to stash your souvenir in the vault? y/n: ")
    if souvenir_in_vault_input == "y":
        souvenir_in_vault = True
        inventory["souvenir"] = False
        print("Your souvenir is safe in the vault")
    elif souvenir_in_vault_input == "n":
        print("Your souvenir is not safe with you. Be careful with it.")
vault_code = random_from_list(["7589", "3489", "3095", "2563", ""])
if souvenir_in_vault:
    print(f"Your vault code is {vault_code}. ") 


camping_place = random_from_list(["45", "98", "23", "67", "91"])
print(f"Your campingplace is place {camping_place}.")
time.sleep(2)
print("before you go to your campingplace, you have to solve a riddle. ")

guessed = False

riddle_index = random_from_range(len(riddles.riddles))
riddle = riddles.riddles[riddle_index]
answers = riddles.answers[riddle_index]

while not guessed:
    player_answer = input(riddle)
    for answer in answers:
        if player_answer.lower() == answer:
            print(f"Your are able to go to campingplace {camping_place}. ")
            guessed = True
        else:
            print("This answer is not correct. Try it again. ")
if souvenir_in_vault == False and random_chance(50):
    print(stories["souvenir2_gets_robbed"])
    inventory["souvenir"] = False
elif souvenir_in_vault == False and random_chance(50):
    print(stories["souvenir_breaks"])
    inventory["souvenir"] = False

print("One week later",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)

while inventory["souvenir"] == False:
    if souvenir_in_vault:
        player_input_vault_code = input("You are leaving the camping. Before you go, you want your souvenir back. \
Enter your vault code to get your souvenir back: ")
        if player_input_vault_code == vault_code:
            inventory["souvenir"] = True
            print("You have your souvenir back. ")
        else:
            print("The code is wrong. Try it again. ")
    
print(stories["go_to_spaceport_moon"])
