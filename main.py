# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import pygame
import random

# 初始化pygame库
pygame.init()

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 定义窗口大小
display_width = 800
display_height = 600

# 创建游戏窗口
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# 定义蛇的大小和速度
snake_block = 10
snake_speed = 15

# 定义字体
font_style = pygame.font.SysFont(None, 30)

# 定义函数来显示消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])

# 定义函数来画蛇
def draw_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(gameDisplay, green, [x[0], x[1], snake_block, snake_block])

# 定义游戏主循环
def gameLoop():
    gameExit = False
    gameOver = False

    # 定义蛇的起始位置和长度
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snake_List = []
    Length_of_snake = 1

    # 在随机位置创建一个数字
    randAppleX = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message("Game Over, press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # 检测用户按键
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # 检测用户按键
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_block
            elif event.key == pygame.K_DOWN:
                lead_y_change = snake_block
                lead_x_change = 0

    # 检测蛇是否撞到边界
    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameOver = True

    # 更新蛇的位置
    lead_x += lead_x_change
    lead_y += lead_y_change

    # 绘制背景
    gameDisplay.fill(white)

    # 绘制数字
    pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, snake_block, snake_block])

    # 将蛇的位置添加到列表中
    snake_Head = []
    snake_Head.append(lead_x)
    snake_Head.append(lead_y)
    snake_List.append(snake_Head)

    # 如果蛇的长度超过Length_of_snake，则删除列表的第一个元素
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    # 检测蛇是否吃到数字
    if lead_x == randAppleX and lead_y == randAppleY:
        randAppleX = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        randAppleY = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    # 绘制蛇
    draw_snake(snake_block, snake_List)

    # 更新窗口
    pygame.display.update()

    # 控制蛇的速度
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# 退出游戏
pygame.quit()
quit()
