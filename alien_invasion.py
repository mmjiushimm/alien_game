import pygame

import settings, ship, bullet

class AlienInvasion():
    def __init__(self):
        pygame.init()
        #创建设置实例对象
        self.settings = settings.Settings()
        #设置显示窗口的大小，并且通过set_mode()返回值获得窗口图像的实列对象
        self.surface = pygame.display.set_mode((self.settings.width, self.settings.height))
        #self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #设置窗口名称
        pygame.display.set_caption(self.settings.game_name)
        #设置主循环标记
        self.run_flag = True
        #设置背景颜色
        #self.bg_color = pygame.Color(160, 160, 160)
        #初始化飞船
        self.ship = ship.Ship(self)
        #创建bullet sprite group对象，统一管理bullet对象
        self.bullets = pygame.sprite.Group()
        
    def run(self):
        '''程序运行的主循环'''
        while self.run_flag:
            #处理事件
            self._check_events()
            #把画面中元素的位置更新放在主循环里，而不放在元素的draw()方法里，
            #是因为考虑到元素的位置变化与显示没有必然联系，
            #比如元素的位置可以变化，但是不一定非要显示出来。
            #update ship location
            self.ship.update_ship()
            #update bullet location
            #bullets（sprite group对象）调用update()方法，
            #相当于这个集合中的每个成员都调用各自的update()方法
            self.bullets.update()
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
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self, event):
        #如果事件触发后，这个事件没有中断，则不会重新判断事件触发的条件。
        #即，右键按下后，如果ship满足右移条件，则会开始右移。
        #在右移过程中，只要右键不松开，则会持续右移，
        #即使触碰窗口右边界，也不会判断右移条件，
        #只有右键松开后，再次按下，才会检查判断条件。
        #所以，要限制移动范围，需要在计算位移的地方，而非响应按键事件的地方
        #if event.key == pygame.K_RIGHT and not self.ship.is_right_boundary():
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_q:
            self.run_flag = False
        if event.key == pygame.K_SPACE:
            self._shoot_bullet()
    
    def _keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_screen(self):
        '''更新屏幕显示'''
        #通过窗口图像实列对象的fill()方法对背景填充颜色
        self.surface.fill(self.settings.bg_color)
        #显示飞船
        self.ship.draw_ship()
        #self.surface.blit(self.ship.image, self.ship.rect)
        #show bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #显示窗口
        pygame.display.flip()

    #后面考虑把这个方法移到Ship类里，作为ship对象的行为
    def _shoot_bullet(self):
        self.bullets.add(bullet.Bullet(self))


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
    pygame.quit()
