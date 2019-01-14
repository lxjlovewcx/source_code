import pygame
class Ship():

    def __init__(self, settings, screen):
        """其中setting说明了飞船的设置参数
        screen说明了需要将飞船绘制到什么地方
        """


        """初始化飞船的初始位置"""
        self.screen = screen

        # 使得setting实例能够被update方法使用
        self.setting = settings

        #加载飞船图形并获取其外形矩形
        self.image = pygame.image.load('images/ship.bmp')  #用于加载图像，返回一个飞船的surface，并将其存放到self.image中。
        self.rect = self.image.get_rect() #使用get_rect方法获取surface的属性rect。python处理的是矩形而非surface的真实形状，
                                            # 但是处理矩形更加高效
        self.screen_rect = screen.get_rect() #获取屏幕的surface属性

        #将每艘飞船初始位置设定为屏幕下部正中央
        self.rect.centerx = self.screen_rect.centerx #获取rect属性后，就可以设置相应属性：center
        #centerx、centery.
        self.rect.bottom = self.screen_rect.bottom

        #在self.center中存储小数值
        self.center = float(self.rect.centerx)

        #飞船的持续移动
        self.moving_right = False
        self.moving_left = False

    """每次"""
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

        """在飞船每次被击毁或者外形人到达屏幕低端后，需要重新将飞船居中"""
    def ship_center(self):
        #飞船的x坐标设置为将屏幕中心的x坐标，使其移到屏幕低端中心位置
        self.center = self.screen_rect.centerx


