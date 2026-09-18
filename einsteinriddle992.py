# Here is another einstein riddle for practicing python. 
# Create the dictionaries
house1 = {
    "color": "",
    "pet": "",
    "tree": "",
    "flower": ""
}
house2 = {
    "color": "",
    "pet": "",
    "tree": "",
    "flower": ""
}
house3 = {
    "color": "",
    "pet": "",
    "tree": "",
    "flower": ""
}
house4 = {
    "color": "",
    "pet": "",
    "tree": "",
    "flower": ""
}
# Create list
houses = [house1, house2, house3, house4]
colors = ["green", "orange", "red", "yellow"]
pets = ["fish", "horse", "pig", "turtle"]
trees = ["bamboo", "palm", "pine", "spruce"]
flowers = ["daisy", "hyacinth", "rose", "sunflower"]
# Begin the process
house4["flower"] = "rose"
house3["flower"] = "sunflower"
house1["pet"] = "fish"
house2["flower"] = "daisy"
house1["flower"] = "hyacinth"
house2["flower"] = "spruce"
house2["pet"] = "pig"
house3["tree"] = "pine"
house2["color"] = "green"
house1["tree"] = "palm"
house3["pet"] = "horse"
house4["pet"] = "turtle"
house4["tree"] = "bamboo"
house3["color"] = "red"
house1["color"] = "yellow"
house4["color"] = "orange"


# run the houses for the final
for number, house in enumerate(houses, start=1):
    print(f"House #{number}: {house}")