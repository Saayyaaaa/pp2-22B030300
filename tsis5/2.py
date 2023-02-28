import re

pattern = r'a[b]{2,3}'

test_strings = ['ab', 'abb', 'a', 'acb', 'abbb', 'abbbb', 'b']

for s in test_strings:
    if re.match(pattern, s):
        print(s, "True")
    else:
        print(s, "False")