# import random
import pygame
from spielsteine import Spielsteine
# Importiere EASTER-EGGS

inactive_blocks = [] # Blöcke, die sich am Boden befinden
active_blocks = [] # aktiver Block


class Board:
    def __init__(self):
        self.block_size = 20
        self.board_width = self.block_size * 16
        self.board_height = self.block_size * 20
        self.blocks_per_row = self.board_width / 20
        self.active_block = True
        self.block_speed = 5
        self.block_x = self.block_size * 16 / 20
        self.block_y = 50


    def draw_playgound(self, win):
        win.fill((0, 0, 0))
        pygame.display.set_mode((self.board_width, self.board_height))
        pygame.display.set_caption("Tetris")
    def play(self):
        # ALTE SPIELSTEINE (inactive) werden gezeichnet
        '''''for inactive_block in inactive_blocks:
            inactive_block = Spielsteine
            inactive_block.draw(self)
        '''''
        # NEUER SPIELSTEIN wird erstellt
        block = Spielsteine # Die Variable Block wird mit der Klasse Spielsteine gleichgesetzt
        block.draw() # Der Block wird gezeichnet
        active_blocks.append(block) # Der Block wird in die Liste der aktiven Blöcke geparkt.
        gedrueckt = pygame.key.get_pressed()

        if gedrueckt[pygame.K_DOWN]:
            self.block_speed += 100
        elif gedrueckt[pygame.K_LEFT]:
            if self.block_x >= 10:
                self.block_x -= 10
            else:
                print("Sie haben das Ende des Spielfeldes erreicht!")
        elif gedrueckt[pygame.K_RIGHT]:
            if self.block_x <= self.board_width - 30:
                self.block_x += 10
            else:
                print("Sie haben das Ende des Spielfeldes erreicht!")

        # Spielsteine.drop()


    # def get_width(self):
    # def get_height(self):
