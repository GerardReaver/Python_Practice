# We are trying to complete the einstein riddle 991 code without any help. 
# Create dictionaries for the houses. 
house1 = {
    "color": "",
    "tree": "",
    "drink": "",
    "sport": ""
    }
house2 = {
    "color": "",
    "tree": "",
    "drink": "",
    "sport": ""
    }
house3 = {
    "color": "",
    "tree": "",
    "drink": "",
    "sport": ""
    }
house4 = {
    "color": "",
    "tree": "",
    "drink": "",
    "sport": ""
    }
# Create list for the attributes.
houses = [house1, house2, house3, house4]
color = ["black", "green", "orange", "red"]
tree = ["maple", "palm", "pine", "spruce"]
drink = ["boba", "herbal", "iced", "juice"]
sport = ["baseball", "football", "golf", "swimming"]
# clue 1: The man who plays baseball lives in the third house.
# clue 2: The man who plays golf is in the first house.
# clue 3: The one whose favorite drink is iced is the swimming player.
# clue 4: The orange house is the first house
# clue 5: the red house is the third house.
# clue 6: the house shaded by the maple is somewhere to the right of the black house.
# clue 7: The one whose favorite drink is juice lives next to the house shaded by the palm. 
# clue 8: The one whose favorite drink is herbal is the football player.
# clue 9: the house shaded by the spruce is the second house
# clue 10: The man whose favorite drink is herbal lives in the black house. 
# The code begins here. 
house3["sport"] = "baseball" # Clue #1 satisfied
house1["sport"] = "golf" # Clue #2 satisfied 
house1["color"] = "orange" # Clue #4 satisfied
house3["color"] = "red" # Clue #5 satisfied
possible_black_maple = []
for black_number in range(len(houses)):
    for maple_number in range(len(houses)):
        if maple_number > black_number and houses[black_number]["color"] != "orange" and houses[black_number]["color"] != "red":
            possible_black_maple.append((black_number + 1, maple_number + 1))
            print(f"black_number {black_number + 1} and maple number {maple_number + 1}") 
print(f"Possible black and maple pairs are {possible_black_maple}")
house2["color"] = "black" # Clue #6 partially satisfied 1/2
house4["color"] = "green" # only color remaining
house2["tree"] = "spruce" # Clue #9 satisfied
house2["drink"] = "herbal" # Clue 10 satisfied
# Here we are going to make a condition to solve for clue #3. 
possible_iced_swimmer = []
for iced_swimmer in range(len(houses)):
    if houses[iced_swimmer]["drink"] != "herbal" and houses[iced_swimmer]["sport"] != "baseball" and houses[iced_swimmer]["sport"] != "golf":
        possible_iced_swimmer.append(iced_swimmer + 1)
        print(f"Possible iced drink and swimmer house {possible_iced_swimmer}")
house4["drink"] = "iced" # Clue #3 satisfied 
house4["sport"] = "swimming" # Clue #3 satisfied
# Here we are going to make a condition to solve for clue #7.
possible_juice_palm = []
for juice_palm in range(len(houses)):
    if houses[juice_palm]["drink"] != "herbal" and houses[juice_palm]["drink"] != "iced":
        if juice_palm == 0:
            if houses[juice_palm + 1]["tree"] != "spruce":
                possible_juice_palm.append(juice_palm + 1)
        elif juice_palm == len(houses) - 1:
            if houses[juice_palm - 1]["tree"] != "spruce":
                possible_juice_palm.append(juice_palm + 1)
        else:
            if (houses[juice_palm + 1]["tree"] != "spruce" or houses[juice_palm - 1]["tree"] != "spruce"):
                possible_juice_palm.append(juice_palm + 1)
# Print the outcome for the list        
print(f"This is the possible house number for juice with a neighbor tree palm {possible_juice_palm}")
house3["drink"] = "juice" # Clue #7 satisifed
house4["tree"] = "palm" # Clue #7 satisfied 
house3["tree"] = "maple" # maple only had 2 options of house3 and house4 and house4 just took palm which leaves one option. 
house1["tree"] = "pine" # Only tree remaining
house1["drink"] = "boba" # Only drink remaining
house2["sport"] = "football" # Clue #8 satisfied
# All clues have been satisfied. 
# This line of code will be run at the end to get the total results. 
for number, house in enumerate(houses):
    print(f"This is house {number + 1}: {house}")
