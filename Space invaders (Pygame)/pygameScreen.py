import pygame
pygame.init()
#creating the screen
screen=pygame.display.set_mode((800,600))
running=True
#infinit loop for stop the window
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=false
