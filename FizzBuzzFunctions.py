# create Fizzbuzz as a function with 3 = fizz 7 = buzz and both as Fizzbuzz. 
# This program will recieve an input rather than create a loop of all numbers 
print("Welcome to FizzBuzz!")

def fizzbuzz(n):
    if n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    else:
        return n

n = int(input())

print(fizzbuzz(n))
    
