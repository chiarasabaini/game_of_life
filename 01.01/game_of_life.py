__author__ = "chiara@sabaini.com"
__version__ = "1.0"
__date__ = "2020/04/1"

import time
import random
from copy import deepcopy
board = []

def board_init(h, w):
    global board
    board = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append(random.randint(0, 1))
        board.append(row)

def count_neighbours(x, y):
    neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (j == y and i == x):
                try:
                    if board[i][j] == 1:
                        neighbours += 1
                except:
                    pass
    return neighbours

def update():
    global board
    next_board = deepcopy(board)
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            neighbours = count_neighbours(x ,y)
            if board[x][y] == 1 and (neighbours < 2 or neighbours > 3):
                next_board[x][y] = 0
            if board[x][y] == 0 and neighbours == 3:
                next_board[x][y] = 1
    board = next_board

def show(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("---")
    
def game_of_life(h, w):
    board_init(h, w)
    show(board)
    while True:
        update()
        show(board)
        time.sleep(0.25)
    
def run(h, w):
    game_of_life(h, w)

if __name__ == "__main__":
    run(8, 12)