import pygame

from const import PROJETIL_COLOR

class Projetil:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.speed = 20
        
    def move(self):
        self.y -= self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, PROJETIL_COLOR, (self.x - 2, self.y, 4, 10))