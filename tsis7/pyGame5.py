import pygame

pygame.init()

WIDTH = 1400
HEIGHT = 1050

center = (1400//2, 1050//2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
image = pygame.image.load(r'C:\Users\Сая\Desktop\pp2-22B030300\tsis7\clockmickey\mickeyclockbase.png')
minute = pygame.image.load(r'"C:\Users\Сая\Desktop\pp2-22B030300\tsis7\clockmickey\minut.png"')
second = pygame.image.load(r'"C:\Users\Сая\Desktop\pp2-22B030300\tsis7\clockmickey\second.png"')
done = False

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(60)