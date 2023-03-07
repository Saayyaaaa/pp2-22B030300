# import os
# entries = os.listdir('../Directories and Files')
# listFiles=next(os.walk('.'))[2]
# for listFile in listFiles:    
#     print(listFile)

import os

root_dir = os.getcwd() #Метод getcwd () модуля os в Python возвращает строку, содержащую абсолютный путь к текущему рабочему каталогу
for dirpath, dirnames, filenames in os.walk(root_dir):
    print("directory: ", dirpath)
    print("subdirectories: ", dirnames)
    print("files: ", filenames)