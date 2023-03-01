import re

pattern = r'^a[b]*$'

test_strings = ['ab', 'abb', 'a', 'acb', 'abbgb', 'abbbb', 'b']

for s in test_strings:
    if re.match(pattern, s):
        print(f"{s}: True")
    else:
        print(f"{s}: False")