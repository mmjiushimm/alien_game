import pygame

class Settings:
    def __init__(self):
        #显示窗口宽度
        self.width = 1500
        #显示窗口高度
        self.height = 900
        #显示窗口标题
        self.game_name = 'alien'
        #显示窗口背景色
        self.bg_color = pygame.Color(160, 160, 160)
        #ship速度
        self.ship_speed = 1