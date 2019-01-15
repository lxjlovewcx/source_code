class Settings():
    '''存储《外星人入侵》的所有设置'''

    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船移动速度设置
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 3   #子弹的速度
        self.bullet_width = 3         #子弹的宽度
        self.bullet_height = 15       #子弹的高度
        self.bullet_color = 60, 60 ,60   #设置子弹的颜色

        #限制子弹数量
        self.bullets_allowed = 3

        #外星人的设置
        self.alien_x_speed = 1    #外星人x移动速度
        self.alien_y_speed = 10   #外星人y移动速度
        #设置外星人x方向上的移动方向1或者-1
        self.alien_direction = 1   #用于调整方向

        #飞船的数量
        self.ship_limit = 3

        #游戏等级提升速度设置
        self.aliens_speedup_level = 3

        #随着游戏重新开始，游戏被初始化
        self.game_setting_initizlization()

    def game_setting_initizlization(self):
        self.alien_x_speed = 1
        self.alien_y_speed = 10

    def game_speedup_level(self):
        self.alien_x_speed *= self.aliens_speedup_level
        self.alien_y_speed *= self.aliens_speedup_level


