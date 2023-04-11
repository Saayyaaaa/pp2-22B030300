import pygame #import pygame — обеспечивает доступ к фреймворку pygame и импортирует все функции pygame.
 
pygame.init() #pygame.init() — используется для инициализации всех необходимых модулей pygame.
screen = pygame.display.set_mode((400,500)) #используется для отображения окна нужного размера
done = False 
 
while not done: 
    for event in pygame.event.get(): #pygame.event.get() — очищает очередиь событий
        if event.type == pygame.QUIT: #pygame.QUIT — используется для завершения события, когда мы нажимаем кнопку закрытия в углу окна
            done = True 
    pygame.display.flip() 

    # pygame.display.flip() — Pygame использует двойную буферизацию, поэтому буферы смещаются.
    # Очень важно вызвать эту функцию, чтобы сделать видимыми любые обновления, которые вы делаете на игровом экране.