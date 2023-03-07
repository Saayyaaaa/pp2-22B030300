import os
f = open('task_1.txt', 'r+')
print(f.read())
f.write('\nhello kbtu - 1\n')
f.write('1 2 3')
print(f.read())
f.close()