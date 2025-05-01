# Write code below 💖\

# These are the 4 magic houses we need as variables
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#This is the first Question
print(' THE SORTING HAT WOULD LIKE TO SORT YOU AS WELL!!!')
print('')
print('Q1. Do you like Dawn or Dusk')
print('1. Dawn')
print('2. Dusk')
answer = int(input('Enter answer 1 or 2  '))

# This puts the points to each of the variables from question 1
if answer == 1:
  Gryffindor = +1
  Ravenclaw = +1
elif answer == 2:
  Hufflepuff = +1
  Slytherin = +1
else:
  print('INVALID INPUT')

# This is question number 2
print('')
print('Q2. When im dead I want people to remember me as   ')
print('1. The Good')
print('2. The Great')
print('3. The Wise')
print('4. The Bold')
answer = int(input('Enter your answer from 1-4   '))

# This puts the points into the variables from question 2
if answer == 1:
  Hufflepuff = +2
elif answer == 2:
  Slytherin = +2
elif answer == 3:
  Ravenclaw = +2
elif answer == 4:
  Gryffindor = +2
else:
  print('INVALID INPUT')

# This is question number 3
print('')
print('Q3. Which kind of instrument most pleases your ear?')
print('1. The Violin')
print('2. The Trumpet')
print('3. The Piano')
print('4. The Drum')
answer = int(input('Enter a number from 1-4  '))

# This puts the points into the variables from question 3
if answer == 1:
  Slytherin = +4
elif answer == 2:
  Hufflepuff = +4
elif answer == 3:
  Ravenclaw = +4
elif answer == 4:
  Gryffindor = +4
else:
  print('INVALID INPUT')

# The final line of code that i went with. I could have created one more to put the result but i prefer it this way. 
print('YOU HAVE BEEN ACCEPTED TO THE HOSUE WITH THE MOST POINTS!!!')
print('')
print("Gryffindor", Gryffindor)
print("Ravenclaw", Ravenclaw)
print("Hufflepuff", Hufflepuff)
print("Slytherin", Slytherin)

# BONUS lines of code to add one more if statement to pull the end result of all the remaining variables.
if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')