'''def Ship class'''

import os
import pygame

class Ship:
    def __init__(self, ai):
        #把窗口图像的实例对象传给飞船图像的实例对象
        self.surface = ai.surface
        #把主程序实例对象的settings属性传给ship实例对象
        self.settings = ai.settings
        
        
        #加载ship图片，返回图片的实例对象
        self.image = pygame.image.load(os.path.join("images", "rocket.png"))
        #获取图片实例对象的rect属性
        self.rect = self.image.get_rect()

        #把窗口的rect属性（rect也是Rect的实例对象）的midbottom属性值赋值给
        #飞船的rect属性的midbottom属性值
        self.rect.midbottom = ai.surface.get_rect().midbottom
        
        #初始化移动flag
        self.move_right = False
        self.move_left = False

    def draw_ship(self):
        '''显示飞船'''
        #self._update_ship()
        self.surface.blit(self.image, self.rect)

    def update_ship(self):
        '''更新位置'''
        if self.move_right and self.rect.right < self.surface.get_rect().right:
        #if self.move_right:
            self.rect.x += self.settings.ship_speed
            print(self.rect.x)
        if self.move_left and self.rect.left > self.surface.get_rect().left:
            self.rect.x -= self.settings.ship_speed
    
    def is_right_boundary(self):
        '''判断ship是否触碰窗口边界'''
        if self.rect.right >= self.surface.get_rect().right:
            return True
        else:
            return False