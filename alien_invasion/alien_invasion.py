import pygame
from setting import Settings #里面是类，所以直接将类导入
from ship import Ship #里面是类，所以直接将类导入
import game_functions as gf #里面是函数，为了防止导入太过复杂，将其全部导入,目的是为了简化
from pygame.sprite import Group
from game_stats import Gamestats
from button import Button
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invation")

    #创建一艘飞船的实例
    ship = Ship(setting, screen)

    #创建一个用于存储子弹的编组的实例
    bullets = Group()

    #创建一个外星人的编组的实例
    aliens = Group()

    #创建外形人群
    gf.creat_fleet(setting, screen, aliens, ship)

    #创建统计信息的实例
    game_stats = Gamestats(setting)

    #创建一个按钮
    play_button = Button(screen, "play", setting)

    #开始游戏 的主循环
    while True:
        #监视键盘和鼠标事件，不管是否游戏进行
        gf.check_events(game_stats, play_button, aliens, bullets, ship, setting, screen)
        #               game_stats, play_button, aliens, bullets, ship, setting, screen   如果是这样就对了
        #               setting, screen, ship, bullets, game_stats, play_button, aliens   如果是这样就会报错，如下：
        #               if play_button.button_rect.collidepoint(mouse_x, mouse_y):
        # AttributeError: 'pygame.Surface' object has no attribute 'button_rect'
        #因此在python中位置参数要一一对应

        #以下代码表示游戏进行中，相关位置的更新
        if game_stats.game_active:

            #更新飞船位置
            ship.update()

            #更新子弹位置，删除已经消失的子弹
            gf.update_bullets(setting, screen, ship, aliens, bullets)

            #更新外星人的位置
            gf.update_aliens(setting, game_stats, aliens, ship, screen, bullets)

        #更新屏幕上的图画并切换到新屏幕，重新绘制屏幕，飞船，子弹和外星人，不管是否游戏进行
        gf.update_screen(setting, screen, ship, bullets, aliens, play_button, game_stats)

run_game()



