L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))

def even_fn(x):
    if x % 2 == 0:
        return True
        return False

print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))