import re

pattern = r'[A-Z][a-z]+'

test_string = input() #This is Test

matches = re.findall(pattern, test_string)

print(matches)