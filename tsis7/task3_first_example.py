import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
clock = pygame.time.Clock()
color = (255, 0, 0)
x = 25
y = 25
White = (255,255,255)

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if x>25:
                            x -= 20
                    if event.key == pygame.K_RIGHT:
                        if x<365:
                            x += 20
                    if event.key == pygame.K_DOWN:
                        if y<365:
                            y += 20
                    if event.key == pygame.K_UP:
                        if y>25:
                            y -= 20

        screen.fill(White)       
        pygame.draw.circle(screen, color, [x, y], 25, 0)
        pygame.display.flip()

        
        clock.tick(100)