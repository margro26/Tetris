import random
import pygame
from spielsteine import Spielsteine
class Board:
    def __init__(self):
        self.block_size = 20
        self.board_width = self.block_size * 16
        self.board_height = self.block_size * 20
        self.blocks_per_row = self.board_width / 20
        self.active_block = True
        # self.blocks_per_col

    def draw_playgound(self, win):
        win.fill((0, 0, 0))
        pygame.display.set_mode((self.board_width, self.board_height))
        pygame.display.set_caption("Tetris")
    def play(self):
        gedrueckt = pygame.key.get_pressed()

        if gedrueckt[pygame.K_DOWN]:
            block_speed += 100
        elif gedrueckt[pygame.K_LEFT]:
            if block_x >= 10:
                block_x -= 10
            else:
                print("Sie haben das Ende des Spielfeldes erreicht!")
        elif gedrueckt[pygame.K_RIGHT]:
            if block_x <= self.board_width - 30:
                block_x += 10
            else:
                print("Sie haben das Ende des Spielfeldes erreicht!")

        Spielsteine.drop()


    # def get_width(self):
    # def get_height(self):