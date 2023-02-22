def even_numbers(N):
    for i in range(1, N+1, +1):
        if i % 2 == 0:
            yield i

for num in even_numbers(int(input())):
    print(num)