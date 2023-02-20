def Fahrenheit(F):
    C = (5 / 9) * (F-32)
    return C

x = Fahrenheit(int(input()))
print(x)