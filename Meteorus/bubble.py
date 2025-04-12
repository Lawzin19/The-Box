import pygame
from const import BUBBLE_COLOR, INNER_BUBBLE_COLOR

class Bubble:
    def __init__(self, x, y, radius=15, inner_radius=13):
        self.x = x
        self.y = y
        self.radius = radius
        self.inner_radius = inner_radius
        self.active = True
        self.hits = 0
        self.flash_duration = 7
        self.flash_timer = 0
        
        self.is_eliminate = False
        self.blink_timer = 0
        self.blink_interval = 5
        self.blink_cont = 0
        self.visible = True
        
    def update(self):
        if self.is_eliminate:
            self.blink_timer -= 1
            if self.blink_timer <= 0:
                self.visible = not self.visible
                self.blink_timer = self.blink_interval
                if not self.visible:
                    self.blink_cont += 1
                    if self.blink_cont >= 3:
                        self.active = False
        else:               
            if self.flash_timer > 0:
                self.flash_timer -= 1
        
    def draw(self, screen):
        if self.active:
            if self.is_eliminate:
                if self.visible:
                    pygame.draw.circle(screen, BUBBLE_COLOR, (self.x, self.y), self.radius)
                    pygame.draw.circle(screen, INNER_BUBBLE_COLOR, (self.x, self.y), self.inner_radius)
            
            else:       
                if self.flash_timer > 0:
                    outer_color = (128, 128, 128)
                    """inner_color = (128, 128, 128)"""
                else:
                    outer_color = BUBBLE_COLOR
                    """inner_color = INNER_BUBBLE_COLOR"""
                    
                pygame.draw.circle(screen, outer_color, (self.x, self.y), self.radius)
                pygame.draw.circle(screen, INNER_BUBBLE_COLOR, (self.x, self.y), self.inner_radius)
            
    def check_collision(self, projetil):
        proj_x, proj_y = projetil.x, projetil.y
        dx = self.x - proj_x
        dy = self.y - proj_y
        distance = (dx**2 + dy**2)**0.5
        return distance < self.radius
    
    def register_hit(self):
        self.hits += 1
        if self.hits < 3:
            self.flash_timer = self.flash_duration
        else:
            self.is_eliminate = True
            self.blink_timer = self.blink_interval
            self.visible = True