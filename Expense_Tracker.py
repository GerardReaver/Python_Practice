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
#Create list for the attributes.
colors = ["red", "green", "white", "yellow", "blue"]
nationalities = ["norwegian", "dane", "german", "swede", "brit"]
drinks = ["beer", "coffee", "milk", "tea", "water"]
cigarettes = ["blends", "blue master", "dunhill", "pall mall", "prince"]
pets = ["birds", "cats", "dogs", "horses", "fish"]
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
could_be_green = [house3, house4]
# We can decude it can not be house 3 because it drinks milk and the green house drinks coffee. Therefore, house 4 must be green and house 5 must be white.
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
could_smoke_blue_master_and_drink_beer = [house2, house5] 
# This hint implies he will also drink beer.
# House 2 and House 5 are the only candidates for Dane/Tea
# House 2 and House 5 are also the only candidates for Blue Master/Beer
# They cannot be the same house because tea != beer.
# Therefore:
# One of House 2/5 = Dane + Tea
# The other House 2/5 = Blue Master + Beer
# This brought us to the revelation that house 1 must drink water because it is the only house left without a drink possibility.
# house 2 = beer/tea house 3 = milk house 4 = coffee house 5 = beer/tea house 1 = water
house1["drink"] = "water"
# Now we can do clue #15. The man who smokes blends has a neighbor who drinks water. 
# The only neighbor of house 1 is house 2. Therefore, the man who smokes blends must live in house 2.
house2["cigarette"] = "blends"
# we now know that house 5 must be the man who smokes blue master and drinks beer. 
# because house 2 is the man who smokes blends which eliminates house 2 from being the man who smokes blue master and drinks beer.
house5["cigarette"] = "blue master"
house5["drink"] = "beer" 
# This allows us to deduce that house 2 must be the Dane who drinks tea.
house2["nationality"] = "dane"
house2["drink"] = "tea"
# We can solve clue 13 now because there are only 2 houses left without a smoker and house 3 is british. 
# so the german smokes prince and lives in house 4.
house4["nationality"] = "german"
house4["cigarette"] = "prince"
# We now know who the swede is because there is only one nationality left. The swede must live in house 5 and he keeps dogs
house5["nationality"] = "swede"
house5["pet"] = "dogs"
# We now know who smokes Pall Mall because there is only one house left without a smoker and that is house 3.
house3["cigarette"] = "pall mall"
# We now who keeps birds because the person who smokes Pall Mall keeps birds. That is house 3.
house3["pet"] = "birds"
# We now know the man who smokes blends has a neighbor who keeps cats. The only neighbor of house 2 is house 1 without a pet. Therefore, house 1 must keep cats.
house1["pet"] = "cats"
# Finally there is only one house left without a pet and that is house 4. Therefore, house 4 must keep fish.
house4["pet"] = "fish"
# This is a loop to run the dictionaries and print them numbered.
for number, house in enumerate(houses, start=1):
    print(f"{number}: {house}")
