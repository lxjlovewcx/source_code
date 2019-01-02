import sys
import pygame
from bullet import Bullet
from alien import Alien

def creat_fleet(setting,screen,aliens,ship):
    alien = Alien(setting, screen)
    number_alien_x = get_alien_number_x(setting, alien)
    number_alien_y = get_alien_number_y(setting, alien,ship)
    for alien_number_x in range(number_alien_x):
        for alien_number_y in range(number_alien_y):
            create_alien(alien_number_x,alien_number_y, setting, screen, aliens)

def get_alien_number_x(setting,alien):
    alien_width = alien.rect.width
    avalilable_x = setting.screen_width - 2*alien_width
    number_alien_x = int(avalilable_x/(2*alien_width))
    print(number_alien_x)
    return number_alien_x

def get_alien_number_y(setting,alien,ship):
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    avalilable_y = setting.screen_height - 2*alien_height - ship_height
    number_alien_y = int(avalilable_y/(2*alien_height))
    print(number_alien_y)
    return number_alien_y

def create_alien(alien_number_x,alien_number_y,setting,screen,aliens):
    alien = Alien(setting, screen)
    alien.x = alien.rect.width + 2*alien_number_x*alien.rect.width
    alien.rect.x = alien.x
    alien.y = alien.rect.width + 2 * alien_number_y * alien.rect.width
    alien.rect.y = alien.y
    aliens.add(alien)

def fire_bullet(bullets,setting,screen,ship):
    """如何还没有到发射限制，就发射一颗子弹"""
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    # 子弹位置更新,并且删除消失的子弹
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_keydown_event(event,setting,ship,screen,bullets):
    #玩家一直按右键，飞船的反应
    if event.key == pygame.K_RIGHT:
        # 向右移动飞行
        ship.moving_right = True

        #玩家一直按左键，飞船的反应
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

        #玩家在按空格键时，系统的反应
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, setting, screen, ship)

        #玩家按下q键时，游戏结束
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞行
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向右移动飞行
        ship.moving_left = False

def check_events(setting,screen,ship,bullets):
    """响应按键和鼠标按键"""
    for event in pygame.event.get():
        '''
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞行
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #向右移动飞行
                ship.moving_right = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #向右移动飞行
                ship.moving_left = 发个True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #向右移动飞行
                ship.moving_left = False
        '''
        #以上部分为自己在此处烦了错，分支结构没有搞清楚，只是执行其中一条
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setting,ship,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(setting,screen,ship,bullets,aliens):
    """更新屏幕上的图画并切换到新屏幕"""

    # 每次循环时都会重绘画面
    screen.fill(setting.bg_color)

    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    # 绘制外星人群
    for alien in aliens:
        alien.blitme()


    # 让最近绘制的屏幕可见
    pygame.display.flip()
