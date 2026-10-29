# These are my test cases scenarios
str1 = "hello"
str2 = "hello world"

# Begin by creating the function
def comparer_strings(str1, str2):
    result = {}
    if str1 in str2:
        result["is_substring"] = True
    else:
        result["is_substring"] = False

    if str2.startswith(str1):
        result["starts_with"] = True
    else:
        result["starts_with"] = False

    if str2.endswith(str1):
        result["ends_with"] = True
    else:
        result["ends_with"] = False

    if str1 == str2:
        result["is_equal"] = True
    else:
        result["is_equal"] = False
    return result

# Call the function with the test cases
print(comparer_strings(str1, str2))
