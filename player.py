import math
import pygame
from settings import *

class Player:
    def __init__(self):
        self.x, self.y = WIDTH // 4, HEIGHT // 4
        self.angle = 0
        self.speed = 10

    def pos(self):
        return (self.x, self.y)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x = self.x - self.speed * math.cos(self.angle)
            self.y = self.y - self.speed * math.sin(self.angle)
        if keys[pygame.K_a]:
            self.x = self.x + self.speed * math.sin(self.angle)
            self.y = self.y - self.speed * math.cos(self.angle)
        if keys[pygame.K_d]:
            self.x = self.x - self.speed * math.sin(self.angle)
            self.y = self.y + self.speed * math.cos(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= SENSETIVITY / FPS
        if keys[pygame.K_RIGHT]:
            self.angle += SENSETIVITY / FPS
