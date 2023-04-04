import pygame
import random

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos, color, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((10, 10))
        self.image.set_colorkey((1, 2, 3))
        self.image.fill((1, 2, 3))
        
        pygame.draw.rect(self.image, pygame.Color(color), [0, 0, 10, 10])
        self.rect = self.image.get_rect(center=pos)

def level():
    screen = pygame.display.set_mode((800, 600))
    colors = ['yellow']

    sprites = pygame.sprite.Group()
    objects = pygame.sprite.Group()
    for _ in range(20):
        pos = random.randint(100, 700), random.randint(100, 600)
        Rectangle(pos, random.choice(colors), sprites, objects)

    for sprite in objects:
        sprite.mask = pygame.mask.from_threshold(sprite.image, pygame.Color('yellow'), (1, 1, 1, 255))

    player = Rectangle(pygame.mouse.get_pos(), 'dodgerblue', sprites)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                return
        player.rect.center = pygame.mouse.get_pos()
        if pygame.sprite.spritecollideany(player, objects, pygame.sprite.collide_mask):
            screen.fill((255, 255, 255))
        else:
            screen.fill((30, 30, 30))
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
main()