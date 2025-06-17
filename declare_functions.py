# This code will be able to declare a function to be able to be used for multiple purposes without having to rewrite the code several different times. 
# we want you to write a function that gets one input, a number. The input number indicates how many times to execute the below function. 
# Create a function that calculates the sum of all of the numbers from 1-10000 (including) and prints it. name the function whatever. 

n = int(input())

def sum_numbers():
    total = 0
    for a in range(1, 10001):
        total += a
    print(total)

for b in range(n):
    sum_numbers()
