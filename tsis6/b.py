def generator(a, b):
    for i in range(b, a+1, -1):
        x = math.sqrt(i)
        yield x

for num in generator(int(input()), int(input())):
    print(num)