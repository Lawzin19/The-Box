import pygame

from const import SHIP_COLOR, WIDTH, HEIGHT

class Ship:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y 
        self.speed = speed
        
    def move(self, keys):
        if keys[pygame.K_UP]:  # Se pressionar UP
            self.y -= self.speed  # A nave sobe
        if keys[pygame.K_DOWN]:  # Se pressionar DOWN
            self.y += self.speed  # A nave desce
        if keys[pygame.K_LEFT]:  # Se pressionar LEFT
            self.x -= self.speed  # A nave vai à esquerda
        if keys[pygame.K_RIGHT]:  # Se pressionar RIGHT
            self.x += self.speed  # A nave vai à direita
            
        # Borda da tela
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT
            
    def draw(self, screen):
        # Formatando a nave (triângulo)
        p1 = (self.x, self.y)  # Ponto superior da nave
        p2 = (self.x - 15, self.y + 30)  # Ponto inferior esquerdo
        p3 = (self.x + 15, self.y + 30)  # Ponto inferior direito
        pygame.draw.polygon(screen, SHIP_COLOR, [p1, p2, p3])  # Gera o triângulo