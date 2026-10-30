# Variables to test the code
list1 = [1, 2, 3]
element_to_append = 4
index_to_remove = 5

# Function to append an element to a list
def manage_list(list1, element_to_append, index_to_remove):
    # Append the element to the list
    list1.append(element_to_append)
    print(list1)
    # Remove the element at the specified index if it exists
    if index_to_remove < len(list1):
        list1.pop(index_to_remove)
        print(list1) 
    if len(list1) > 3:
        print("The list has more than 3 elements")
    else:
        print("The list has 3 or feewer elements")

manage_list(list1, element_to_append, index_to_remove)