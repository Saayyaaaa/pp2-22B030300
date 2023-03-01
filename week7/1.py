import os

def createFile(fname):
    f = open(file_name+".txt", mode='w')
    print(f)
    f.write('hello kbtu - 1\n')
    f.write('1 2 3')

def readFile(fname):
    f = open(fname, mode='r')

    s = f.readlines()
    print(s, type(s))

    f.close()

def appendFile(fname):
    f = open(fname, mode='r')
    fname.remove()
    s = f.readlines()
    print(s, type(s))

    f.close()

def overwriteFile(fname):
    pass

def removeFile(fname):
    pass


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')