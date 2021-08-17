__author__ = "chiara"
__version__ = "2.0"
__date__ = "2020-05-07"

import pygame
import cli as gol
import pygame.locals as pl

pygame.init()

GAME_RES = WIDTH, HEIGHT = 256, 256
FPS = 30
CELL_SIZE = 4
CELL_COLOR = (55, 0, 255)
GAME_TITLE = 'GAME OF LIFE by Chiara Sabaini'

window = pygame.display.set_mode(GAME_RES, pl.HWACCEL|pl.HWSURFACE|pl.DOUBLEBUF) # Sets the window
pygame.display.set_caption(GAME_TITLE) # Sets the game title
clock = pygame.time.Clock()

# Game Values

background_color = (0, 0, 0) # RGB value
gol.board_init(WIDTH, HEIGHT)

# End of Game Values

# Game loop
game_running = True
while game_running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pl.QUIT:
            game_running  = False
            break
        if event.type == pl.KEYDOWN:
            if event.key == pl.K_ESCAPE:
                game_running  = False
                break
            if event.key == pl.K_SPACE:
                gol.board_init(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE) # Reinitializes the board when the space key is pressed

    # Game logic
    gol.update()

    # Display update
    pygame.Surface.fill(window, background_color)
    
    for x in range(len(gol.board)):
        for y in range(len(gol.board[x])):
            if gol.board[x][y] == 1:
                pygame.draw.rect(window, CELL_COLOR, [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE])

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
