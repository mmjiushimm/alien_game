import pygame

import settings, ship

class AlienInvasion():
    def __init__(self):
        pygame.init()
        #创建设置实例对象
        self.settings = settings.Settings()
        #设置显示窗口的大小，并且通过set_mode()返回值获得窗口图像的实列对象
        self.surface = pygame.display.set_mode((self.settings.width, self.settings.height))
        #设置窗口名称
        pygame.display.set_caption(self.settings.game_name)
        #设置主循环标记
        self.run_flag = True
        #设置背景颜色
        #self.bg_color = pygame.Color(160, 160, 160)
        #初始化飞船
        self.ship = ship.Ship(self)
        
    def run(self):
        '''程序运行的主循环'''
        while self.run_flag:
            #处理事件
            self._check_events()
            #显示
            self._update_screen()

    def _check_events(self):
        '''处理鼠标键盘事件'''
        for event in pygame.event.get():
            #窗口退出事件发生时，主循环结束
            if event.type == pygame.QUIT:
                self.run_flag = False
            #event对象会根据type的值（即根据不同的event类型）有不同的属性
            #比如type是pygame.KEYDOWN，则event会有key这个属性。
            #key属性可以对应具体的某个按键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 10

    def _update_screen(self):
        '''更新屏幕显示'''
        #通过窗口图像实列对象的fill()方法对背景填充颜色
        self.surface.fill(self.settings.bg_color)
        #显示飞船
        self.ship.draw_ship()
        #self.surface.blit(self.ship.image, self.ship.rect)
        #显示窗口
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
    pygame.quit()
