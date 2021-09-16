import time

import pygame
from pygame.rect import Rect
from pygame.time import Clock

size = [500, 300]
pygame.init()
screen = pygame.display.set_mode(size)
color = (255, 255, 255)
screen.fill(color)
pygame.display.flip()

dino = pygame.image.load("images/d1.png")

position = Rect(50, 100, 0, 0)

pygame.display.flip()
done = 0
position = Rect(50, 100, 0, 0)

clock = Clock()  # 设置时钟
while not done:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = 1
            break
    position = position.move([10, 0])  # 每次往前移动10
    screen.fill(color)  # 一定要重新填充背景色，否则移动时会留下上次的影子
   # screen.blit(dino, position)

    pygame.display.flip()


pygame.quit()
