#Shooting_game.py
import pygame
import sys
pygame.init()

######
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
pink = (255, 133, 215)
orange = (240, 155, 89)
#####



w = 480
h = 640

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption('Shooting Game') #제목 설정

pad.fill(yellow)



#pygame.draw.line(pad,red,(0,210),(480,210),5)           #선 그리기
#pygame.draw.line(pad,red,(240,0),(240,640),5)           #선 그리기
pygame.draw.circle(pad,blue,(240,310),250,0)           #원 그리기
#pygame.draw.circle(pad,blue,(360,100),50,0)           #원 그리기
pygame.draw.rect(pad,black,(70,250,340,200),0)           #사각형 그리기
#pygame.draw.polygon(pad,pink,((100,100),(20,200),(170,200),(220,100)))
pygame.draw.ellipse(pad,pink,(300,150,100,50),0)
pygame.draw.ellipse(pad,pink,(75,150,100,50),0)
pygame.draw.line(pad,((75,75,75)),(71,345),(409,345),5)
pygame.draw.rect(pad,white,(71,347,168,103),0)
pygame.draw.rect(pad,red,(242,250,168,93),0)
pygame.display.update() #화면 업데이트

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
