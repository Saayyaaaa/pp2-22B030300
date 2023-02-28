import re

pattern = r'a.*b$'

test_string = input()
match = re.search(pattern, test_string)

print(bool(match))
