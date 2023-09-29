import random
import time
import story
import story_2
import riddles
import images
inventory = dict(moon_suit = False, nice_person = False, bottle = False, headphones = True, souvenir = False, photo = False, friend = False, soup = 0, oxygen = False, sandwich = 0, fruit = 0, mars_sand = False, orange_juice = False, fish_fingers_or_tompouce_or_broccoli = 0, bread = False, cookies = False, starbucks = False)
speler_data = dict(name = "")
stories = story.story
stories_2 = story_2.story_2
command_line_colors = dict(
    red = '\033[91m',
    white = '\033[0;0m',
    yellow = '\033[93m',
    green = '\033[92m',
)
def color(text, rgb):
    return "\033[38;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )
def draw_image(image):
    for y in range(image[0]):
        # draw the numbers for the y axis
        for x in range(image[1]):
            print(color("██",image[y+2][x]),end="",flush=True)
        print()
    print(command_line_colors["white"])
def draw_image_with_ship(image,sx,sy):
    for y in range(image[0]):
        # draw the numbers for the y axis
        for x in range(image[1]):
            if x == sx and y == sy:
                print(color("██",[255,0,0]),end="",flush=True)
            else:
                print(color("██",image[y+2][x]),end="",flush=True)
        print()
    print(command_line_colors["white"])
# create a list for the asteroids
# set the player position

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
def find_similarity(string: str, other: str):
    similarity = 0.0
    if len(string) > 0:
        i = 0
        for character in string:
            if len(other)-1 >= i:
                if character == other[i]:
                    similarity += 1
                else:
                    if character == other[(i+1)%len(other)] and string[(i+1)%len(string)] != other[(i+1)%len(other)]:
                        similarity += 0.25
                    if character == other[(i-1)] and string[(i-1)] != other[(i-1)]:
                        similarity += 0.25
            i += 1
        similarity /= i
    return similarity
def mix(v,w,i):
    return (1-i)*v+w*i
def travel_to_place_on_image(image,start,to,printDelay,amount):
    for i in range(amount):
        current_time = i / (amount-1)
        position = [round(mix(start[0],to[0],current_time)),round(mix(start[1],to[1],current_time))]
        draw_image_with_ship(image,position[0],position[1])
        time.sleep(printDelay)
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
print("Travelling",flush=True)
travel_to_place_on_image(images.images["earth_to_moon"],[11,12],[11,8],1.5,5)
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
        player_answer = ""
        while player_answer != "pilot" and player_answer != "store":
            player_answer = input("Do you want to ask the pilot where to buy a moon suit, or, go to the store to buy one? pilot/store: ")
            if player_answer == "pilot":

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
        first_visit = True
        # if the player hasn't found a moon suit yet.
        while not inventory["moon_suit"] or stay:
            if inventory["moon_suit"] and not first_visit:
                if input("do you want to leave, or continue shopping? leave/stay: ") == "leave":
                    stay = False
            first_visit = False
            if stay:
                user_store_input = input("To which store do you want to go: Albert Hein, H&M, Gilgal? ").title()
                # the user input, Albert Hein, H&M, Gilgal or something invalid
                store_selection = ""

                # replace the text with the names that match the dictionary
                if user_store_input == "Albert Hein":
                    store_selection = "Albert_Hein"
                    inventory["orange_juice"] = True
                elif user_store_input == "H&M":
                    store_selection = "H_M"
                    inventory["orange_juice"] = True
                elif user_store_input == "Gilgal":
                    store_selection = "Gilgal"
                    inventory["orange_juice"] = True
                
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
print("You enter the spaceship and take a seat somewhere in the back.")
time.sleep(2)
if inventory["nice_person"]:
    print("You depart from the spaceport. While listening to some music and drinking your juice, you also notice that the person you helped is here too.",end="\n\n")
    inventory["orange_juice"] = False
else:
    print("You depart from the spaceport. While listening to some music",end="\n\n")
    inventory["orange_juice"] = False
time.sleep(2)
print("Travelling",flush=True)

travel_to_place_on_image(images.images["earth_to_moon"],[11,8],[8,1],0.75,10)
print(stories["arrival_spaceport_2"], end="\n\n")
time.sleep(5)
print(stories["transfer_to_another_spaceship"])
time.sleep(3)
player_answer = ""
while player_answer != "n" and player_answer != "y":
    player_answer = input(stories["ask_to_explore_the_station"])
    if player_answer == "y":
        time.sleep(2)
        print(stories["explore_the_station"])
        time.sleep(2)
        if input("Do you want to go to the shop? y/n: ") == "y":
            inventory["souvenir"] = True
        time.sleep(3)
        print("You also bought yourself a bread, when looking around. You noticed that you are hungry.")
        inventory["bread"] = True
        time.sleep(2)
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
    elif player_answer == "n":
        print(stories["stay_at_station"])
        time.sleep(2)
        if inventory["bottle"]:
            if input("Do you want to drink your bottle alone?") == "y":
                print(stories["drink_bottle"])
                inventory["bottle"] = False
            time.sleep(2)
        print(stories["pass_out_at_station"])
        inventory["headphones"] = False
        time.sleep(2)
        print(stories["headphones_stolen"])
        inventory["bread"] = True
        time.sleep(2)
    else:
        print("what did you say?")

print(stories["spaceship2_departs"])
inventory["bread"] = False
time.sleep(2)
friend_names = random_from_list(["Ben", "Jaap", "Klaas", "Jan", "Emily", "Rozanne", "Suzanne", "Annalies"])
if inventory["bottle"]:
    print(stories["someone_wants_drink"])
    inventory["bottle"] = False
    inventory["friend"] = True
    time.sleep(4)
else:
    print(stories["you_talk_to_someone"])
    inventory["friend"]
    time.sleep(3)
print("After hours of talking",flush=True)
travel_to_place_on_image(images.images["moon_station_to_moon"],[11,3],[15,17],0.5,16)

print(stories["landing_on_moon"])
time.sleep(3)

player_answer = ""
while player_answer != "y" and player_answer != "n":
    player_answer = input(f"{friend_names} says: \"Do you want to take a picture together?\" y/n: ")
    if player_answer == "y":
        inventory["photo"] = True
        time.sleep(2)
        print(stories["photo_taken"])
        draw_image(images.images["picture_from_friend"])
    elif player_answer == "n":
        print(stories["photo_not_taken"])
        time.sleep(2)

print(stories["take_train_to_camping"])
time.sleep(4)
if not inventory["souvenir"]:
    print("You go to the shop and buy a souvenir. ")
    inventory["souvenir"] = True
time.sleep(2)

player_answer = ""
souvenir_in_vault = False
while player_answer != "y" and player_answer != "n":
    player_answer = input("Do you want to stash your souvenir in the vault? y/n: ")
    if player_answer == "y":
        souvenir_in_vault = True
        inventory["souvenir"] = False
        print("Your souvenir is safe in the vault")
    elif player_answer == "n":
        print("Your souvenir is not safe with you. Be careful with it.")
vault_code = ""
for i in range(4):
    vault_code += str(random.randint(0,9))
if souvenir_in_vault:
    print(f"Your vault code is {vault_code}. ") 


camping_place = random_from_list(["45", "98", "23", "67", "91"])
print(f"You have to go to camping place {camping_place}.")
time.sleep(2)
print("But, before you go to your campingplace, you have to solve a riddle. ")

guessed = False

riddle_index = random_from_range(len(riddles.riddles))
riddle = riddles.riddles[riddle_index]
answers = riddles.answers[riddle_index]

while not guessed:
    player_answer = input(riddle)
    for answer in answers:
        if not guessed:
            if player_answer.lower() == answer:
                print(f"Your are able to go to campingplace {camping_place}. \n")
                guessed = True
    if not guessed:
        print("This answer is not correct. Try it again. \n")
if souvenir_in_vault == False and random_chance(50):
    print(stories["souvenir2_gets_robbed"] + "\n")
    inventory["souvenir"] = False
elif souvenir_in_vault == False and random_chance(50):
    print(stories["souvenir_breaks"] + "\n")
    inventory["souvenir"] = False

print("One week later",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)

while inventory["souvenir"] == False:
    if souvenir_in_vault:
        player_input_vault_code = input("You are leaving the camping. Before you go, you want your souvenir back. \n\
Enter your vault code to get your souvenir back: ")
        if player_input_vault_code == vault_code:
            inventory["souvenir"] = True
            print("\nYou have your souvenir back. ")
        else:
            print("\nThe code is wrong. Try it again. \n")
time.sleep(2)
print("Before leaving the camping, you bought some cookies to eat on your way to saturn. ")
inventory["cookies"] = True
time.sleep(2)
print(stories["go_to_spaceport_moon"])
time.sleep(2)
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")
time.sleep(2)
print(f"You arrive at gate {gate}.",end="\n\n")
time.sleep(2)
print("Before entering you have to show your passport to the customs.")
time.sleep(2)
print(f"\"Thank you, have a nice flight {speler_data['name']}!\"")
time.sleep(2)

print(stories["leave_the_moon"])
inventory["cookies"] = False
time.sleep(3)

print("travelling",flush=True)

travel_to_place_on_image(images.images["moon_station_to_moon"],[15,17],[11,3],0.5,16)

choice = input("Do you want to go to saturn first or straight back home? saturn/home: ")
time.sleep(2)
print(stories["announcement_flight_cancelled"])
if choice == "home":
    print(stories["go_to_saturn_anyways"])
time.sleep(2)
print(stories["get_starbucks"])
inventory["starbucks"] = True
time.sleep(2)
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")
time.sleep(2)
print(f"You arrive at gate {gate}.",end="\n\n")
time.sleep(2)
print("Before entering you have to show your passport to the customs.")
time.sleep(2)
print(f"\"Thank you, have a nice flight {speler_data['name']}!\"")
time.sleep(2)
print("You enter the spaceship and take a seat by the window and there you drink your starbucks. ")
inventory["starbucks"] = False

print("Travelling",flush=True)

travel_to_place_on_image(images.images["moon_to_saturn"],[0,6],[12,2],0.5,12)

print(stories["arrival_spaceport_saturn"])
time.sleep(4)
draw_image(images.images["saturn_station"])
time.sleep(4)
print(stories["go_to_places_saturn"])
time.sleep(2)
player_answer = ""
while player_answer != "hotel":
    player_answer = input("What do you want to do? Go to the shop, Take a walk or go back to the hotel and sleep. shop/walk/hotel: ")
    time.sleep(2)
    if find_similarity(player_answer,"shop") >= 0.75:
        print(stories["go_to_shop_saturn"])
        time.sleep(2)
        player_shop_answer = ""
        while player_shop_answer != "leave":
            player_shop_answer = input("What do you want to buy? They have sandwiches, canned soup and a lot of it and fruit. sandwich/soup/fruit/leave: ")
            time.sleep(2)
            if find_similarity(player_shop_answer,"sandwich") >= 0.75:
                inventory["sandwich"] += 1
                print("You take a nice sandwich for tomorrow.\n")
                if inventory["sandwich"] == 2:
                    time.sleep(2)
                    print("do you really need multiple?")
                if inventory["sandwich"] > 3:
                    time.sleep(2)
                    print("This is insanity!")
            elif find_similarity(player_shop_answer,"soup") >= 0.75:
                inventory["soup"] += 1
                print("You take some soup for tonight.\n")
                if inventory["soup"] == 2:
                    time.sleep(2)
                    print("do you really need multiple?")
                if inventory["soup"] > 3:
                    time.sleep(2)
                    print("This is insanity!")
            elif find_similarity(player_shop_answer,"fruit") >= 0.75:
                inventory["fruit"] += 1
                print("You take some fruit with you, an apple a day keeps the doctor away!\n")
                if inventory["fruit"] == 2:
                    time.sleep(2)
                    print("do you really need multiple?")
                if inventory["fruit"] > 3:
                    time.sleep(2)
                    print("This is insanity!")
            elif find_similarity(player_shop_answer,"leave") >= 0.75:
                inventory["oxygen"] = True
                print("You decide to leave the shop, but not without taking some extra oxygen bottles with you, never know when they will come in handy.\n")
            else:
                print("They don't have that here")
            time.sleep(2)


    elif find_similarity(player_answer,"walk") >= 0.75:
        print(stories["walk_around_saturn_refinery"])
        time.sleep(3)
    elif find_similarity(player_answer,"hotel") >= 0.75:
        print(stories["go_back_to_hotel_saturn_refinery"])
        time.sleep(2)
    else:
        print("you looked around, but couldn't find that.")
        time.sleep(2)

time.sleep(3)
print(command_line_colors["red"]+stories["saturn_refinery_disaster"])
time.sleep(8)
print(stories["saturn_refinery_main_story"])
time.sleep(6)
print(stories["evacuate_saturn_refinery"])
time.sleep(6)

print(command_line_colors["white"])
print(stories["crash_with_asteroids"])

gameover = False
Dead = False
first_time = True
while Dead or first_time:
    poging = 0
    oxygen_repaired = False
    engine_repaired = False
    people_calmed_down = False
    first_time = False
    while (oxygen_repaired == False or engine_repaired == False or people_calmed_down == False) and gameover == False:
        choice_asteroids = input(stories["story_choice_asteroids"]+"\n\n")

        poging += 1
        if poging > 3:
            gameover = True
        else:
            if poging == 1 and choice_asteroids != "hull":
                print("You ran out of oxygen and died. \n")
                time.sleep(1)
                poging = 0
            elif poging == 1 and choice_asteroids == "hull":
                oxygen_repaired = True
                print("You have repaired the hull. \n\
What do you want to repair now? \n")
                if inventory["sandwich"] >= 1:
                    inventory["sandwich"] -= 1
                elif inventory["soup"] >= 1:
                    inventory["soup"] -= 1
                elif inventory["fruit"] >= 1:
                    inventory["fruit"] -= 1
                time.sleep(1)
            else:
                if choice_asteroids == "hull":
                    oxygen_repaired = True
                    if poging != 3: # laatste keer kan je niks meer repareren
                        print("You have repaired the hull. \n\
What do you want to repair now? \n")
                        if inventory["sandwich"] >= 1:
                            inventory["sandwich"] -= 1
                        elif inventory["soup"] >= 1:
                            inventory["soup"] -= 1
                        elif inventory["fruit"] >= 1:
                            inventory["fruit"] -= 1
                        time.sleep(1)
                    elif poging != 3 and oxygen_repaired and people_calmed_down and engine_repaired:
                        print("You repaired the hull and you solved everything. Congratulations. The ship can move on. \n")
                        
                        time.sleep(1)
                elif choice_asteroids == "repair engine":
                    engine_repaired = True
                    if poging != 3: # laatste keer kan je niks meer repareren
                        print("You have repaired the engine of the ship. \n\
What do you want to repair now? \n")
                        if inventory["soup"] >= 1:
                            inventory["soup"] -= 1
                        elif inventory["sandwich"] >= 1:
                            inventory["sandwich"] -= 1
                        elif inventory["fruit"] >= 1:
                            inventory["fruit"] -= 1
                        time.sleep(1)
                    elif poging != 3 and oxygen_repaired and people_calmed_down and engine_repaired:
                        print("You repaird the engine and you solved everything. Congratulations. The ship can move on. \n")
                        if inventory["soup"] >= 1:
                            inventory["soup"] -= 1
                        elif inventory["sandwich"] >= 1:
                            inventory["sandwich"] -= 1
                        elif inventory["fruit"] >= 1:
                            inventory["fruit"] -= 1
                        time.sleep(1)
                elif choice_asteroids == "calm down":
                    people_calmed_down = True
                    if poging != 3: # laatste keer kan je niks meer repareren
                        print("You calmed down the people. \n\
What do you want to repair now? \n\n")
                        if inventory["fruit"] >= 1:
                            inventory["fruit"] -= 1
                        elif inventory["soup"] >= 1:
                            inventory["soup"] -= 1
                        elif inventory["sandwich"] >= 1:
                            inventory["sandwich"] -= 1
                        time.sleep(1)
                    elif poging != 3 and oxygen_repaired and people_calmed_down and engine_repaired:
                        print("You calmed the people down and you have solved everything. Congratulations. The ship can move on. \n")
                        Dead = False
                        if inventory["fruit"] >= 1:
                            inventory["fruit"] -= 1
                        elif inventory["soup"] >= 1:
                            inventory["soup"] -= 1
                        elif inventory["sandwich"] >= 1:
                            inventory["sandwich"] -= 1
                        time.sleep(1)
                else:
                    print("You can not do that\n\n")
                    time.sleep()

    if oxygen_repaired and people_calmed_down and engine_repaired:
        print("You start navigating to a supply station. \n\n")
        time.sleep(1)
    else:
        print(command_line_colors["red"]+"Game over. Try again\n\n")
        print(command_line_colors["white"])
        time.sleep(1)
        Dead = True

print(stories["out_of_the_asteroid_belt"])
player_answer = ""
while player_answer != "people" and player_answer != "friend":
    player_answer = input("Will you help the group of people stuck under some rubble first or your friend? people/friend: ")
    time.sleep(2)
    if player_answer == "friend":
        friend_saved = False
        friend_dead = False
        while not friend_saved and not friend_dead:
            friend_wounded_input = input(stories["friend_wounded"])
            while (friend_wounded_input == "stitch" or friend_wounded_input == "bandage") and not friend_dead and not friend_saved:
                if friend_wounded_input == "stitch":
                    need_alcohol = input("Do you want to poor some alcohol on your friends wound \
to desinfect the wound and to make it bleed less? (y/n): ")
                    if need_alcohol == "y":
                        print(f"Luckily {friend_names} survived because of your good treatment. One mistake and he would have been dead. \
Anyways, he says he owes you something.")
                        friend_saved = True
                        time.sleep(2)
                    elif need_alcohol == "n":
                        print(f"Sorry, but {friend_names} died while trying to stitch his wound. ")
                        inventory["friend"] = False
                        friend_dead = True
                        time.sleep(2)
                elif friend_wounded_input == "bandage":
                    if random_chance(33):
                        print(f"After all you tried to help {friend_names}, but he dies of the wound he had. The bandage was too loose. ")
                        inventory["friend"] = False
                        friend_dead = True
                        time.sleep(2)
                    else:
                        print(f"Luckily {friend_names} survived after you put the bandage tight around his wound. \n\
He owes you something, because you saved his life. ")
                        friend_saved = True
                        time.sleep(2)
                else:
                    print("How dare you to treat your friend like that. Do you want him to die?")
                    time.sleep(2)
    else:
        questions = [
            "What is the temperature of the sun? ",
            "How many moons does mars have? ",
            "What is the closest solar system to us? ",
            "How is the biggest asteroid called in the asteroid belt? ",
        ]
        answers = [
            [5780,5780+273],
            [2],
            ["alpha centauri"],
            ["ceres"],
        ]
        print("To help the people, you have to get two answers right within 3 attempts.")
        question_index = random.randint(0,3)
        amount_correct = 0
        for i in range(2): # two questions
            question_index = (question_index + 1) % 4
            player_answer = ""
            attempts = 0
            correct = False
            while attempts <= 2 and not correct:
                attempts += 1
                player_answer = input(questions[question_index])
                time.sleep(2)
                if type(answers[question_index][0]) == "string":
                    for answer in answers[question_index]:
                        if not correct:
                            if find_similarity(answer,player_answer) > 0.75:
                                print("Correct!")
                                correct = True
                                amount_correct += 1
                        if not correct:
                            if attempts != 2:
                                print("Try again.")
                            else:
                                print("Too bad, you didn't get it within 3 attempts.")
                else:
                    for answer in answers[question_index]:
                        if not correct:
                            if abs(1-answer/int(player_answer)) < 0.1: # als de afwijking minder dan 10% is
                                print("Correct!\n")
                                correct = True
                                amount_correct += 1
                        if not correct:
                            if attempts != 2:
                                print("Try again.\n")
                            else:
                                print("Too bad, you didn't get it within 3 attempts.\n")
                time.sleep(2)
        if amount_correct == 0:
            print("You weren't able to help anyone.")
        elif amount_correct == 1:
            print("You could only help one person.")
        else:
            print("You were able to help everyone!")
        time.sleep(2)

print("It isn't done yet! You still have to get out of the asteroid field, to navigate, \n\
give the coordinates of the next place you want to go to, you can move one tile, \n\
you can move horizontally, vertically and diagonally. You're the W, if you hit an asteroid, X \n\
then you lose, the asteroids move to the right every other move. You need to reach the bottom.")
grid = []
width = 11
height = 20
player = [5,0]
# create a list for the asteroids
for y in range(height):
    grid.append([])
    for x in range(width):
        grid[y].append(random.random() > 0.8 and "X" or "O")
# set the player position
grid[player[1]][player[0]] = "V"
move = False
while player[1] != 19:
    died = False
    if move:
        move = False
        for y in range(height-1,-1,-1): # loop inversely otherwise the asteroids could move the entire row instantly
            for x in range(width-1,-1,-1): # loop inversely otherwise the asteroids could move the entire row instantly
                if grid[y][x] == "X":
                    if grid[y][(x+1)%width] == "V":
                        print("You got hit by an asteroid!")
                        died = True
                    else:
                        grid[y][x] = "O"
                        grid[y][(x+1)%width] = "X"
    else:
        move = True
    # draw the numbers for the x axis
    print(command_line_colors["white"],end="",flush=True)
    print("   ",end="")
    for x in range(width):
        print(x,end=" ")
    print()
    for y in range(height):
        # draw the numbers for the y axis
        print(command_line_colors["white"],end="",flush=True)
        print(y,end=len(str(y)) == 1 and "  " or " ")

        for x in range(width):
            if grid[y][x] == "X":
                print(command_line_colors["red"],end="",flush=True)
            elif grid[y][x] == "V":
                print(command_line_colors["green"],end="",flush=True)
            elif move and grid[y][(x-1)%width] == "X":
                print(command_line_colors["yellow"],end="",flush=True)
            else:
                print(command_line_colors["white"],end="",flush=True)
            print(grid[y][x],end=" ",flush=True)
        print()
    print(command_line_colors["white"],end="",flush=True)
    moved = False
    while not moved and not died:
        split_text = input("give new coodinates: x,y: ").split(",")
        if len(split_text) == 2:
            move_to_x,move_to_y = split_text[0],split_text[1]
            if move_to_x.isnumeric() and move_to_y.isnumeric():
                x,y = int(move_to_x),int(move_to_y)
                if x < width and x >= 0 and y < height and y >= 0:
                    if abs(x-player[0]) <= 1 and abs(y-player[1]) <= 1:
                        moved = True
                        if grid[y][x] == "X":
                            print("You hit an asteroid!")
                            died = True
                        grid[player[1]][player[0]] = "O"
                        player[0],player[1] = x,y
                        grid[player[1]][player[0]] = "V"
                    else:
                        print("can't move that far!")
                else:
                    print("space isn't that big!")
            else:
                print("please provide a number coordinate")
        else:
            print("please provide an x and y coordinate")
    if died:
        # create a list for the asteroids
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(random.random() > 0.8 and "X" or "O")
                player = [5,0]
        grid[player[1]][player[0]] = "V"
        move = False
print("You made it out of the asteroid field, nicely done!")

print(stories["go_to_supply_station"])
print(stories_2["arrival_supply_station"])
shop_supply_station_boolean = False
while not shop_supply_station_boolean:
    input_shop_supply_station = input(stories_2["choice_shop_supply_station"])
    if input_shop_supply_station == "Jumbo":
        print("You are able to buy enough food for the way to mars. Your food consists largely of fish fingers. ")
        inventory["fish_fingers_or_tompouce_or_broccoli"] += 1
        shop_supply_station_boolean = True
    elif input_shop_supply_station == "Hema":
        print("You are able to buy enough food for the way to mars. Your food consists largely of tompouce. ")
        inventory["fish_fingers_or_tompouce_or_broccoli"] += 1
        shop_supply_station_boolean = True
    elif input_shop_supply_station == "Lidl":
        print("You are able to buy enough food for the way to mars. Your food consists largely of broccoli. ")
        inventory["fish_fingers_or_tompouce_or_broccoli"] += 1
        shop_supply_station_boolean = True
    else:
        print("You cannot choose this shop. ")
departure_supply_station_input = input(stories_2["departure_supply_station"])
right_gate_boolean = False
while not right_gate_boolean:
    if departure_supply_station_input == "m":
        print("Your choice was good. This is the right gate. Your journey goes on. ")
        right_gate_boolean = True
    else:
        print("This is the wrong gate. Try it again. ")

print(stories_2["going_to_mars"])
inventory["fish_fingers_or_tompouce_or_broccoli"] -= 1
print("ZZZZZZZzzzzzzzz",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)

print(stories["arrival_mars"])
mars_jeep__or_train = input(stories["jeep_or_train"])
made_choice = False
while not made_choice:
    if mars_jeep__or_train == "jeep":
        print("You enter the jeep. It will be a long, but beautiful journey to the last spaceport. ")
        print("Enjoying the ride",end="",flush=True)

        for i in range(10):
            time.sleep(0.5)
            print(".",end=(i==9 and "\n\n" or ""),flush=True)
        print(stories_2["jeep"])
        time.sleep(2)
        sand_or_not_input = input(stories_2["sand_or_not"])
        sandy_choice = False
        while not sandy_choice:
            if sand_or_not_input == "y":
                print("Now you put a bit of sand in a box. ")
                mars_sand = True
                sandy_choice = True
            elif sand_or_not_input == "n":
                print("This trip will be reminded by you, your life long. ")
                sandy_choice = True
            else:
                print("You have to enter \"y\" or \"n\"")
        print(stories_2["continue_jeep"])
        lose_tire_jeep_input = input(stories_2["lose_tire_jeep"])
        lose_tire_jeep_boolean = True
        while lose_tire_jeep_boolean:
            if lose_tire_jeep_input == "find":
                print("Searching",end="",flush=True)

                for i in range(10):
                    time.sleep(0.5)
                    print(".",end=(i==9 and "\n\n" or ""),flush=True)
                print("\n\nYou found the tire after hours of looking. Now you can move on. ")
                lose_tire_jeep_boolean = False
            elif lose_tire_jeep_input == "change":
                print("Changing tire",end="",flush=True)

                for i in range(10):
                    time.sleep(0.1)
                    print(".",end=(i==9 and "\n\n" or ""),flush=True)
                print("\n\nYou changed the tire in half an hour. Now you can move on. ")
                lose_tire_jeep_boolean = False
            else:
                print("Sorry, you cannot put this crappy tire on the jeep. ")
        made_choice = True
    elif mars_jeep__or_train == "train":
        print("You go with the train and You have chosen the quicker option \
if there is no trouble on your way to the spaceport to earth. ")
        made_choice = True
    else:
        print("Sorry, you cannot go to the spaceport with that. ")

print(stories_2["arrival_spaceport"])

# the player goes to a gate
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")
time.sleep(2)

print(f"You arrive at gate {gate}.",end="\n\n")
time.sleep(2)
print("Before entering you have to show your passport to the customs.")
time.sleep(2)
print(f"\"Thank you, have a nice flight {speler_data['name']}!\"")
time.sleep(2)
print("You enter the spaceship and take a seat somewhere in the back.")
time.sleep(2)
print("You depart from the spaceport for the last time.",end="\n\n")
time.sleep(2)
print("Travelling",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)
time.sleep(1)

print("Time to go back home.")
time.sleep(2)
gate = random_from_list(["A", "B", "C", "E", "D", "F"])
print(stories["go_to_gate"]+gate+".")
time.sleep(2)

print(f"You arrive at gate {gate}.",end="\n\n")
time.sleep(2)
print("Before entering you have to show your passport to the customs for the last time.")
time.sleep(2)
print(f"\"Thank you, have a nice return home {speler_data['name']}!\"")
time.sleep(2)
print("You enter the spaceship fall asleep.")
time.sleep(2)
print("You depart from the spaceport for the last time.",end="\n\n")
time.sleep(2)
print("Travelling",end="",flush=True)

for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n\n" or ""),flush=True)

time.sleep(1)
print("You get woken up by the jolt of the spaceship touching the launchpad.")
time.sleep(2)
print("But when you want to get out and return home, you notice that you're still in zero g...")
