def all_numbers(N):
    for i in range(N, -1, -1):
        yield i

for num in all_numbers(int(input())):
    print(num)