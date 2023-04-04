import os
 
path = r'C:\Users\Сая\Desktop\pp2-22B030300\tsis7\music'
songs = []

for file in os.listdir(path):
    if file.endswith(".mp3"):
        songs.append(file)
 
print(songs)