import os

os.mkdir('./new') #Метод os.mkdir () создаёт директорию, выдает OSError, если директория существует
print(os.listdir('.'))
os.makedirs('./tests1/subtests1/subsubtests1') #Метод os.makedirs () создаёт директорию, создавая при этом промежуточные директории
os.rmdir('./tests1')

# Функция rmdir() модуля os удаляет путь к каталогу path.
# Если директория path не существует или не является пустым 
# каталогом, соответственно возникает исключение FileNotFoundError или OSError.