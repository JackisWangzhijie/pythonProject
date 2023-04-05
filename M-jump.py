import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# set the size of the game board
UI_WIDTH, UI_HEIGHT = 600, 600

# set the size of the game board cell
GRID_HEIGHT, GRID_WIDTH = 40, 40

# set the size of the game board's rows and columns
ROWS, COLS = int(UI_HEIGHT / GRID_HEIGHT), int(UI_WIDTH / GRID_WIDTH)

# initialize the game board
game_board = [[0 for j in range(COLS)] for i in range(ROWS)]

# initialize the pygame
pygame.init()

# set the size of the screen
SIZE = (UI_WIDTH, UI_HEIGHT)
screen = pygame.display.set_mode(SIZE)

# set the title of the screen
pygame.display.set_caption("Gobang Game")

# set the background color of the screen
screen.fill(WHITE)

# set font for the scoreboard
scoreFont = pygame.font.Font(None, 30)

# set the player turn
player_turn = True

# set the messages of the scoreboard
player_messages = ["Black Chess", "White Chess"]
WINNER_MSG = "Winner: "
TIE_MSG = "Tie game!"


# draw the game board and scoreboard
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, [col * GRID_WIDTH, row * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT], 1)


def draw_chess_piece(row, col, playerTurn):
    x = col * GRID_WIDTH + GRID_WIDTH // 2
    y = row * GRID_HEIGHT + GRID_HEIGHT // 2
    color = BLACK if playerTurn else RED
    pygame.draw.circle(screen, color, [x, y], 15)


# check if the current player has won the game or not
def check_win(row, col, val):
    # check rows
    for r in range(row - 4, row + 1):
        if r < 0 or r + 4 >= ROWS:
            continue
        if game_board[r][col] == val and game_board[r + 1][col] == val and game_board[r + 2][col] == val and \
                game_board[r + 3][col] == val and game_board[r + 4][col] == val:
            return True

    # check columns
    for c in range(col - 4, col + 1):
        if c < 0 or c + 4 >= COLS:
            continue
        if game_board[row][c] == val and game_board[row][c + 1] == val and game_board[row][c + 2] == val and \
                game_board[row][c + 3] == val and game_board[row][c + 4] == val:
            return True

    # check diagonals
    for r in range(row - 4, row + 1):
        for c in range(col - 4, col + 1):
            if r < 0 or r + 4 >= ROWS or c < 0 or c + 4 >= COLS:
                continue
            if game_board[r][c] == val and game_board[r + 1][c + 1] == val and game_board[r + 2][c + 2] == val and \
                    game_board[r + 3][c + 3] == val and game_board[r + 4][c + 4] == val:
                return True

    # check anti-diagonals
    for r in range(row + 4, row - 1, -1):
        for c in range(col - 4, col + 1):
            if r >= ROWS or r - 4 < 0 or c < 0 or c + 4 >= COLS:
                continue
            if game_board[r][c] == val and game_board[r - 1][c + 1] == val and game_board[r - 2][c + 2] == val and \
                    game_board[r - 3][c + 3] == val and game_board[r - 4][c + 4] == val:
                return True

    return False


# check if the game is tied or not
def check_tie():
    for row in range(ROWS):
        for col in range(COLS):
            if game_board[row][col] == 0:
                return False
    return True


# draw scoreboard
def draw_scoreboard(row, col):
    player_one_turn_or_winner = WINNER_MSG if check_win(row, col, 1) else (
        player_messages[0] if player_turn else player_messages[1])
    player_two_turn_or_winner = WINNER_MSG if check_win(row, col, 2) else (
        player_messages[1] if player_turn else player_messages[0])

    if check_tie() and not check_win(row, col, 1) and not check_win(row, col, 2):
        p1_scores = scoreFont.render("Score: TIE", True, BLACK)
        p2_scores = scoreFont.render("Score: TIE", True, BLACK)
    else:
        p1_scores = scoreFont.render("Score: " + str(check_win(row, col, 1)).upper(), True, BLACK)
        p2_scores = scoreFont.render("Score: " + str(check_win(row, col, 2)).upper(), True, BLACK)

    p1_turn = scoreFont.render(player_one_turn_or_winner, True, BLACK)
    p2_turn = scoreFont.render(player_two_turn_or_winner, True, BLACK)
    reset_message = scoreFont.render("Press C to reset the game!", True, BLACK)
    screen.blit(p1_scores, (0, 0))
    screen.blit(p1_turn, (0, 35))
    screen.blit(p2_scores, ((UI_WIDTH - p2_scores.get_width()), 0))
    screen.blit(p2_turn, ((UI_WIDTH - p2_turn.get_width()), 35))
    screen.blit(reset_message,
                ((UI_WIDTH - reset_message.get_width()) // 2, (UI_HEIGHT - reset_message.get_height())))


draw_board()

x, y = 0,0

# game loop
game_running = True
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                x, y = event.pos
                col, row = int(x / GRID_WIDTH), int(y / GRID_HEIGHT)
                if game_board[row][col] == 0:
                    draw_chess_piece(row, col, player_turn)
                    game_board[row][col] = 1 if player_turn else 2
                    if check_win(row, col, 1):
                        print("Black Chess win!")
                        game_running = False
                    if check_win(row, col, 2):
                        print("White Chess win!")
                        game_running = False
                    if check_tie():
                        print(TIE_MSG)
                        game_running = False
                    player_turn = not player_turn

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # reset the game
                game_board = [[0 for j in range(COLS)] for i in range(ROWS)]
                player_turn = True
                screen.fill(WHITE)
                draw_board()
                continue

    # draw the screen
    draw_scoreboard(int(x / GRID_WIDTH), int(y / GRID_HEIGHT))
    pygame.display.flip()

# quit the game
pygame.quit()
