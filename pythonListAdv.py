numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])
# Output: [2, 3, 4, 5] 
# This slice starts at index 2 and goes up to, but does not include, index 6. (exclusive)

print(numbers[:5])
# Output: [0, 1, 2, 3, 4]
# This slice starts at the beginning of the list and goes up to, but does not include, index 5. it ommites the first index.

print(numbers[5:])
# Output: [5, 6, 7, 8, 9]
# This slice starts at index 5 and goes to the end of the list. it ommites the last index.

# CREATE A PROGRAM THAT RECEIVES A LIST AS AN IN PUT AND PRINTS THE FOLLWOING SLICED LISTS. 
# FOR ODD-LENGTH LISTS: TAKE THE MIDDLE ITEM AND ONE ITEM ON EACH SIDE (3 ITEMS TOTAL)
# FOR EVEN-LENGTH LISTS: TAKE THE TWO MIDDLE ITEMS. 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mid = 0
if len(lst) % 2 == 0:
    mid = len(lst) // 2
    print(lst[mid - 1:mid + 1])
elif len(lst) % 2 == 1:
    mid = len(lst) // 2
    print(lst[mid -1:mid + 2])
else:
    print("you screwed up")

input_list = [1, 2, 3, 4, 5, 6]

first_two = input_list[:2]
last_two = input_list[len(input_list) -2:len(input_list)]
more_five = first_two + last_two
first = input_list[:1]
last = input_list[len(input_list) -1: len(input_list)]
less_five = first + last  
if len(input_list) >= 5:
    print(more_five)
else:
    print(less_five)