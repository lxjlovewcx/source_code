import pygame
import sys
from pygame.sprite import Sprite
class Alien(Sprite):
    """

    """
    def __init__(self,setting,screen):
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
        #存储外星人真实的坐标
        self.x = float(self.rect.x)


 #       self.screen_rect = screen.get_rect()
    def blitme(self):
        """在制定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)



