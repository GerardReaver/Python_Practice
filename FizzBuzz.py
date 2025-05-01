# Write code below 💖
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)

# just remember the order of the operations matter so it needs to check for the 3 and 5 first then it can check for the rest by themselves with 'elif' statements