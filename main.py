import random
inventory = []
speler_data = dict(name = "",surname = "")
stories = dict(
    intro = "You have landed on a spaceport and you are going to the sun. \n\
The last thing you have to get is somewhere at the spaceport.\n\
You have to get a sun suit. \n\
There is a shoppingmall, a pilot walking around and you have a suitcase with you. "
)
playing = True
while playing:
    print(stories["intro"])# begin het spel, print het begin verhaal text
    name_correct = False
    while not name_correct:
        speler_data["name"] = input("What is your name? ").title()
        speler_data["achternaam"] = input("What is your surname? ")
        name_correct = input(f"Please verify your name, {speler_data['name']} {speler_data['achternaam']}, y/n: ") == "y"
    