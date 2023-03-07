
import os

print(os.getcwd()) #getcwd() модуля os вернет строку, представляющую текущий рабочий каталог
print(os.getcwdb()) #getcwdb() вернет строку байтов, представляющую текущий рабочий каталог
print(os.listdir('.')) #os.listdir() Она показывает все содержимое каталога
print(os.listdir(os.getcwd()))
print(os.chdir(r'C:\Users\Сая\Desktop\pp2-22B030300\tsis6\Directories and Files')) #os.chdir() — смена текущей рабочей директории
print(os.getcwd())