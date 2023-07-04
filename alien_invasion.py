import pygame

class AlienInvasion():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((500, 300))
        pygame.display.set_caption('alien')
        self.flag = True

    def run(self):
        while self.flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()
    """ print('a')
    str(123)
    input() """