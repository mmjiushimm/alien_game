import os
from typing import Any
import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, ai):
        super().__init__()
        self.surface = ai.surface
        self.image = pygame.image.load(os.path.join("images", "alien.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ai.surface.get_rect().topleft
        self.settings = ai.settings
        #由于rect.x，rect.y是整数，为了更精细调整速度，坐标需要用浮点型表示
        self.x = (float)(self.rect.x)
        self.y = (float)(self.rect.y)
    
    def draw_alien(self):
        #在显示alien之前，需要把更新的坐标转换成整型
        self.rect.x = (int)(self.x)
        self.rect.y = (int)(self.y)
        self.surface.blit(self.image, self.rect)
    
    def update(self, *args: Any, **kwargs: Any):
        self.y += self.settings.alien_speed

    def set_aliens_origin(self, x=0, y=0):
        self.x = x
        self.y = y
