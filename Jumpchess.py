import tkinter as tk

# 设置棋盘大小和格子数量
BOARD_SIZE = 600
GRID_NUM = 8

class Checkerboard:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        # 绘制棋盘
        for i in range(GRID_NUM):
            for j in range(GRID_NUM):
                x1 = j * (BOARD_SIZE / GRID_NUM)
                y1 = i * (BOARD_SIZE / GRID_NUM)
                x2 = (j + 1) * (BOARD_SIZE / GRID_NUM)
                y2 = (i + 1) * (BOARD_SIZE / GRID_NUM)
                if (i + j) % 2 == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

    def draw_pieces(self):
        # 绘制棋子
        for i in range(GRID_NUM):
            for j in range(GRID_NUM):
                if (i + j) % 2 != 0 and i < 3:
                    x = j * (BOARD_SIZE / GRID_NUM) + (BOARD_SIZE / GRID_NUM) / 2
                    y = i * (BOARD_SIZE / GRID_NUM) + (BOARD_SIZE / GRID_NUM) / 2
                    self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red")
                elif (i + j) % 2 != 0 and i > 4:
                    x = j * (BOARD_SIZE / GRID_NUM) + (BOARD_SIZE / GRID_NUM) / 2
                    y = i * (BOARD_SIZE / GRID_NUM) + (BOARD_SIZE / GRID_NUM) / 2
                    self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("跳棋游戏")
    checkerboard = Checkerboard(root)
    root.mainloop()