import pygame
# import random
from block import Block
from board import Board
win = pygame.display.get_surface()
# ---------------Türkis--------Gelb-----------Lila-----------Grün---------Rot----------Blau---------Orange
block_colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]

"""""
def neuer_spielstein():
    global random_color, block_x, block_y, block_speed
    pygame.draw.rect(win, block_colors[random_color], (block_x, block_y + block_speed, block_size, block_size))
"""""


# Board.draw_background(win)
pygame.init()


bRun = True
while bRun:
    pygame.time.delay(100)
    #win.fill(0, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False
    # Board.play()
    pygame.display.update()
pygame.quit()
