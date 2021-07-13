import random
import pygame


class Kreis:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 10
        self.color = (255, 255, 255)
        self.left = 0
        self.right = 0
        self.speed = 0

        self.move_right = True

    def set_random_values(self, max_x, max_y):
        self.radius = random.randint(10, 50)
        self.speed = random.randint(1, 20)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(0, max_x)
        self.left = self.x
        self.y = random.randint(0, max_y)
        self.right = self.x + random.randint(0, max_x - self.x)

    def move(self):
        if self.move_right:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.x >= self.right:
            self.move_right = False
        elif self.x <= self.left:
            self.move_right = True

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
