# Get age as an integer
age = int(input())

# Get parental guidance as a boolean (True/False)
with_parent = input() == "true"

# Declare a variable named message with "None"
message = "None"

# Write your nested if-else code here
if age < 18:
    if with_parent == True:
        message = "You can watch PG-13 movies"
    else:
        message = "You can only watch G-rated movies"
else:
    message = "You can watch any movie"

# Don't change below this line
print(message)
