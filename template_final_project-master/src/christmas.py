import pygame
import random

class GameObject:
    def __init__(self, image_file, x, y):
        self.image_file = image_file
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

class Santa(GameObject):
    def __init__(self, image_file, x, y, speed):
        super().__init__(image_file, x, y)
        self.speed = speed

    def move(self, direction):
        if direction == "UP" and self.y - self.speed >= 0:
            self.update_position(self.x, self.y - self.speed)
        if direction == "DOWN" and self.y + self.speed + self.rect.height <= 600:
            self.update_position(self.x, self.y + self.speed)
        if direction == "LEFT" and self.x - self.speed >= 0:
            self.update_position(self.x - self.speed, self.y)
        if direction == "RIGHT" and self.x + self.speed + self.rect.width <= 800:
            self.update_position(self.x + self.speed, self.y)

class Grinch(GameObject):
    def __init__(self, image_file, x, y, dx, dy):
        super().__init__(image_file, x, y)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Smaller Grinch
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx = dx
        self.dy = dy

class Present(GameObject):
    def __init__(self, image_file, x, y):
        super().__init__(image_file, x, y)
        self.image = pygame.transform.scale(self.image, (30, 30))  # Smaller present
        self.rect = self.image.get_rect(topleft=(x, y))
