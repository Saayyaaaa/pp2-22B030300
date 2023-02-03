def extender(source_list, extend_list):
    source_list.extend(extend_list)

values = list(map(int, input().split()))
extender(values, [4, 5, 6])
print(values)

print(list(map(lambda n: n**2, values)))

def square(n):
    return n**2
print(list(map(square, values)))