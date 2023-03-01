import re

pattern = r'[a-z+_a-z]+'

test_string = 'this_is_a_test_string with_something_more'

matches = re.findall(pattern, test_string)

print(matches)