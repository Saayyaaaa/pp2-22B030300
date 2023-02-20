def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

x = grams_to_ounces(int(input()))

print(x)