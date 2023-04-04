import pygame
import math
import datetime
pygame.init()

display=pygame.display.set_mode((800,800))
pygame.display.set_caption("Clock")

clock=pygame.time.Clock()

FPS=50
def print_text(text,position):
    font=pygame.font.SysFont("Castellar",40,True,False)
    surface=font.render(text,True,(0,0,0))
    display.blit(surface,position)
def show_numbers(R,theta):
    
    y=math.cos(2*math.pi*theta/360)*R
    x=math.sin(2*math.pi*theta/360)*R
    return x+400-15,-(y-400)-20
def show_lines(R,theta):
    
    y=math.cos(2*math.pi*theta/360)*R
    x=math.sin(2*math.pi*theta/360)*R
    return x+400,-(y-400)
def game():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        current_time=datetime.datetime.now()
        second=current_time.second
        minute=current_time.minute
        hour=current_time.hour
        display.fill((255,255,255))
        pygame.draw.circle(display,(0,0,0),(400,400),400,4)
        for line in range(1,61):
            pygame.draw.line(display,(0,0,0),(400,400),show_lines(395,line*6),4)
        pygame.draw.circle(display,(255,255,255),(400,400),380)

        for line in range(1,13):
            pygame.draw.line(display,(255,0,0),(400,400),show_lines(395,line*30),4)
        pygame.draw.circle(display,(255,255,255),(400,400),375)
        for number in range(1,13):
            print_text(str(number),show_numbers(350,number*30))
        
        #second
        R=300
        theta=second*(360/60)
        pygame.draw.line(display,(255,0,0),(400,400),show_lines(R,theta),3)
        #minute
        R=350
        theta=(minute+second/60)*(360/60)
        pygame.draw.line(display,(0,0,0),(400,400),show_lines(R,theta),3)

        #hour
        R=280
        theta=(hour+minute/60+second/3600)*(360/12)
        pygame.draw.line(display,(255,255,0),(400,400),show_lines(R,theta),4)
        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()