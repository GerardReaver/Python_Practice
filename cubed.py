# Create a function called cube_number that takes a single parameter n and returns its cube. 
# Then, call the function with the input value and store the result in a variable called result. Finally, print the value of result.
def cube_number(n):
    # Write you code below
    return n * n * n 
    

input_num = int(input())
result = cube_number(input_num)  # call the function
print(result)
