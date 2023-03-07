import string, os

if not os.path.exists("letters"): #os.path.exists проверяет существует ли указанный путь и возвращает True или False
   os.makedirs("letters") #os.makedirs () создаёт директорию, создавая при этом промежуточные директории
for letter in string.ascii_uppercase:
   #Python3 ascii_uppercase — это предварительно инициализированная строка, используемая как строковая константа

   with open(letter + ".txt", "w") as f:
       f.writelines(letter) #writelines () — для записи сразу списка строк в файл