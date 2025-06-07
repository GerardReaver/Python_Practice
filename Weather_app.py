# The following code is going to be used to help create a weather app to determine suitable outdoor activities based on the the weather conditions. 
# Create a program that uses logiacl operations to determine if certain activities are possible.

is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22
# These are the variables that are needed to determine what activities are viable for these weather conditions

can_go_hiking = is_sunny == True and temperature > 15 and wind_speed < 20

can_go_swimming = is_sunny == True and temperature > 20 and water_temperature > 18

cannot_go_outside = is_sunny == False or temperature < 10 or wind_speed > 30

print("can go hiking:", can_go_hiking)
print("can go swimming:", can_go_swimming)
print("cannot go outside:", cannot_go_outside)