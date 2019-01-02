import pygame
from setting import Settings #里面是类，所以直接将类导入
from ship import Ship #里面是类，所以直接将类导入
import game_functions as gf #里面是函数，为了防止导入太过复杂，将其全部导入,目的是为了简化
from pygame.sprite import Group
from alien import Alien
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invation")

    #创建一艘飞船
    ship = Ship(setting,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人的编组
    aliens = Group()

    #创建外形人群
    gf.creat_fleet(setting,screen,aliens,ship)

    #开始游戏 的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(setting,screen,ship,bullets)

        #飞船位置更新
        ship.update()

        #子弹位置更新，删除已经消失的子弹
        gf.update_bullets(bullets)

        #更新屏幕上的图画并切换到新屏幕
        gf.update_screen(setting,screen,ship,bullets,aliens)

run_game()



