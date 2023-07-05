import pygame

class AlienInvasion():
    def __init__(self):
        pygame.init()
        #设置显示窗口的大小，并且通过set_mode()返回值获得窗口图像的实列对象
        self.surface = pygame.display.set_mode((500, 300))
        #设置窗口名称
        pygame.display.set_caption('alien')
        #设置主循环标记
        self.run_flag = True
        #设置背景颜色
        self.bg_color = pygame.Color(160, 160, 160)

    def run(self):
        '''程序运行的主方法'''
        while self.run_flag:
            #处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_flag = False
            #显示窗口
            pygame.display.flip()
            #通过窗口图像实列对象的fill()方法对背景填充颜色
            self.surface.fill(self.bg_color)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
