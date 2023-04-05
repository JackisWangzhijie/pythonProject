import tkinter as tk
import pygame
import random

# 定义游戏区域的大小和每个格子的大小
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20

# 初始化pygame和Tkinter
pygame.init()
root = tk.Tk()

# 创建画布和游戏区域
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
game_area = canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")

# 定义贪吃蛇的初始位置和长度
snake = [(0, 0)]
snake_length = 1

# 定义贪吃蛇的移动方向
dx = 1
dy = 0

# 定义食物的位置
food = (random.randint(0, WIDTH // GRID_SIZE - 1), random.randint(0, HEIGHT // GRID_SIZE - 1))


# 定义游戏循环函数
def game_loop():
    global snake, snake_length, dx, dy, food

    # 移动贪吃蛇
    x, y = snake[-1]
    x += dx
    y += dy
    snake.append((x, y))

    # 判断是否吃到食物
    if snake[-1] == food:
        food = (random.randint(0, WIDTH // GRID_SIZE - 1), random.randint(0, HEIGHT // GRID_SIZE - 1))
        snake_length += 1

    # 判断是否撞到边界或自己的身体
    if x < 0 or x >= WIDTH // GRID_SIZE or y < 0 or y >= HEIGHT // GRID_SIZE or (x, y) in snake[:-1]:
        # 游戏结束
        print("Game over!")
        root.destroy()
        return

    # 删除贪吃蛇的尾部
    if len(snake) > snake_length:
        snake.pop(0)

    # 重新绘制游戏区域
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x * GRID_SIZE, y * GRID_SIZE, (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE, fill="green",
                                tags="snake")
    canvas.create_rectangle(food[0] * GRID_SIZE, food[1] * GRID_SIZE, (food[0] + 1) * GRID_SIZE,
                            (food[1] + 1) * GRID_SIZE, fill="red", tags="food")

    # 延迟一段时间后再次运行游戏循环函数
    root.after(100, game_loop)


# 绑定键盘事件，控制贪吃蛇的移动方向
def on_key_press(event):
    global dx, dy
    if event.keysym == "Up":
        dx = 0
        dy = -1
    elif event.keysym == "Down":
        dx = 0
        dy = 1
    elif event.keysym == "Left":
        dx = -1
        dy = 0
    elif event.keysym == "Right":
        dx = 1
        dy = 0

# 绑定键盘事件到画布上
canvas.bind_all("<Key>", on_key_press)

# 开始游戏循环
game_loop()

# 运行Tkinter的消息循环
root.mainloop()