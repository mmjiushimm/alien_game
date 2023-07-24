'''def Bullet class'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.settings = ai.settings
        self.surface = ai.surface
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai.ship.rect.midtop

    def draw_bullet(self):
        pygame.draw.rect(self.surface, self.settings.bullet_color, self.rect)
    
    #重写Sprite父类的update()方法
    #通过调用sprite.group对象的update()，系统会自动调用加入group的每个sprite对象的update()方法
    def update(self):
        self.rect.y -= self.settings.bullet_speed