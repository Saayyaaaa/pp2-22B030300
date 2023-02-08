# Set -> pop, discard, remove
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]

s = set(a)

query = int(input())
print(query)

for _ in range(query):
    q = tuple(input().split()) #неизменяемый список
    if q[0] == "pop":
        s.pop()
    elif q[0] == "discard":
        s.discard(int(q[1]))
    elif q[0] == "remove":
        s.remove(int(q[1]))
        print(sum(s))