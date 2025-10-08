text = "apple banana cherry"
fruits = text.split()
print(fruits)

# Output: ['apple', 'banana', 'cherry']
# This code splits a string of fruits into a list of individual fruit names.

data = "john,23,new york"
data = data.split(',')
print(data)
# Output: ['john', '23', 'new york']
# This code splits a string containing a name, age, and city into a list using a comma as the delimiter.
# This code demonstrates how to use the split() method to divide strings into lists based on specified delimiters.

words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# Output: "Hello World Python"
# This code joins a list of words into a single string with spaces in between.

fruits = ['apple', 'banana', 'cherry']
line = ','.join(fruits)
print(line)
# Output: "apple,banana,cherry"
# This code joins a list of fruit names into a single string with commas separating them.
# This code demonstrates how to use the join() method to concatenate list elements into a single string with specified separators.

# Example usage of split() and join() methods in Python
# WRITE A PROGRAM THAT TAKES TWO INPUTS: A STRING AND A DELIMITER
# THE PROGRAM SHOULD SPLIT THE TEXT BYU WHITESPACE INTO WORDS, THEN JOIN THESE WORDS USING THE SPECIFIED DELIMITED CHARACTER AND PRINT THE RESULTING STRING.

text = "Hello world python"
delimiter = "-" 

result1 = text.split()
result2 = delimiter.join(result1)
print(result2)
# Output: "Hello-world-python"

# CREATE A PROGRAM THAT TAKES TWO INPUTS: A STRING OF NUMBERS SEPARATED BY SPACES AND A PREFIX STRING.
# THE PROGRAM SHOULD SPLIT THE NUMBER STRING INTO INDIVIDUAL NUMBERS, ADD THE PREFIX TO EACH NUMBER THEN JOIN THESE MODIFIED NUMBERS BACK INTO A SINGLE STRING SEPARATED BY SPACES. 
# FINALLY, PRINT THE RESULTING STRING. 

numbers = "123 456 789"
prefix = "+1"
result3 = numbers.split()
for i in range(len(result3)):
    result3[i] = prefix + result3[i] 
    result4 = " ".join(result3)
print(result4) 