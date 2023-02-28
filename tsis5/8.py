import re
def split_at_uppercase(string):
    return [substring for substring in re.split(r'(?=[A-Z])', string) if substring]

my_string = "SplitThisStringAtUppercaseLetters"
new_list = split_at_uppercase(my_string)
print(new_list)