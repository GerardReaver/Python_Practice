# i happens to be a variable that you don't have to set outside of the equation. just print it here. 

# STRING CONCATENATION

for i in range(5):
  print('The square of ' + str(i) + ' is ' + str(i*i))

# you need to use the string function "str()" to put the interger of the for function into the string and place it like any other word while changing its value. 

# STRING INTERLOPATION
# String interpolation is a process of substituting values of variables into placeholders in a string.
# For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to meet you!', you would like to replace the placeholder {name} with an actual name. 
for i in range(5):
  print(f'The square of {i} is {i*i}')

# "99 Bottles of Beer" is an old song that annoying kids, oops I mean everyone, sang on road trips to pass the time.

# Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."
i = 99
for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i - 1} bottles of beer on the wall')