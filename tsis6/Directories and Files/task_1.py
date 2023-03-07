import os
entries = os.listdir('../Directories and Files')
listFiles=next(os.walk('.'))[1]
for listFile in listFiles:    
    print(listFile)

print(os.path.join('.', name))