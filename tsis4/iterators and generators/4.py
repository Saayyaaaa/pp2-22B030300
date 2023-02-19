def square_of_numbers(A, B):
    for i in range(A, B+1, +1):
        yield i*i

for num in square_of_numbers(int(input()), int(input())):
    print(num)