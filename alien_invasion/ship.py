import pygame
class Ship():

    def __init__(self,settings,screen):

        """初始化飞船的初始位置"""
        self.screen = screen

        # 使得setting实例能够被update方法使用
        self.setting = settings

        #加载飞船图形并获取其外形矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船初始位置设定为屏幕下部正中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在self.center中存储小数值
        self.center = float(self.rect.centerx)

        #飞船的持续移动
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.center <= self.screen_rect.right:
            self.center += self.setting.ship_speed_factor
        if self.moving_left and self.center >= self.screen_rect.left:
            self.center -= self.setting.ship_speed_factor

         #根据self.center 更新self.rect.centerx 对象
        self.rect.centerx = self.center


