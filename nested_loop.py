# Write a program that finds all pairs of numbers that multiply to give n using numbers from 1-n. 
# The program should show all possible combinations including duplicate pairs in reverse order. 
n = int(input())
# Write your code below
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == n:
            print(i, j)
