__author__ = "chiara@sabaini.com"
__version__ = "2.0"
__date__ = "2020-05-07"

import time
import random
from copy import deepcopy
ALIVE = 1
DEAD = 0

board = []

def board_init(h, w):
    """Initializassigning a random state (1: alive, 0: dead) to every cell."""
    global board
    board = []

    for y in range(h):
        row = []

        for x in range(w):
            row.append(random.randint(0, 1))

        board.append(row)

    return board

def count_neighbours(x, y):
    """Counts how many cells around the one with the given coordinates are alive."""
    global board

    neighbours = 0

    for i in range(x - 1, x + 2):
        if i > 0:
            for j in range(y - 1, y + 2):
                if j > 0:
                    if not (j == y and i == x):
                        try:
                            if board[i][j] == ALIVE:
                                neighbours += 1
                        except:
                            pass

    return neighbours

def update():
    """Updates the board"""
    global board

    next_board = deepcopy(board)
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            neighbours = count_neighbours(x ,y)

            if board[x][y] == ALIVE and (neighbours < 2 or neighbours > 3):
                next_board[x][y] = 0

            if board[x][y] == DEAD and neighbours == 3:
                next_board[x][y] = 1
                
    board = next_board

def show():
    """Shows the board with * where the cell is alive and a space when the cell is dead."""
    global board

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()

    print("---")
    
def game_of_life(h, w):
    """This function is the one that make the game run"""
    board_init(h, w)
    show()

    while True:
        update()
        show()
        time.sleep(0.25)
    
def main(h, w):
    game_of_life(h, w)

if __name__ == "__main__":
    main(8, 12)