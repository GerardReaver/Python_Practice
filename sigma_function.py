# Write a function named "Sigma" with one argument that represents a numebr "n". 
# The function will return the sum of all the numbers from 1 to n (including). 
# For example, for "Sigma(5), the function will return 15, because 15 = 1 + 2 + 3 + 4 + 5. 
def sigma(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

sigma(5)
