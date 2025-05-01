# Write code below 💖

height_question = int(input('What is your height in cm?   '))

credit_question = int(input('How many credits do you have?   '))

if height_question > 136 and credit_question > 9:
  print('Enjoy the ride!')
elif not height_question > 136 and credit_question > 9:
  print('You are not tall enough to ride.')
elif height_question > 136 and not credit_question > 9:
  print("You don't have enought credits")
else:
  print('You have not many any of the requirements')

# This returns a program where it returns whether you meet the requirements to ride this specific roller coaster based on the logical operations of the file. 
# you enter your height in cm, then your number of credits and receive your answer. 