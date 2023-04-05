import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口和画布大小
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400

# 创建窗口和画布
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
canvas = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))

# 设置画笔初始位置和颜色
x, y = CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2
color = (255, 192, 203)

# 主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 填充背景色
    canvas.fill((255, 255, 255))

    # 画小猪
    pygame.draw.circle(canvas, color, (x, y), 100, 0)
    pygame.draw.circle(canvas, (0, 0, 0), (x - 40, y - 20), 20)
    pygame.draw.circle(canvas, (0, 0, 0), (x + 40, y - 20), 20)
    pygame.draw.line(canvas, (139, 69, 19), (x - 60, y - 40), (x + 60, y - 40), 20)

    # 将画布绘制到窗口
    screen.blit(canvas, (50, 50))

    # 刷新窗口
    pygame.display.update()

# 退出pygame
pygame.quit()
