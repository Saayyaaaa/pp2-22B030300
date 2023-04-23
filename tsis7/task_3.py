import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
White = (255,255,255)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if y > 30:
                y -= 20
        if pressed[pygame.K_DOWN]:
            if y < 355:
                y += 20
        if pressed[pygame.K_LEFT]:
            if x > 30:
                x -= 20
        if pressed[pygame.K_RIGHT]:
            if x < 355:
                x += 20
        
        screen.fill((White))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, color, [x, y], 25, 0)
        
        pygame.display.flip()
        clock.tick(40)