def divisible_nums(N):
    for i in range(1, N+1, +1):
        if i % 3 == 0 and i % 4 == 0:
            print(i)

divisible_nums(int(input()))