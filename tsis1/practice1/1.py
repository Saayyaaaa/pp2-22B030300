# input: apple candy grapes banana
# output: I have apple, candy, grapes, banana in my shopping cart.

words = input().split() #строку разделяет на список подстрок по пробелу
formatted_sentence = "I have {objects} in my shopping cart" #метод формат
words_1 = ', '.join(words) #Преобразование списка в строку

print(formatted_sentence.format(objects = words_1))