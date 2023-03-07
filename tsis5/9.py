import re
def insert_spaces(string):
    new_string = ""
    for char in string:
        if char.isupper() and new_string != " ":
            new_string += " "
        new_string += char
    return new_string

my_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
new_string = insert_spaces(my_string)
print(new_string)