import sys

import pygame

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色
screen.fill(color)
pygame.display.update()
ball = pygame.image.load('ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域
clock = pygame.time.Clock()
print(ballrect)
speed = [5, 5]  # 设置移动的X轴、Y轴
while True:  # 死循环确保窗口一直显示
    clock.tick(150)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)  # 移动小球

    if ballrect.left <= 0 or ballrect.right >= width:
        speed[0] = -speed[0]

    if ballrect.top <= 0 or ballrect.bottom >= height:
        speed[1] = -speed[1]
    screen.blit(ball, ballrect)  # 将图片画到窗口的什么位置上
    pygame.display.update()  # 更新全部显示

pygame.quit()  # 退出pygame
