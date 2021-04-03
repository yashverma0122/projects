import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
running=True
pygame.display.set_caption("MY SPACE GAME")
icon=pygame.image.load('sship.png')
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #seting background colour from colour picker(rgb)
    screen.fill((193,118,171))
    pygame.display.update()
