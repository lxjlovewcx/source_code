import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_aliens_bottom(screen, aliens, game_stats, bullets, setting, ship):
    #在此处，因为未设置screen类，因此需要重新获取get_rect(),获取rect后才能使用surface的属性值。
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: #此处犯过错，应该是>= 而不是==，同时属性单词
                                                    # 写错应该是bottom，不是buttom
            ship_hit(game_stats, aliens, bullets, setting, screen, ship)
            break                                   #此处没有考虑break

def creat_fleet(setting, screen, aliens, ship):
    alien = Alien(setting, screen)
    number_alien_x = get_alien_number_x(setting, alien)
    number_alien_y = get_alien_number_y(setting, alien, ship)
    for alien_number_x in range(number_alien_x):
        for alien_number_y in range(number_alien_y):
            create_alien(alien_number_x, alien_number_y, setting, screen, aliens)

def get_alien_number_x(setting, alien):
    alien_width = alien.rect.width
    avalilable_x = setting.screen_width - 2*alien_width
    number_alien_x = int(avalilable_x/(2*alien_width))
    print(number_alien_x)
    return number_alien_x

def get_alien_number_y(setting, alien, ship):
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    avalilable_y = setting.screen_height - 2*alien_height - ship_height
    number_alien_y = int(avalilable_y/(2*alien_height))
    print(number_alien_y)
    return number_alien_y

def create_alien(alien_number_x, alien_number_y, setting, screen, aliens):
    alien = Alien(setting, screen)
    alien.x = alien.rect.width + 2*alien_number_x*alien.rect.width
    alien.rect.x = alien.x
    alien.y = alien.rect.width + 2 * alien_number_y * alien.rect.width
    alien.rect.y = alien.y
    aliens.add(alien)

def fire_bullet(bullets, setting, screen, ship):
    """如何还没有到发射限制，就发射一颗子弹"""
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def check_bullet_alien_collision(setting, screen, aliens, ship, bullets):
    """响应外星人和子弹的碰撞，并且在aliens和bullets组中剔除"""
    """将删除的字典元素存储到collisions字典中"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        """删除现有的子弹并创建一批外星人"""
        bullets.empty()
        #当外星人全部被消灭，即将创建新的外形人的时候，修改设置，使其升级。
        setting.game_speedup_level()
        creat_fleet(setting, screen, aliens, ship)

def update_bullets(setting, screen, ship, aliens, bullets):
    # 子弹位置更新,并且删除消失的子弹
    bullets.update()
    check_bullet_alien_collision(setting, screen, aliens, ship, bullets)
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def ship_hit(game_stats, aliens, bullets, setting, screen, ship):
    # 其检查aliens编组当中是否有成员与ship发生碰撞，如果找到了与精灵发生碰撞的成员后就停止遍历。
    # 并且返回第一个与飞船发生碰撞的外星人。如果没有发生碰撞，就返回none，那么if语句不会执行。
    # 如果找到变执行下面的语句。
    if game_stats.ship_left > 0:
        print("ship hit")
        # 飞船数量减一
        game_stats.ship_left -= 1

        """
        这是我最开始的写法，但是这种减了后就进行判断的化，会造成逻辑错误。
        if game_stats.ship_left <= 0:
            game_stats.game_active = False
        """
        # 清空子弹和外星人列表
        aliens.empty()
        bullets.empty()

        # 创建一批新的外星人，并将飞船位置居中
        creat_fleet(setting, screen, aliens, ship)
        ship.ship_center()

        # 暂停1s
        sleep(1)
    else:
        #表明游戏结束
        game_stats.game_active = False
        #游戏鼠标可以见了
        pygame.mouse.set_visible(True)

def check_alien_ship_collision(aliens, ship, game_stats, setting, screen, bullets):
    """响应外星人和飞船的碰撞，并且显示hit"""
    """将删除的字典元素存储到collisions字典中"""
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_stats, aliens, bullets, setting, screen, ship)

def update_aliens(setting, game_stats, aliens, ship, screen, bullets):
    # 外星人位置更新
    check_fleet_edge(aliens, setting)
    aliens.update()
    check_alien_ship_collision(aliens, ship, game_stats, setting, screen, bullets)
    check_aliens_bottom(screen, aliens, game_stats, bullets, setting, ship)


def check_fleet_edge(aliens, setting):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, setting)
            break

def change_fleet_direction(aliens, setting):
    for alien in aliens.sprites():
        alien.rect.y += setting.alien_y_speed
    setting.alien_direction *= -1

def check_keydown_event(event, setting, ship, screen, bullets):
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

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞行
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向右移动飞行
        ship.moving_left = False

def check_play_button(game_stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, setting, screen):
    """在玩家点击playbutton后开始新游戏，game_stats.game_active状态变化"""
    # 添加参数play_button, 以确定玩家是否单击了play按钮
    # game_stats 以访问game.active
    #为了解决在游戏开始后玩家点击 原来区域的位置是，游戏任然会做出相应并重新开始，我们添加了限制条件，当game_active为false时才能。
    play_button_collide = play_button.button_rect.collidepoint(mouse_x, mouse_y)
    if (game_stats.game_active == False) and play_button_collide:
        #游戏设置被初始化
        setting.game_setting_initizlization()

        #检查鼠标是否在button的rect内
        #重置游戏统计信息
        #此处就用上了，不是在游戏初始化时使用，而是游戏结束后使用。游戏重置状态为3次。
        #每次结束游戏后，用户点击开始按钮后触发重新开始，但是外星人数量和子弹可能都变了，
        # 不能称职为新的开始。以为新的游戏开始的条件包括状态为True，飞船数量不能小于0，分数和外星人都必须
        # 是全新的。
        game_stats.reset_stats()
        game_stats.game_active = True

        #游戏开始后隐藏光标
        pygame.mouse.set_visible(False)

        # 清空子弹和外星人列表
        aliens.empty()
        bullets.empty()

        # 创建一批新的外星人，并将飞船位置居中
        creat_fleet(setting, screen, aliens, ship)
        ship.ship_center()

def check_events(game_stats, play_button, aliens, bullets, ship, setting, screen):
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
            check_keydown_event(event, setting, ship, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        #检查鼠标点击事件
        elif event.type == pygame.MOUSEBUTTONDOWN:

        # 通过检查游戏按钮是否与鼠标指针发生碰撞，修改游戏状态
            mouse_x, mouse_y = pygame.mouse.get_pos() #返回一个元祖
            check_play_button(game_stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, setting, screen)

def update_screen(setting, screen, ship, bullets, aliens, play_button, game_stats):
    """更新屏幕上的图画并切换到新屏幕"""
    # 每次循环时都会重新重绘画面
    screen.fill(setting.bg_color)

    #重新绘制飞船
    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    # 绘制外星人群
    for alien in aliens:
        alien.blitme()

    """如果游戏处于非活动状态，就绘制play按钮"""
    #放在这个位置，表示让这个按钮位于其他图标的上面，因此在绘制其他所有游戏元素后再绘制这个图标
    if not game_stats.game_active:
        play_button.draw_button()


    # 让最近绘制的屏幕可见
    pygame.display.flip()
