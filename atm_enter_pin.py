print('BANK OF CODEX')

pin = int(input('Enter your PIN:  '))

# This is an example of a WHILE LOOP. it will keep continueing as long as you don't reach the desired outcome and it will continue to loop
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again:'))

if pin == 1234:
  print('PIN accepted')

# When you type in the correct PIN you will finally get the PIN accepted answer and won't have to continue the WHILE LOOP