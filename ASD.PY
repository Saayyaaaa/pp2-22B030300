import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
BLUE = pg.Color('dodgerblue')
points = [(200, 200), (250, 250), (200, 300), (150, 250)]

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(BG_COLOR)
    pg.draw.polygon(screen, BLUE, points)
    pg.display.flip()
    clock.tick(60)