# 创建一个游戏，画面正中是一个红色小球，画面1/4位置出现一个蓝色小球，然后蓝色小球围绕着红色小球开始转，10圈后，程序退出

import turtle

# 创建画布和画笔
canvas = turtle.Screen()
pen = turtle.Turtle()

# 绘制实心红色圆
pen.penup()
pen.goto(0, 0)
pen.dot(50, "red")

# 绘制实心蓝色小球
pen.penup()
pen.goto(100, 0)
pen.dot(20, "blue")

# 让蓝球围绕红圆转10圈
for i in range(10):
    pen.goto(0, 0)  # 将画笔移动到红圆中心
    pen.right(36)   # 使蓝球绕红圆转一圈所需的角度为36度
    pen.goto(100, 0) # 将画笔移动到蓝球位置
