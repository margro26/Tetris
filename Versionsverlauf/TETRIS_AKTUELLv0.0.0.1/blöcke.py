import pygame
import random

# ---------------Türkis--------Gelb-----------Lila-----------Grün---------Rot----------Blau---------Orange
#block_colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]
#block_form = [()]

class Blöcke:
    def block_1():
        rc1 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc1]), (int(block_x), int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc1]), (int(block_x) + 20, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc1]), (int(block_x) + 40, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc1]), (int(block_x) + 60, int(block_y), 20, 20))


    def block_2():
        rc2 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc2]), (int(block_x), int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc2]), (int(block_x), int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc2]), (int(block_x) + 20, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc2]), (int(block_x) + 40, int(block_y) + 20, 20, 20))


    def block_3():
        rc3 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc3]), (int(block_x), int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc3]), (int(block_x) + 20, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc3]), (int(block_x) + 40, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc3]), (int(block_x) + 40, int(block_y), 20, 20))


    def block_4():
        rc4 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc4]), (int(block_x), int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc4]), (int(block_x), int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc4]), (int(block_x) + 20, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc4]), (int(block_x) + 20, int(block_y) + 20, 20, 20))


    def block_5():
        rc5 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc5]), (int(block_x) + 20, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc5]), (int(block_x) + 40, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc5]), (int(block_x), int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc5]), (int(block_x) + 20, int(block_y) + 20, 20, 20))


    def block_6():
        rc6 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc6]), (int(block_x), int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc6]), (int(block_x) + 20, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc6]), (int(block_x) + 40, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc6]), (int(block_x) + 20, int(block_y), 20, 20))


    def block_7():
        rc7 = random.randint(0, 6)
        pygame.draw.rect(win, (block_colors[rc7]), (int(block_x), int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc7]), (int(block_x) + 20, int(block_y), 20, 20))
        pygame.draw.rect(win, (block_colors[rc7]), (int(block_x) + 20, int(block_y) + 20, 20, 20))
        pygame.draw.rect(win, (block_colors[rc7]), (int(block_x) + 40, int(block_y) + 20, 20, 20))

"""""
block_size = 10
board_width = block_size * 16
board_height = block_size * 20
block_speed = 5
block_x = block_size * 16 / 2
block_y = 50
random_color = random.randint(0, 6)


pygame.init()
pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Tetris")
win = pygame.display.get_surface()
bRun = True
while bRun:
    pygame.time.delay(100)
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    # pygame.draw.rect(win, block_colors[random_color], (block_x, block_y + block_speed, block_size, block_size))
    # block_speed += 5
    # if block_speed >= block_size * 20 - 70:
    #     block_speed = 0
    #     random_color = random.randint(0, 6)
    #     block_x = random.randint(0, 380)
    random_block = random.randint(0, 6)
    if random_block == 0:
        block_1()
    elif random_block == 1:
        block_2()
    elif random_block == 2:
        block_3()
    elif random_block == 3:
        block_4()
    elif random_block == 4:
        block_5()
    elif random_block == 5:
        block_6()
    elif random_block == 6:
        block_7()
    pygame.display.update()
"""""