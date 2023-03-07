import os

root_dir = os.getcwd() #Метод getcwd () модуля os в Python возвращает строку, содержащую абсолютный путь к текущему рабочему каталогу
for dirpath, dirnames, filenames in os.walk('../week7'):
    print("directory: ", dirpath)
    print("subdirectories: ", dirnames)
    print("files: ", filenames)