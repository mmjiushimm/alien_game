import pygame

import settings, ship, bullet, alien

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
        self._run_flag = True
        #设置背景颜色
        #self.bg_color = pygame.Color(160, 160, 160)
        #初始化飞船
        self._ship = ship.Ship(self)
        #创建bullet sprite group对象，统一管理bullet对象
        self._bullets = pygame.sprite.Group()
        #init alien
        self._aliens = pygame.sprite.Group()
        #alien左边界
        self._alien_left_boundary = 0
        #alien右边界
        self._alien_right_boundary = 0
        #alien移动标记
        self._alien_move_flag = True
        
    def run(self):
        '''程序运行的主循环'''
        while self._run_flag:
            #处理事件
            self._check_events()

            #把画面中元素的位置更新和图像显示分开，
            #是因为考虑到元素的位置变化与显示没有必然联系，
            #比如元素的位置可以变化，但是不一定非要显示出来。
            #update ship location
            self._ship.update_ship()

            #更新子弹
            self._update_bullet()

            #更新alien
            self._update_alien()

            #更新显示
            self._update_screen()

    def _check_events(self):
        '''处理鼠标键盘事件'''
        for event in pygame.event.get():
            #窗口退出事件发生时，主循环结束
            if event.type == pygame.QUIT:
                self._run_flag = False
            #event对象会根据type的值（即根据不同的event类型）有不同的属性
            #比如type是pygame.KEYDOWN，则event会有key这个属性。
            #key属性可以对应具体的某个按键
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self, event):
        '''键盘按下事件'''
        #如果事件触发后，这个事件没有中断，则不会重新判断事件触发的条件。
        #即，右键按下后，如果ship满足右移条件，则会开始右移。
        #在右移过程中，只要右键不松开，则会持续右移，
        #即使触碰窗口右边界，也不会判断右移条件，
        #只有右键松开后，再次按下，才会检查判断条件。
        #所以，要限制移动范围，需要在计算位移的地方，而非响应按键事件的地方
        #if event.key == pygame.K_RIGHT and not self.ship.is_right_boundary():
        if event.key == pygame.K_RIGHT:
            self._ship.move_right = True
        if event.key == pygame.K_LEFT:
            self._ship.move_left = True
        if event.key == pygame.K_q:
            self._run_flag = False
        if event.key == pygame.K_SPACE:
            self._shoot_bullet()
    
    def _keyup_event(self, event):
        '''键盘松开事件'''
        if event.key == pygame.K_RIGHT:
            self._ship.move_right = False
        if event.key == pygame.K_LEFT:
            self._ship.move_left = False

    def _update_screen(self):
        '''更新屏幕显示'''
        #通过窗口图像实列对象的fill()方法对背景填充颜色
        self.surface.fill(self.settings.bg_color)
        
        #显示飞船
        self._ship.draw_ship()
        #self.surface.blit(self.ship.image, self.ship.rect)
        
        #show bullet
        for bullet in self._bullets.sprites():
            bullet.draw_bullet()
        
        #show alien
        for alien in self._aliens.sprites():
            alien.draw_alien()

        #显示窗口
        pygame.display.flip()

    #后面考虑把这个方法移到Ship类里，作为ship对象的行为
    def _shoot_bullet(self):
        '''发射子弹'''
        if len(self._bullets) < self.settings.bullet_limit:
            self._bullets.add(bullet.Bullet(self))
    
    def _remove_bullet(self):
        '''删除超出范围的bullet'''
        for bullet in self._bullets.sprites():
            if bullet.rect.bottom < 0:
                self._bullets.remove(bullet)
                print(len(self._bullets.sprites()))
    
    def _update_bullet(self):
        '''更新子弹位置和有效的数量'''
        #update bullet location
        #bullets（sprite group对象）调用update()方法，
        #相当于这个集合中的每个成员都调用各自的update()方法
        self._bullets.update()
        if len(self._bullets.sprites()):
            self._remove_bullet()
    
    def _update_alien(self):
        '''更新alien的位置和有效数量'''
        #self.alien.update()
        if not len(self._aliens):
            self._creat_aliens()
        else:
            #self._aliens.update()
            self._move_aliens()
            self._remove_aliens()
    
    def _creat_aliens(self):
        '''创建alien群'''
        new_alien = alien.Alien(self)
        #计算屏幕宽度可以放alien的数量，还要考虑两个alien之间的margin
        #下一行末尾的反斜线\用于代码行换行
        n = (self.surface.get_rect().width - 2 * self.settings.screen_x_margin) // \
        (new_alien.rect.width + self.settings.alien_x_margin)
        for i in range(n):
            new_alien = alien.Alien(self)
            new_alien.set_aliens_origin(self.settings.screen_x_margin + i * (new_alien.rect.width + self.settings.alien_x_margin))
            self._aliens.add(new_alien)
        self._alien_left_boundary = self.settings.screen_x_margin
        self._alien_right_boundary = self.settings.screen_x_margin + n * (new_alien.rect.width + self.settings.alien_x_margin) - self.settings.alien_x_margin
        """ aliens_list = list(self._aliens.sprites())
        self._alien_left_boundary = aliens_list[0].rect.left
        self._alien_right_boundary = aliens_list[-1].rect.right """
    
    def _move_aliens(self):
        screen_right = self.surface.get_rect().right
        screen_left = self.surface.get_rect().left
        if(self._alien_move_flag):
            if(screen_right - self._alien_right_boundary > self.settings.alien_x_margin):
                self._aliens_fly(0)
            else:
                self._aliens_fly(2)
                self._alien_move_flag = False
        else:
            if(self._alien_left_boundary - screen_left > self.settings.alien_x_margin):
                self._aliens_fly(1)
            else:
                self._aliens_fly(2)
                self._alien_move_flag = True
    
    def _aliens_fly(self, i):
        #右移
        if i == 0:
            for alien in self._aliens:
                alien.x += self.settings.alien_speed
            self._alien_right_boundary += self.settings.alien_speed
            self._alien_left_boundary += self.settings.alien_speed

        #左移
        if i == 1:
            for alien in self._aliens:
                alien.x -= self.settings.alien_speed
            self._alien_right_boundary -= self.settings.alien_speed
            self._alien_left_boundary -= self.settings.alien_speed

        #下移
        if i == 2:
            for alien in self._aliens:
                alien.y += 50 * self.settings.alien_speed



    def _remove_aliens(self):
        '''删除无效的aliens'''
        for alien in self._aliens.sprites():
            if alien.rect.top > self.surface.get_rect().bottom:
                self._aliens.remove(alien)
                print(len(self._aliens.sprites()))



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
    pygame.quit()
