# Write code below 💖
guess = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input('Guess the number:  '))
  tries = tries +1
if guess != 6:
  print('YOU RAN OUT OF TRIES')
else:
  print('YOU WIN DUDE')

# When trying to calculate for tries you need to make it equal to itself plus 1 for the new attempt when updating the variable