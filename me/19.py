a = int(input())

b = a * 45
c = int(float(a/2))

if a % 2 == 1:
    d = (c+1)*5
else:
    d = c * 5

f = b + c*10 + d
print(f)

g = int(float(f / 60))
print(g)

h = int(float(f / 60))
print(h)


print(9 + g, f - g*60)