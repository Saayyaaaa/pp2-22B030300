import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 500))
done = True
play = True
num = 0

#Лист .mp3
path = r'C:\Users\Сая\Desktop\pp2-22B030300\tsis7\music'
songs = []

for file in os.listdir(path):
    if file.endswith(".mp3"):
        songs.append(file)

clock = pygame.time.Clock()
pygame.mixer.music.load('tsis7/music/' + songs[0])
pygame.mixer.music.play()

while done:
        current = num
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    done = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play

                elif event.key == pygame.K_RIGHT:
                    if num < len(songs)-1:
                        num += 1
                    else:
                        num = 0

                elif event.key == pygame.K_LEFT:
                    if num > 0:
                        num -= 1
                    else:
                        num = len(songs)-1
        
        screen.fill((0, 250, 109))

        font = pygame.font.SysFont("balker", 60)

        name = songs[num].replace('.mp3','')

        text = font.render(name, False, (112, 112, 255))
        text_rect = text.get_rect(center=(800/2, 500/2))

        screen.blit(text, text_rect)

        if play == False:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        if current != num:
            pygame.mixer.music.load('tsis7/music/' + songs[num])
            pygame.mixer.music.play()
        
        pygame.display.flip()
        clock.tick(60)