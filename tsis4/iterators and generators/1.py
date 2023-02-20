def square_generator(N):
    for i in range(1, N + 1, +1):
        yield i * i

for square in square_generator(int(input())):
    print(square)

N = int(input())
a = (i**2 for i in range(1, N+1, +1))
for i in a:
    print(i)