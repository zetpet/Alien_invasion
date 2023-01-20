import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"A class for controlling bullets fired by a ship"""
    def __init__(self, ai_settings, screen, ship):
        """"Creates a bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        #Creating a bullet at position (0,0) and assigning the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Bullet position is stored in real format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen"""
        #Update bullet position in real format
        self.y -= self.speed_factor
        #Rectangle Position Update
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Bullet output on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)