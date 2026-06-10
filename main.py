import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1280
altura = 720
clock = pygame.time.Clock()

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cat Runner")

while True:
    clock.tick(60)
    display.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            ...    

     
    pygame.display.update()
    