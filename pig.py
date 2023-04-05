import turtle

# 设置画笔
t = turtle.Pen()

# 鼻子
t.speed(0)
t.penup()
t.goto(0, 100)
t.pendown()
t.left(45)
t.forward(60)
t.right(90)
t.circle(60, -90)

# 头
t.right(180)
t.circle(-60, 180)
t.right(180)

# 身体
t.circle(-120, 180)
t.right(180)

# 脚
t.forward(80)
t.left(90)
t.forward(40)
t.right(180)
t.circle(40, -180)
t.right(180)
t.forward(40)

# 画完后隐藏画笔
t.hideturtle()

# 保持窗口不会自动关闭
turtle.done()
