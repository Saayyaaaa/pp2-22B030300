import pygame 
pygame.init() 
white =(255, 255, 255) 
height = 400 
width = 400 
display_surface = pygame.display.set_mode((height, width)) 
 
pygame.display.set_caption('Image') # set the pygame window name  
 
image = pygame.image.load(r'C:\Users\DEVANSH SHARMA\Desktop\download.png')  #загружаем картину
 
while True: 
    display_surface.fill(white) 
    display_surface.blit(image,(0, 0)) 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
        pygame.display.update()  