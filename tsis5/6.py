import re
def replace_chars_with_colon(string):
    chars_to_replace = [' ', ',', '.']

    for char in chars_to_replace:
        string = string.replace(char, ':')

    return string

my_string = input() #"Hello, world. How are you?"
new_string = replace_chars_with_colon(my_string)
print(new_string)
