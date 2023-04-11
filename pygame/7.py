import time
import random
 
import pygame
 
if __name__ == '__main__':
    coords = []
    koef = 1
    with open(r'C:\Users\Сая\Desktop\pp2-22B030300\pygame\points.txt', 'r', encoding='UTF8') as f:
        data = f.read().split(', ')
    for i in data:
        x, y = i[1:-1].split(';')
        x = float(x.replace(',', '.')) + 250
        y = float(y.replace(',', '.')) * -1 + 250
        coords.append([x, y])
    print(data)
    pygame.init()
    pygame.display.set_caption('К щелчку')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    fps = random.randint(40, 144)
    kx, ky = 1, 1
    x, y = 250, 250
    dx, dy = 0, 0
    x1, y1 = 0, 0
    running = True
    pygame.draw.polygon(screen, (255, 255, 255), coords, 1)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:'''
            if event.type == pygame.MOUSEWHEEL and pygame.mouse.get_pressed(3):
                print(pygame.mouse.get_pressed(3))
                koef = 1.3
            if event.type == pygame.MOUSEWHEEL and pygame.mouse.get_pressed(5):
                koef = 0.7
            for j in coords:
                j[0] = (j[0] - 250) * koef + 250
                j[1] = (j[1] - 250) * koef + 250
            screen.fill((0, 0, 0))
            pygame.draw.polygon(screen, (255, 255, 255), coords, 1)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()