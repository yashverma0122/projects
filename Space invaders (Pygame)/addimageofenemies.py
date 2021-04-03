import pygame
import random
import math
from pygame import mixer
pygame.init()
mixer.music.load('background.wav')
mixer.music.play(-1)
screen=pygame.display.set_mode((800,600))
running=True
pygame.display.set_caption("MY SPACE GAME")
icon=pygame.image.load('sship.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('playerimg.png')
background=pygame.image.load('back.png')
playerX=370
playerY=480

player_change=0
score =0
enemyimg=[]
enemyX=[]
enemyY=[]
enemyx_change=[]
enemyY_change=[]

enemy_change=5
noofenemies=6
for i in range(noofenemies):
    enemyimg.append(pygame.image.load('enemyimg.png'))
    enemyX.append(random.randint(0,770))
    enemyY.append(random.randint(50,130))
    enemyx_change.append(4)
    enemyY_change.append(40)


score_value = 0
font = pygame.font.Font('comicsans.ttf', 32)

textX = 10
testY = 10



def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))



bulletimg=pygame.image.load('bullet.png')
#bullet ready state means not fire
# #bullet fire state means currently fire
bulletX=370
bulletY=480
bullet_changeX=10
bullet_changeY=10
bullet_state='ready'


def player(x,y):
    screen.blit(playerimg,(x,y))#here blits means draw
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global  bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+15,y+10))
def iscollision(eneymX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(eneymX-bulletX,2))+((math.pow(enemyY-bulletY,2))))
    if distance<27:
        return True

    else:
        return  False
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_change=-3
            elif event.key==pygame.K_RIGHT:
                player_change=3
            elif event.key == pygame.K_SPACE:
                bulletsound=mixer.Sound('laser.wav')
                bulletsound.play()
                fire_bullet(playerX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_change=0

    #seting background colour from colour picker(rgb)
    #screen.fill((193,118,171))
    playerX=playerX+player_change
    if playerX<=0:
        playerX=0
    if playerX>=740:
        playerX=740
    player(playerX,playerY)

    for i in range(noofenemies):

        enemyX[i] = enemyX[i] + enemyx_change[i]

        if enemyX[i] <= 0:

            enemyX[i] = 0
            enemyY[i] = enemyY[i] + 20
            enemyx_change[i]=5

        if enemyX[i] >= 740:
            enemyX[i] = 740
            enemyY[i]= enemyY[i] + 20
            enemyx_change[i]=-5
        collission = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if collission:
            esound = mixer.Sound('explosion.wav')
            esound.play()
            bullet_state = ' ready'
            bulletY = 480
            score_value = score_value + 1

            enemyX[i] = 370
            enemyX[i] = 50
            print(score)

        enemy(enemyX[i], enemyY[i],i)
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY-=bullet_changeY

    show_score(textX, testY)
    pygame.display.update()
