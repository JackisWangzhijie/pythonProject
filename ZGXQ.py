import pygame
from pygame.locals import *

# 设置游戏界面尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# 棋盘尺寸
BOARD_SIZE = 9

# 棋子尺寸
PIECE_SIZE = 50

# 棋盘颜色
BOARD_COLOR = (235, 170, 95)

# 棋子颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定义棋子初始位置
piece_pos = [
    ((0, 0), "車"),
    ((1, 0), "馬"),
    ((2, 0), "相"),
    ((3, 0), "士"),
    ((4, 0), "帥"),
    ((5, 0), "士"),
    ((6, 0), "象"),
    ((7, 0), "馬"),
    ((8, 0), "車"),
    ((0, 9), "車"),
    ((1, 9), "馬"),
    ((2, 9), "象"),
    ((3, 9), "士"),
    ((4, 9), "將"),
    ((5, 9), "士"),
    ((6, 9), "象"),
    ((7, 9), "馬"),
    ((8, 9), "車"),
    ((1, 2), "炮"),
    ((7, 2), "炮"),
    ((0, 3), "兵"),
    ((2, 3), "兵"),
    ((4, 3), "兵"),
    ((6, 3), "兵"),
    ((8, 3), "兵"),
    ((0, 6), "卒"),
    ((2, 6), "卒"),
    ((4, 6), "卒"),
    ((6, 6), "卒"),
    ((8, 6), "卒")
]

# 初始化棋子位置
pieces = {}
for pos, name in piece_pos:
    x, y = pos
    pieces[(x, y)] = name

# 初始化Pygame
pygame.init()

# 设置游戏界面
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("中国象棋")

# 加载棋子图片
black_pieces = {}
red_pieces = {}
for name in set(pieces.values()):
    black_pieces[name] = pygame.image.load(f"images/black_{name}.png").convert_alpha()
    red_pieces[name] = pygame.image.load(f"images/red_{name}.png").convert_alpha()

# 定义绘制棋盘的函数
def draw_board():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            # 绘制棋盘格子
            rect = pygame.Rect(x * PIECE_SIZE, y * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE)
            pygame.draw.rect(screen, BOARD_COLOR, rect)

            # 绘制棋子
            piece = pieces.get((x, y), None)
            if piece:
                if piece.isupper():
                    img = black_pieces[piece]
                else:
                    img = red_pieces[piece]
                img_rect = img.get_rect()
                img_rect.center = rect.center
                screen.blit(img, img_rect)

def handle_click(pos):
# 将鼠标点击位置转换为棋子位置
x, y = pos[0] // PIECE_SIZE, pos[1] // PIECE_SIZE

