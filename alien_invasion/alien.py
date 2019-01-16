import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    表示单个外星人的类
    除了位置不同外，这个类的大部分代码都和ship类相似。每一个外星人最初都位于屏幕左上角附近。
    """
    def __init__(self, setting, screen):
        #继承sprite中的属性值
        super().__init__()

        #初始化外形人的位置
        self.screen = screen
        self.setting = setting

        #载入外星人的图片并获取其矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #将外星人首先出现位置定义在左上角。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.alien_x_speed = self.setting.alien_x_speed
        #存储外星人真实的坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


 #       self.screen_rect = screen.get_rect()
    def blitme(self):
        """在制定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        #外星人群向右移动
        self.x += self.alien_x_speed * self.setting.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.setting.screen_width:
            return True
        elif self.rect.x <= 0:
            return True







