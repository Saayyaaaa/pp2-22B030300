x = int(input())
k = 1
for i in range(x):
    print(' '*(x-1-i),'*'*k, sep='')
    k += 2