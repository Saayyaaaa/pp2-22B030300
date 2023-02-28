import re

pattern = r'a[b]*'

test_strings = ['ab', 'abb', 'a', 'acb', 'abbb', 'abbbb', 'b']

for s in test_strings:
    if re.match(pattern, s):
        print(s, "matches the pattern.")
    else:
        print(s, "does not match the pattern.")
