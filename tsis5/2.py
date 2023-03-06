import re

pattern = r'a[b]{2,3}'

test_strings = ['abbbabadedjabbbaddjfjabbb']

for s in test_strings:
    print(re.findall(pattern, s))