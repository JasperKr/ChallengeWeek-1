import random
import time
inventory = []
speler_data = dict(name = "")
stories = dict(
    intro = "You have arrived at the launchpad and you need to check in. There is a security guard. ",
    departure = "you depart"
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
print(stories["departure"])
print("travelling: ",end="",flush=True)
for i in range(10):
    time.sleep(0.5)
    print(".",end=(i==9 and "\n" or ""),flush=True)