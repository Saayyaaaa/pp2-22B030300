f = open('rawdata.txt', mode='r')
# s = f.read()
# print(s, type(s))

# s = f.readline()
# print(s, type(s))
# print(f.readline())

s = f.readlines() #readline() используется для построчного чтения содержимого файла. Она используется для крупных файлов
print(s, type(s))

line_coun = 0
for line in s:
    line_coun += 1
print(line_coun)

f.close()