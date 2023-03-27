import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
image = pygame.image.load(r'C:\Users\Сая\Desktop\pp2-22B030300\tsis7\imagetest\tutorial_2_3.png')
screen.fill((255, 255, 255))
screen.blit(image, (50, 20))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        pygame.display.flip()