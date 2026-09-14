# We are starting the Einstein problem. First thing we will do is print the name. 
print("Einstein Puzzle")
print("")
print("There are five houses of different colors next to each other. In each house lives a man.")
print("Each man has a unique nationality, an exclusive favorite drink, a distinct favorite brand of cigarettes and keeps specific pets.")
print("Use all the clues below to fill the grid and answer the question: 'Who owns the fish?'")
print("")
# Time to create a dictionary for the houses. 
house1 = {
    "color": "",
    "nationality": "", 
    "drink": "",
    "cigarette": "",
    "pet": ""
}
house2 = {
    "color": "",
    "nationality": "", 
    "drink": "",
    "cigarette": "",
    "pet": ""
}
house3 = {
    "color": "",
    "nationality": "", 
    "drink": "",
    "cigarette": "",
    "pet": ""
}
house4 = {
    "color": "",
    "nationality": "", 
    "drink": "",
    "cigarette": "",
    "pet": ""
}
house5 = {
    "color": "",
    "nationality": "", 
    "drink": "",
    "cigarette": "",
    "pet": ""
}
#Create a list of the houses to make it easier to iterate through them and get positional information. 
houses = [house1, house2, house3, house4, house5]
#Solving the problem is now going to begin. We will use the clues to fill in the houses.
house3["drink"] = "milk" #Clue 8
house1["nationality"] = "norwegian" #Clue 9
house2["color"] = "blue" #Clue 14
#Clue 9 check.
for house in houses:
    if house["nationality"] == "norwegian":
        print("Found the Norwegian!")
#Clue 8 check.
for house in houses:
    if house["drink"] == "milk":
        print("Found the milk drinker!")
#Clue 14 check.
for house in houses:
    if house["color"] == "blue":
        print("Found the blue house!")
#Create list for the attributes.
colors = ["red", "green", "white", "yellow", "blue"]
nationalities = ["norwegian", "dane", "german", "swede", "brit"]
drinks = ["beer", "coffee", "milk", "tea", "water"]
cigarettes = ["blends", "blue master", "dunhill", "pall mall", "prince"]
pets = ["birds", "cats", "dogs", "horses", "fish"]
#Test loops for the attributes.
for color in colors:
    for house in houses:
        if house["color"] == color:
            print(f"Found the {color} house!")
for nationality in nationalities:
    for house in houses:
        if house["nationality"] == nationality:
            print(f"found the {nationality} house!")
for drink in drinks:
    for house in houses:
        if house["drink"] == drink:
            print(f"found the {drink} house!")
for cigarette in cigarettes:
    for house in houses:
        if house["cigarette"] == cigarette:
            print(f"found the {cigarette} house!")
for pet in pets:
    for house in houses:
        if house["pet"] == pet:
            print(f"found the {pet} house!")
# Making my first deduction code. 
for house in houses:
    if house["nationality"] == "dane" and house["drink"] == "tea":
        print("The Dane drinks tea!")
#Starting to actually have python test the loops for the clue above. 
for nationality in nationalities:
    for drink in drinks:
        if nationality == "dane" and drink == "tea":
            print(f"{nationality} drinks {drink}")
# Creating my first loop constraint
possible_green_houses = []
for number in range(4):
    if houses[number]["color"] != "blue" and houses[number + 1]["color"] != "blue" and houses[number]["drink"] != "milk":
        possible_green_houses.append(number + 1)
print(f" possible green houses are: {possible_green_houses}")
# Dictionaries for the new clues we found out are added here. 
house4["color"] = "green" #Clue 4 and 5 combined. The green house is to the left of the white house and the green house drinks coffee.
house5["color"] = "white" #Clue 4 and 5 combined.
house4["drink"] = "coffee" #Clue 4 and 5 combined. 
# This function below will print which house the brit can live in while running an enumerate loop to get the house's number and print the houses dictionary 
# information to make for easier reading. 
for number, house in enumerate(houses, start=1):
    if house["color"] != "blue" and house["color"] != "green" and house["color"] != "white" and house["drink"] != "coffee" and house["nationality"] != "norwegian":
        print(f"The Brit can live in house {number}: {house}")  
# add the new information to the house dictionaries. 
house3["color"] = "red" #Clue 1. The Brit lives in the red house. we know this because the only house left for the Brit to live in is house 3.
house3["nationality"] = "brit" #Clue 1. The Brit lives in the red house. we know this because the only house left for the Brit to live in is house 3.
house1["color"] = "yellow" # This happend because it is the only color remaining after clue 1, 4, 9, and 14 were used.
house1["cigarette"] = "dunhill" #Clue 7. The man who smokes Dunhill lives in the yellow.
house2["pet"] = "horses" #Clue 11. the man who keeps horses lives next to the man who smokes dunhill. Its the only house left.  
# This is a loop to run the dictionaries and print them numbered. 
for number, house in enumerate(houses, start=1):
    print(f"{number}: {house}")
#Solving clue 15. the man who smokes blends has a neighbor who drinks water. 
could_smoke_blends = [house2, house3, house4, house5]
for house in could_smoke_blends:
    number = houses.index(house) + 1
    print(f"Could smoke blends house number {number}: {house}")
could_dane_drink_tea = [house2, house5] 
#This hint implies he will also be the Dane.
could_smoke_blue_master_and_drink_beer = [house2, house5] 
#This hint implies he will also drink beer.
# House 2 and House 5 are the only candidates for Dane/Tea
# House 2 and House 5 are also the only candidates for Blue Master/Beer
# They cannot be the same house because tea != beer.
# Therefore:
# One of House 2/5 = Dane + Tea
# The other House 2/5 = Blue Master + Beer
could_smoke_pall_mall_and_have_birds = [house3, house4, house5]
# The final hint says the man who smokes blends has a neighbor who drinks water. this elimates house 5 from our previous list. 
could_smoke_blends.remove(house5)
could_swede_have_dogs = [house4, house5]
could_german_smoke_prince = [house2, house4, house5]