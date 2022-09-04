import pygame
from pygame.locals import *
import math
import random
import sys
import time


pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100,100]
arrows = []
healthvalue = 35
pygame.mixer.init()

mainClock = pygame.time.Clock()
player = pygame.image.load('sprites/0 to sides going.png')
grass = pygame.image.load('Graphics/grass.png')
arrow = pygame.image.load('Graphics/bullet.png')
healthbar = pygame.image.load('Graphics/Healthbar empty.png')
health = pygame.image.load('Graphics/Health bar.png')
running = 1
exitcode = 0

LEFT = 1

while running:
    screen.fill(0)
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))  

    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 720-angle*17.5)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    screen.blit(healthbar, (6,7))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            position=pygame.mouse.get_pos()
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5

    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
    pygame.display.flip()



