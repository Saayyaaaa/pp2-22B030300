def upper_lower_case(str):
    s = "ASfghhdxsdfdghcsshGSGHSJJ"
    x = {sum(map(str.isupper, s))}
    y = {sum(map(str.islower, s))}
    return x, y

print(upper_lower_case(str))