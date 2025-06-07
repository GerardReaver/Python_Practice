# THIS CODE WILL HELP DETERMINE IF THIS PETSHOP WILL BE ABLE TO SELL DIFFERENT TYPES OF PETS BASED ON THE QUALIFICATIONS OF THE LOCATION

# Initialize variables
has_license = True
has_space = True
has_experience = False 

# Calculate conditions
can_sell_regular_pet = (has_license == True) or (has_experience == True) and (has_space == True)
can_sell_exotic_pet = (has_license == True) and (has_experience == True) and (has_space == True)
cannot_sell_any_pet = (has_license == False) and (has_experience == False) or (has_space == False)

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)
