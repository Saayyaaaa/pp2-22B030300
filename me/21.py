n=int(input())
for num in range(10**n-1, 10**(n-1), -1):
    if num%2:
        print(num)

for i in range(3, 10):
    print(i, end = ", ")