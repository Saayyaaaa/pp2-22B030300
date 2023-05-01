import pygame
import random

# Определяем размер экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Определяем размер клетки и количество клеток на экране
CELL_SIZE = 20
CELL_WIDTH = SCREEN_WIDTH // CELL_SIZE
CELL_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализируем pygame
pygame.init()

# Создаем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Создаем таймер
clock = pygame.time.Clock()

# Определяем начальное положение змейки и направление ее движения
snake_head = [CELL_WIDTH // 2, CELL_HEIGHT // 2]
snake_body = [[snake_head[0], snake_head[1] + i] for i in range(-2, 1)]
direction = 'up'

# Создаем еду для змейки в случайном месте на экране
food = [random.randint(0, CELL_WIDTH - 1), random.randint(0, CELL_HEIGHT - 1)]

# Функция отрисовки змейки и еды на экране
def draw(screen, snake_body, food):
    # Отрисовываем змейку
    for i, pos in enumerate(snake_body):
        if i == 0:
            color = GREEN
        else:
            color = WHITE
        pygame.draw.rect(screen, color, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отрисовываем еду
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'

    # Двигаем змейку
    if direction == 'up':
        snake_head[1] -= 1
    elif direction == 'down':
        snake_head[1] += 1
    elif direction == 'left':
        snake_head[0] -= 1
    elif direction == 'right':
        snake_head[0] += 1

    # Проверяем, не вышла ли змейка за пределы экрана
    if snake_head[0] < 0 or snake_head[0] >= CELL_WIDTH or snake_head[
