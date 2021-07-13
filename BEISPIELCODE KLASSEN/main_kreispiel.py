import pygame
import random
from kreis import Kreis

pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("Zufällige Kreise")

kreise = []
counter = 0

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    if counter == 0:
        k = Kreis()
        k.set_random_values(500, 500)
        kreise.append(k)

    counter = (counter + 1) % 10

    win = pygame.display.get_surface()
    win.fill((0, 0, 0))

    for k in kreise:
        k.move()
        k.draw(win)

    pygame.display.update()

pygame.quit()
