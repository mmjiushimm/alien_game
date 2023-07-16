import os
import pygame

class Ship:
    def __init__(self, ai):
        #把窗口图像的实例对象传给飞船图像的实例对象
        self.surface = ai.surface
        
        #加载ship图片，返回图片的实例对象
        self.image = pygame.image.load(os.path.join("images", "rocket.png"))
        #获取图片实例对象的rect属性
        self.rect = self.image.get_rect()

        #把窗口的rect属性（rect也是Rect的实例对象）的midbottom属性值赋值给
        #飞船的rect属性的midbottom属性值
        self.rect.midbottom = ai.surface.get_rect().midbottom

    def draw_ship(self):
        '''显示飞船'''
        self.surface.blit(self.image, self.rect)