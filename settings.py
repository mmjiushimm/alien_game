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
        #bullet width
        self.bullet_width = 10
        #bullet height
        self.bullet_height = 15
        #bullet speed
        self.bullet_speed = 1
        #bullet color
        self.bullet_color = pygame.Color(0, 0, 0)
        #max bullet quantity
        self.bullet_limit = 3
        #alien speed
        self.alien_speed = 0.5
        #alien x margin
        self.alien_x_margin = 10
        #alien y margin
        self.alien_y_margin = 10
        #screen x margin
        self.screen_x_margin = 100
