import pygame
import random
# from blöcke import Blöcke

# ---------------Türkis--------Gelb-----------Lila-----------Grün---------Rot----------Blau---------Orange
block_colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]

win = pygame.display.get_surface()


class Spielsteine:
    def __init__(self):
        self.block_x = 0 # Position Block auf der x-Achse
        self.block_y = 0 # Position Block auf der y-Achse
        self.block_size = 20 # Seitengröße des Blockes
        #self.block_color = (0, 0, 0) # Die Farbe, in der der Block gezeichnet wird (Parameter)
        self.block_colors_position = 1 # Die Farbe des Blockes. Der Wert wird aus der Liste geholt
        self.block_speed = 5 # Fallgeschwindigkeit des Blockes
        self.board_width = self.block_size * 16 # Fensterbreite
        self.board_height = self.block_size * 20 # Fensterhöhe
        self.block_active = True # True, falls der Block noch nicht unten bei board_height angekommen ist, sonst False

    def draw_new_block(self): # Der neue Block wird im Fenster gezeichnet
        self.block_x = self.block_size * 16 / 2 - (self.block_size/2)
        self.block_colors_position = random.randint(0, 6)
        pygame.draw.rect(win, block_colors[self.block_colors_position], )

    #def is_active(self): # Liefert den Wert des Attributs active zurück.
        ###
    #def drop(self): # Wenn der Block noch aktiv ist, "fällt" er um speed pixel nach unten
        ###





"""""
        block_speed += 5
        if block_speed >= self.board_height - 70:
            block_speed = 0
            block_x = self.block_size * 16 / 2
            random_color = random.randint(0, 6)

"""""
