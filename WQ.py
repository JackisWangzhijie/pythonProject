import turtle

# 定义棋盘大小和格子大小
board_size = 600
grid_size = board_size // 19

# 初始化画布和画笔
canvas = turtle.Screen()
canvas.bgcolor("white")
canvas.setup(board_size + 100, board_size + 100)
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# 绘制棋盘线条
pen.penup()
pen.goto(-board_size // 2, board_size // 2)
pen.pendown()
for i in range(19):
    pen.forward(board_size)
    pen.penup()
    pen.backward(board_size)
    pen.right(90)
    pen.forward(grid_size)
    pen.left(90)
    pen.pendown()

# 绘制星位
star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9), (15, 9), (3, 15), (9, 15), (15, 15)]
pen.penup()
for x, y in star_points:
    pen.goto((x - 9) * grid_size, (9 - y) * grid_size)
    pen.dot(5)

# 显示画布
canvas.mainloop()
